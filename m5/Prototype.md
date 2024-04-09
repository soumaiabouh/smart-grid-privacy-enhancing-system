# Report on the Implementation of the Proposed Smart Meter Privacy Enhancing System

Group 7: Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

## 1. Smart Metering and Privacy-First Energy Management 

Our research has indicated that from the aggregated energy consumption data collected by smart meters of individual households, it is possible to infer consumers’ behavior and household properties. In order to avert this tracking and inference of personal routines while still maintaining the original functionality of the smart meter system, we introduce the PrivacySmart Smart Metering system. 

The PrivacySmart system includes two main components:

1.	**Privacy Enhancement System (PES):** At the heart of our system, the PES functions as the principal unit for encrypting and processing energy consumption data. Smart meters encrypt household energy data using the Advanced Encryption Standard (AES) before sending it to the PES via the Data Concentrator. At the PES, the AES-encrypted data is decrypted and immediately re-encrypted using the Paillier cryptosystem, adding an advanced layer of security. A key aspect of this process is that only a minimal amount of data is decrypted at any one time, reducing risk. Importantly, this granular data is not stored after processing, further ensuring consumer privacy. Additionally, the PES aggregates data to remove granularity before sending it to the Meter Data Management System (MDMS), where the aggregated data is encrypted using RSA. This aggregation step ensures that the MDMS receives data in a form that prevents the derivation of individual household behaviors while still enabling the performance of necessary statistical analyses and bill calculations directly on encrypted data, thereby maintaining stringent consumer privacy standards.

2.	**Secure Data Transmission to User Centric System (UCS):** Parallel to our privacy goals, the system ensures the secure transmission of encrypted energy data from smart meters to a User-Centric System (UCS). This element allows consumers to securely access detailed information about their energy consumption. The architecture guarantees that only the users associated with the specific smart meters can decrypt and view their granular data. This approach aligns with our objective to offer consumers privacy without hindering their ability to understand their energy usage. 

By integrating the PrivacySmart Smart Metering system's PES and secure data transmission protocols, we address crucial concerns about data confidentiality in the era of smart utilities, ensuring that smart meters can continue to provide valuable energy insights without compromising consumer privacy.


## 2. Requirements
[recap on requirements we described in M3 linked to the problem statement detailed in M1 and M3 - also mention the problem statement]

The most pressing function and privacy requirement of the SmartPrivacy Smart Metering system is the anonymity of smart meter data and customer confidentiality during billing and analysis. Our system achieves this through multiple steps of encryption. Specifically, the data is immediately encrypted with AES at collection and then decrypted and re-encrypted immediately with the Paillier encryption scheme. The Paillier cryptosystem is known for its homomorphic properties that allow computations to be performed on encrypted data without decrypting it. This enables the utility company to perform necessary operations like billing and monitoring energy consumption trends on encrypted meter readings without compromising individual users’ privacy. This scheme renders it unnecessary for raw individual data to be handled at any time. 

[other requirements]

## 3. Implementation of the System 

[First give overview - could use UML diagram here]

In order to demonstrate and implement our system, we have generated a simulation of smart meter readings using data from a 2016 data set from the University of Massachusetts Amherst. 
- Choice of code language etc 
- Basic overview

### 3.1 Simulation of Generation of Readings from Smart Meter 
*[Offer overview of the smart meters and state theat they are meant to be a simulation of actual smart meters]*

#### 3.1.1 Source Code Overview
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*

#### 3.1.2 AES Encryption Implementation 
Consistent with current smart meter system implementations, we utilized AES encryption in our simulation in the initial generation and transition of the smart meter data. This was achieved through utilizing a Python package, PyCryptodome, that contains low level cryptographic primitives.

For our meter readings, we specifically used Galois/Counter Mode (GCM). This mode offers the added benefit of data integrity alongside encryption, which is particularly important regarding our main goals to ensure data remains confidential and that it has not been tampered with.

### 3.2 Data Concentrator
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*

### 3.3 Privacy Enhancing System
*[Give intro, explain purpose of this and how it's supposed to be integrated]*

#### 3.3.1 Source Code Overview
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*


##### [DRAFT] How to ensure the individual data is not retrievable from the database's standpoint?
I have data that is too granular, and I want to encrypt it, aggregate it using Paillier encryption, and then store the result of the aggregation in a database where it should be possible to decrypt the result. Now, if I share the key used in Paillier encryption to the database system, it could be possible to retrieve the granular data, but I want to prevent that while minizing security risks. How? By getting rid of the granular data as soon as we're done with. 

We encrypt the data using Paillier, then aggregate, and before sending anything to the database, we get rid of those individual readings from the Privacy Enhancement Subsystem. Then, we send the decryption key to the entities managing the database system so that they can operate on it (predictions, statistical analysis, bill calculation) If anything goes haywire, we're still good, since smart meters are designed to retain readings for a certain period. 

##### [DRAFT] Predictions and the statistical analysis
For the predictions and the statistical analysis, the entirity of the data from n smart meters from the same region can be aggregated over a certain period of time (1 hour). No need for data on the individual families. 

##### [DRAFT] Bill calculations
For the bill calculations, the data could be aggregated over a longer period of time, and then sent off. For example, for a single household, could send the total energy consumption over the last 2 hours instead of every 5 min. 


#### 3.3.2 Paillier Encryption Implementation
[Explain how it has been implemented, choice of algorithm - walk through the code, how it influenced the choice of the source code language]

[DRAFT]

Modules considered:
- [python-paillier](https://github.com/data61/python-paillier): A python library that can be installed via `pip install phe`. Easy to use, and allows for constant addition and multiplication on an encrypted value, as well as the addition of encrypted values. 
- [pailliercryptolib](https://github.com/intel/pailliercryptolib_python): Python library best suited for Intel CPUs. Works on the Ubuntu operating system as well Red Hat Enterprise Linux. Could potentially be used by installing the necessary dependencies in a docker container. 

**Performance check:** The performance depends on the hardware used, as well as the length of the encryption and decryption keys chosen. Best length? 
TODO: with a big amount of data, verify how significantly the performance changes in terms of time.

### 3.4 MDMS Manager
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*

### 3.5 MDMS
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*

## 4. Conclusion
*[Main lessons learned, areas to consider for improvement (choice of encryption and encryption algorithm is an example)]*
