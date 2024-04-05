# Report on the Implementation of the Proposed Smart Meter Privacy Enhancing System

Group 7: Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

## Privacy First Energy Management 

Our research has indicated that from the aggregated energy consumption data collected by smart meters of individual households, it is possible to infer consumers’ behavior and household properties. In order to avert this tracking and inference of personal routines while still maintaining the original functionality of the smart meter system, we introduce the PrivacySmart Smart Metering system. 

This system contains two main structures. The first of which is a central data concentrator that serves as an intermediary between individual smart meters and the central meter data management system. As the smart meters collect homeowner data, they encrypt the data using AES encryption before transmission. Our system adds an additional layer of encryption within the data concentrator such that upon receipt, the data concentrator decrypts the AES encrypted data and immediately re-encrypts the data using Paillier encryption. This encrypted data is then transmitted to the Meter Data Management System (MDMS) where computations can be performed on the data without the need for decryption. The second structure in our system is a secure process for sending encrypted energy data from smart meters to a user interface (UI) component. 

## Requirements 
[recap on requirements we described in M3 linked to the problem statement detailed in M1 and M3 - also mention the problem statement]

The most pressing function and privacy requirement of the SmartPrivacy Smart Metering system is the anonymity of smart meter data and customer confidentiality during billing and analysis. Our system achieves this through multiple steps of encryption. Specifically, the data is immediately encrypted with AES at collection and then decrypted and re-encrypted immediately with the Paillier encryption scheme. The Paillier cryptosystem is known for its homomorphic properties that allow computations to be performed on encrypted data without decrypting it. This enables the utility company to perform necessary operations like billing and monitoring energy consumption trends on encrypted meter readings without compromising individual users’ privacy. This scheme renders it unnecessary for raw individual data to be handled at any time. 

[other requirements]

## Simulation 
In order to demonstrate and implement our system, we have generated a simulation of smart meter readings using data from a 2016 data set from the University of Massachusetts Amherst. 
- Choice of code language etc 
- Basic overview


## AES Encryption Implementation 

Consistent with current smart meter system implementations, we utilized AES encryption in our simulation in the initial generation and transition of the smart meter data. This was achieved through utilizing a Python package, PyCryptodome, that contains low level cryptographic primitives.

For our meter readings, we specifically used Galois/Counter Mode (GCM). This mode offers the added benefit of data integrity alongside encryption, which is particularly important regarding our main goals to ensure data remains confidential and that it has not been tampered with.


## Paillier Encryption Implementation
[Explain how it has been implemented, choice of algorithm - walk through the code, how it influenced the choice of the source code language]


**Idea: Show a before-after, graphically
