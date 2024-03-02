# Title
**Group 7:** Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

Note: Use footnotes[^0] for references and links to relevant material.

[^0]: https://gitlab.cs.mcgill.ca/martin/comp555-winter2024/-/blob/main/project/Milestone-3.md

## 1. System Purpose and Scope
*Determine the main function of the system and its functional boundaries. For example, is this a podcast listener? An information website? An image sharing tool? Clarify any potential ambiguity about the extent of the functionality it would cover. Identify the main privacy requirements. You are encouraged to stick to the core functionality. Be careful of [scope creep](https://en.wikipedia.org/wiki/Scope_creep), and of including requirements that would be difficult or impossible to prototype in a demonstration application (e.g., automotive software).*

(Our system consists of X and Y component) (Our focus will be on) The main function of our system is to anonymize the smart meter data collected and encrypt communications between the smart meter and the system. Smart meter data typically includes sensitive information about energy usage patterns, which, if exposed, could lead to privacy concerns and security risks for individuals (or organizations?). We wish to anonymize this data to ensure that privacy is maintained while still allowing for useful analysis and insights to be drawn from the aggregated information (e.g. for load balancing purposes, etc). We also wish for customers to be able to access a detailed breakdown of their energy consumption without needing to reveal those details to anyone else. (TODO: clarify that we have 2 components, and be more precise/clear)

## 2. Similar Systems
*To help in your requirement elicitation, make sure to consider the state of the art in terms of systems in the same class. Presumably these would be systems that are _not_ implemented following the principles of Privacy by Design. Envision this section as a kind of comparison between your future system and the existing "competition" (see [the Threema docs](https://threema.ch/en/messenger-comparison) for an example of what this can look like).*

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

#### Scenario 1: Smart Meter Data Transmission and Processing

- **Overview:** How the system processes the information transmitted from the smart meters in order to give the suppliers the data needed for individual billing and neighborhood-level forecasting.

- **System state:** The Data Concentrator and MDMS have been initialized with the necessary encryption and decryption keys.

- **System environment:** The system environment is operating normally, without problems.

- **External stimulus:** Individual smart meters transmit AES-encrypted energy consumption data to the Data Concentrator at regular intervals.

- **Required system response:** Every time the Data Concentrator receives the AES-encrypted data from individual smart meters, it decrypts it (DataDecryption component) before immediately re-encrypting it using Paillier Encryption (PaillierEncryption component). Then, the data is aggregated in two ways (DataAggregator component):
    1. The system aggregates the encrypted data at the neighborhood level, preserving the privacy of individual consumers while allowing useful analysis such as demand forecasting.
    2. The system aggregates the encrypted data at the individual level until it has collected 3 hours worth of individual data. This allows the individual data to be sent after longer intervals of time to reduce the sensitivity of the data while still allowing for accurate billing.

The aggregated data is then transmitted securely to the central meter data management system for further analysis and processing.


#### Scenario 2: User Access to Detailed Energy Consumption Data
- **Overview:** 
- **System state:** 
- **System environment:** 
- **External stimulus:** 
- **Required system response:** 

