# Architectural Framework for Privacy by Design in Smart Meter Systems
**Group 7:** Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

Note: Use footnotes[^0] for references and links to relevant material.

[^0]: https://gitlab.cs.mcgill.ca/martin/comp555-winter2024/-/blob/main/project/Milestone-3.md

## 1. System Purpose and Scope
*Determine the main function of the system and its functional boundaries. For example, is this a podcast listener? An information website? An image sharing tool? Clarify any potential ambiguity about the extent of the functionality it would cover. Identify the main privacy requirements. You are encouraged to stick to the core functionality. Be careful of [scope creep](https://en.wikipedia.org/wiki/Scope_creep), and of including requirements that would be difficult or impossible to prototype in a demonstration application (e.g., automotive software).*

Our privacy system is focused on averting the tracking and inference of personal routines through smart meter data while still maintaining original functionality. Our system takes the form of a data concentrator as an intermediary between individual smart meters and the central meter data management system. Data concentrators are typically used in utilities and telecommunications to collect, aggregate and manage data from multiple sources. They facilitate the communication of data between the meters and energy service providers but can also incorporate encryption, authentication and access control mechanisms ([source](https://www.ti.com/lit/wp/spry248a/spry248a.pdf?ts=1709191363299&ref_url=https%253A%252F%252Fwww.google.com%252F#:~:text=A%20data%20concentrator%20is%20the,to%20the%20central%20utility%20database.)). 

The core function and privacy requirement of our system is the anonymity of smart meter data. The way our system achieves this is two-pronged. First, through homomorphic encryption mechanisms, specifically Paillier Encryption, we ensure that individual consumption data remains private and cannot be accessed or linked to specific individuals without proper authorization. Following this, our system achieves private access control to detailed data with restricted supplier and third party access. Second, anonymity of smart meter data will be achieved by aggregating consumption data from individual smart meters into neighborhood level data. The purpose of aggregating data is to provide exactly the function of k-anonymity within a data set: pooling individual data into a larger group to hide individual values and reduce the granularity of the data. The aggregated data still will allow useful analysis, such as demand forecasting and accurate billing. 

In reference to future milestones, we acknowledge the inability to prototype or demonstrate a physical data concentrator or smart meter; however, we plan on generating a simulation of smart meter readings, smart meter to central data management system communication, and our privacy system with public smart meter data sets. 


## 2. Similar Systems
*To help in your requirement elicitation, make sure to consider the state of the art in terms of systems in the same class. Presumably these would be systems that are _not_ implemented following the principles of Privacy by Design. Envision this section as a kind of comparison between your future system and the existing "competition" (see [the Threema docs](https://threema.ch/en/messenger-comparison) for an example of what this can look like).*

We looked at four other companies and the security measures they take. We focused primarily on encryption, de-identification, privacy by design, and generalization by aggregation, as we will be implementing them into our system.
The first company is Landis+Gyr, and the Smart Meter we chose from them is the "IoT grid sensing electric meter". We found that in terms of security, they implement encryption through a 256-bit AES, digital image signing by validating all signatures on all firmware and application images, and they implement physical hardening by doing post-security and data-at-rest encryption.
The second company is Hydro One. They mention that data collected is processed by the Independent Electricity System Operator (IESO) before being used. IESO is a company that protects the privacy of Ontarians and does so by de-identifying data and aggregating it. Their system meets "the internationally recognized principles of Privacy by Design®".
The third company is EKM Metering Inc. They don't mention that they impement any specific data protection when it comes to data collection done by their meters. The only information they provide is that the data is stored in the cloud.
Finally, the fourth company is ONZO. ONZO does protect data through "secure data transfer, data encryption, multi-factor authentication, and role-based access controls distributed across a scalable, secure infrastructure, provided by Amazon Web Services". Even though ONZO might protect users' data, we've seen in our first report that they potentially give this data to third parties and that we don't know who these are.
As for our system and the ways we protect data, refer to section 6 about the architecture.

| Company  | Encryption  | Privacy By Design   |  De-Identification | Generalization by Data Aggregation  |
|---|---|---|---|---|
| Landis+Gyr  |  :white_check_mark: | :x:  | :x:  | :x:  |
| hydro one  | :x:  | :white_check_mark:  |:white_check_mark:   | :white_check_mark:  |
| EKM Metering Inc | :x:  | :x:  | :x:  |  :x:|
| ONZO | :white_check_mark:  | :x:  | :x:  |  :x:|
| Our system | :white_check_mark:  | :white_check_mark:  | :white_check_mark:  |  :white_check_mark:|




## 3. Functional Requirements
The system must protect consumer privacy by obfuscating personal routines and habits that can be derived from aggregated energy consumption data. The goal is to prevent unauthorized inferences from the energy supplier and possible third parties, while maintaining transparency in energy usage for the consumers.

### 3.1 Data Privacy and Access
1.	**Private Access to Detailed Data:** The system must allow the customer to access detailed energy consumption data via a private key that is unique to each user and not accessible by anyone else.
2.	**Restricted Supplier and Third-Party Access:** The system must ensure that suppliers and possible third parties can only access aggregated and anonymized data, with no capability to view individual and detailed customer energy consumption.

### 3.2 Communication and Data Handling
1.	**Smart Meter to MDMS Communication:** The system must include a secure communication component between the smart meters and the Meter Data Management System (MDMS) that encrypts data transmission.
2.	**Billing Data Averaging:** For billing purposes, the system must send averaged out data about each customer over longer intervals to prevent fine-grained consumption patterns from being revealed.
3.	**Supplier-Side Aggregation:** To inform the supplier about energy demands, the system must aggregate more detailed data among members of a neighborhood, ensuring individual user data remains private.

### 3.3 Data Encryption
1.	**End-to-End Encryption:** The system must encrypt data from the point of capture at the smart meter to the other components, ensuring data integrity and confidentiality.
2.	**Encryption Standards Compliance:** The system must employ strong encryption standards compliant with industry best practices for data in transit and at rest.

### 3.4 System Reliability and Performance
1.	**Real-Time Processing:** The system must be capable of processing real-time data for immediate access by the customer using their private key.
2.	**High Availability:** The system must ensure high availability for the continuous and reliable operation of smart meters and accessibility of MDMS.



## 4. Privacy Requirements
*List, using a structured format (e.g., enumerated lists organized by section) the main privacy requirements your system will support.*

### 4.1 Data Anonymity and Customer Confidentiality
1. Ensure personally identifiable information is stripped from collected data to prevent identification
### 4.2 Encryption
### 4.3 Data Minimization 
1. Collect only the necessary data required for billing and system operation. Minimize the collection of personal information beyond what is essential for providing services. 
### 4.4 Transparency and Consent 
1. Inform users about the data being collected and obtain explicit consent to do so. 
2. **User Control**: provide users with the option to control their data


For reference, the following activities 5-6-7 are described in detail in [Rozanski and Woods Ch. 13](https://mcgill.on.worldcat.org/oclc/794554030).

## 5. Stakeholders
*Clarify who would be using you system, especially if there are different classes of users.*
The companies that own the smart meters would be using our system. They would implement our system between the data flow from the smart meters to their database. If we were to look at the whole process then there's also users that get involved by providing data, but they do not use our system, they just provide data to our system.

## 6. Architectural Design Decisions and Models:
*Elicit a high-level decomposition of your system into components, modes of communication, major technology used, etc. Be sure to represent decisions that have an impact on privacy. Create one or more original diagrams representing the key aspects of the system. UML is strongly recommended. Ad hoc boxologies are not recommended. The model should be consistent with the decisions elicited.*

### 6.1 General Overview of the System
[Insert overview of the system here]

### 6.2 Algorithm Choice for Data Encryption
We want to anonymize user data while enabling the suppliers to perform the operations they need on the data, i.e., calculating the billing fees as well as being able to monitor the general energy consumption of particular neighborhoods.  For this purpose, we propose the use of Paillier Encryption.

#### Context and Considerations for Using Paillier Encryption:
- **Privacy:** Paillier encryption preserves the confidentiality of individual users' data while allowing the aggregation needed for billing and supply forecasting. 
- **Regulatory Compliance:** Using encryption to protect user data can help in meeting data protection regulations.
- **Performance:** While homomorphic encryption is generally slower than traditional encryption methods, Paillier is relatively efficient for addition operations, which is the primary operation needed for aggregating energy usage data.

#### Alternatives Considered and Rejected:
- **Symmetric Encryption:** Rejected due to the single point of failure in key management and lack of support for operations on encrypted data. 
- **Asymmetric Encryption:** While it provides secure data transmission, it does not support homomorphic properties for processing aggregated data.
- **Non-encrypted Aggregation:** Not considered due to non-compliance with privacy requirements.

#### Rationale for Choosing Paillier Encryption:
- It enables additive homomorphic properties, meaning that the system can compute the sum of encrypted user data without decrypting it, which is suitable for generating aggregated statistics.
- It does not require the sharing of decryption keys with the data processor (supplier), which reduces the risk of exposing individual user data.


## 7. Important Scenarios:
*Identify and describe important scenarios. A scenario is "a well-defined description of an interaction between an external entity and the system. It defines the event that triggers the scenario, the interaction initiated by the external entity, and the response required of the system" [Rozanski and Woods]. You can represent scenarios using plain text or UML Sequence Diagrams. The scenarios you choose should be relevant to the privacy requirements and be generally useful for developing and communicating your system architecture.*

