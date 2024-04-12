# Report on the Implementation of the Proposed Smart Meter Privacy Enhancing System

Group 7: Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

## 1. Smarter Metering and Privacy-First Energy Management 

Our research has indicated that from the aggregated energy consumption data collected by smart meters of individual households, it is possible to infer consumers’ behavior and household properties. In order to avert this tracking and inference of personal routines while still maintaining the original functionality of the smart meter system, we introduce the Smarter Metering system. 

The Smarter Metering system includes two main components:

1.	**Privacy Enhancement System (PES):** At the heart of our system, the PES functions as the principal unit for encrypting and processing energy consumption data. Smart meters encrypt household energy data using the Advanced Encryption Standard (AES) before sending it to the PES via the Data Concentrator. At the PES, the AES-encrypted data is decrypted and immediately re-encrypted using the Paillier cryptosystem, adding an advanced layer of security. A key aspect of this process is that only a minimal amount of data is decrypted at any one time, reducing risk. Importantly, this granular data is not stored after processing, further ensuring consumer privacy. Additionally, the PES aggregates data to remove granularity before sending it to the Meter Data Management System (MDMS), where the aggregated data is encrypted using RSA. This aggregation step ensures that the MDMS receives data in a form that prevents the derivation of individual household behaviors while still enabling the performance of necessary statistical analyses and bill calculations directly on encrypted data, thereby maintaining stringent consumer privacy standards.

2.	**Secure Data Transmission to User Centric System (UCS):** Parallel to our privacy goals, the system ensures the secure transmission of encrypted energy data from smart meters to a User-Centric System (UCS). This element allows consumers to securely access detailed information about their energy consumption. The architecture guarantees that only the users associated with the specific smart meters can decrypt and view their granular data. This approach aligns with our objective to offer consumers privacy without hindering their ability to understand their energy usage. 

By integrating the Smarter Metering system's PES and secure data transmission protocols, we address crucial concerns about data confidentiality in the era of smart utilities, ensuring that smart meters can continue to provide valuable energy insights without compromising consumer privacy.


## 2. Requirements
[recap on requirements we described in M3 linked to the problem statement detailed in M1 and M3 - also mention the problem statement]

The most pressing function and privacy requirement of the Smarter Metering system is the anonymity of smart meter data and customer confidentiality during billing and analysis. Our system achieves this through multiple steps of encryption. Specifically, the data is immediately encrypted with AES at collection and then decrypted and re-encrypted immediately with the Paillier encryption scheme. The Paillier cryptosystem is known for its homomorphic properties that allow computations to be performed on encrypted data without decrypting it. This enables the utility company to perform necessary operations like billing and monitoring energy consumption trends on encrypted meter readings without compromising individual users’ privacy. This scheme renders it unnecessary for raw individual data to be handled at any time. 

[other requirements]

## 3. Implementation of the System 

[First give overview - could use UML diagram here]

In order to demonstrate and implement our system, we have generated a simulation of smart meter readings using data from a 2016 data set from the University of Massachusetts Amherst. 
- Choice of code language etc 
- Basic overview

### 3.1 Simulation of Generation of Readings from Smart Meter 
The smart meter class, available in smart_meter.py, encapsulates the functionality of a smart meter, which collects energy consumption data and transmits it to the PES. 

#### 3.1.1 Source Code Overview
Upon initialization, the smart meter instance requires the PES public key, a filename containing energy consumption data and an optional parameter specifying the number of readings to load initially. During initialization, the system generates a random AES key for data encryption, encrypts it using PKCS-OAEP (Public-Key Cryptography Standards - Optional Asymmetric Encryption Padding) encryption with the PES public key, and generates a unique identifier for the smart meter. 
PKCS-OAEP is designed to enhance the security of RSA encryption by adding randomness to the plaintext before encryption. 


#### 3.1.2 AES Encryption Implementation 
Consistent with current smart meter system implementations, we utilized AES encryption in our simulation in the initial generation and transition of the smart meter data. This was achieved through utilizing a Python package, PyCryptodome, that contains low level cryptographic primitives. Our research demonstrated that this package is widely used for cryptographic operations and is considered secure when used correctly. 

For our meter readings, we specifically used Galois/Counter Mode (GCM). This mode offers the added benefit of data integrity alongside encryption, which is particularly important regarding our main goals to ensure data remains confidential and that it has not been tampered with. For our smart meters, we decided to implement 256 bit keys since our priority was increased security. Longer keys typically increase the difficulty of any cryptanalysis or brute force attacks and may provide an additional security margin. 
Ultimately, the success of AES implementation depends on proper key management. 


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


### 3.4 MDMS
The MDMS is an interface supplied to companies using our software. It ensures that the data these companies can view is aggregated and de-identified, thus providing better user privacy. The MDMS has two main components: the MDMS UI and the MDMS database.

#### 3.4.1 MDMS Manager
The MDMS Manager is a Node app. When running the app, the user receives a URL. The URL brings the user to a login page. This page is for an admin from the company using our product. Once in the MDMS, the admin can look at smart meters and the relative statistics. The statistics link brings the admin to the statistics page and displays the power consumption and bill for the selected smart meter.

In section 2, one of the main requirements is anonymity and confidentiality. These are done in previous steps using AES as well as Pallier. The MDMS manager ensures that the data displayed to the admin does not divulge which smart meter belongs to whom, as the IDs are encrypted. The data is pulled from the MDMS database, further explained in section 3.4.2. As the data from the database is aggregated and encrypted, this enforces that the admin cannot infer consumer behavior or household routines from the data that they have access to.

#### 3.4.1 MDMS Database
To simulate smart meter data production data from an open source is used. The data is in the c555w24/m5/src/data folder. There are CSV files for each apartment with a smart meter that contain the power consumption collected using a 1 minute time interval over a year. This data is aggregated by the PES, as explained in section 1. Once aggregated by the PES and made less granular by Pallier, the data is encrypted using RSA rather than keeping the data Pallier encrypted. Pallier encryption is powerful, but it introduces a significant overhand when it performs multiple calculations within a short amount of time. This is problematic in the context of interacting with the MDMS Manager UI. This is why RSA is a better choice in this scenario. The RSA data is stored on the MDMS Database, which is a MongoDB Atlas database. 

In the c555w24/m5/src/mdms-ui folder, there is a file called app.js. This is the only file in the Node app that contains code to access the MongoDB database. It connects to the database by calling "MongoClient" on a link provided by MongoDB and then using a connect function on the object returned.
Within the app.js file, there are multiple functions that query data from the database, such as "app.get('/statistics'". This function is triggered when the browser does a GET request to get the statistics page. The function then does a query to get apartment IDs and then alters the statistics page to display this data.


### 3.5 User Centric System
One of our main requirements was the ability for customers to have secure access to their own energy consumption data. This aspect of our system is achieved through the user_centric_system.py class which is accessible within the folder src and referred to in the following sections.  

When a user first generates their username and password, the setCredentials function on line 40 initializes multiple values. First, the individual’s username is set and saved. Next, a random 16 byte string, referred to as the _salt_, is generated from the Crypto.Random package. Similarly, an RSA key pair is generated where the keys are each 2048 bits of length. The user’s public key is utilized to encrypt the user’s smart meter’s symmetric key. Lastly, the user’s password is hashed using the salt that was previously generated and a helper function derive_key on line 105. 

#### 3.5.1 Hashing Passwords

This helper function uses a password based key derivation function (PBKDF2) also from the Crypto package. It operates by repeatedly applying a pseudorandom function to the input password along with the salt. The function used in this class is a Hash-Based Message Authentication Code (HMAC) that uses SHA-256 cryptographic hash function as the underlying hashing algorithm. SHA-256 is considered widely secure for most cryptographic applications, resulting in our decision to use this hash function over the default SHA-1, which is now considered vulnerable due to collision attacks. The number of iterations corresponds to the computational cost and makes the result more resistant to brute-force attacks. Currently, this code uses 1000000 iterations and generates a hash of length 32 bytes. PBKDF2 performs key derivation according to the second version of Public Key Cryptography Standards (PKCS). This hash is stored as the user _hashed_password_ and we are never storing user passwords directly. In order to authenticate our users, when they enter their password, this hash is regenerated and compared with our stored hashed_password. Since SHA-256 is deterministic and we are also storing the salt value, this allows for these hashes to be regenerated and used for secure authentication.  

Hashing passwords provides an additional layer of security since if a hacker were to obtain the hashed passwords, they are not immediately usable without knowledge of the original passwords. This maintains confidentiality by preventing unauthorized access to sensitive information. Lastly, since a unique salt is generated for every user, the hash of a user password will be unique for every user, even if the user’s have the same password (given the possibility of collisions is extremely low for the many possible salt values and SHA-256 outputs).  

#### 3.5.2 Displaying Data 
As previously mentioned, there is a smart meter associated with every User Centric System instance. The smart meter’s encryption key can therefore be encrypted with the user’s RSA public key in order for safe transfer of the key between the two components, effectively resolving the key distribution problem. We utilize this process in our display function on line 21. The smart meter’s AES key is decrypted using the user’s private key, allowing for access of the raw consumption data. This data is then graphed using a data visualization library, Plotly.  

We want to emphasize that our system ensures the secure delivery of this data and the creation of an actual interface used by customers to view this data was decided to be out of our scope. This interface will handle the specifics of display and potentially incorporate other functionalities. Our file is simply to demonstrate a simulation of the flow of the data, a basic example of a user system, and ensure that suppliers don’t need to directly observe customer data. 


### 3.6 UI
*[Go over parts of the source code or simply refer to it, and explain how it fits the requirements stated in section 2]*

## 4. Conclusion
### 4.1 Limitations 

We have identified a few limitations regarding the actual implementation of our system architecture. The first is regarding our usage of Paillier encryption. This cryptosystem involves complex mathematical operations and large key sizes in comparison to other encryption schemes like AES. For instance, a typical AES key is 256 bits while the typical key size for Paillier is 2048 bits or higher. As a result, there is a significant computational overhead when utilizing this scheme for encryption and decryption. Ultimately, we decided that for our system, the homomorphic properties and privacy benefits resulting from Paillier encryption outweighed its requirement for more computational resources. 

We also acknowledge a potential point of weakness with our decryption and immediate re-encryption in the privacy enhancing system. Since our smart meter data is sent incrementally, this process within the PES only involves small batches of data to limit this potential window of vulnerability. 

Lastly, we acknowledge the potential for function creep in the implementation of a smart meter system. This is because smart meters themselves are responsible for obtaining energy consumption data and it could be possible to modify the system to store data. To avoid this, we would have to modify the smart meters themselves so that they would do the aggregation internally. Since smart meters are already widely deployed, this fix is not likely which is why we propose our system instead. 

### 4.2 Lessons
