# Report on the Implementation of the Proposed Smart Meter Privacy Enhancing System

Group 7: Ella Reck​, Soumaia Bouhouia​, Felicia Sun​, Vanessa Akhras​.

## Requirements 
[recap on requirements we described in M3 linked to the problem statement detailed in M1 and M3 - also mention the problem statement]

## Paillier Encryption Implementation
[Explain how it has been implemented, choice of algorithm - walk through the code, how it influenced the choice of the source code language]
### [DRAFT] Thought-process behind implementation

#### How to ensure the individual data is not retrievable from the database's standpoint?
I have data that is too granular, and I want to encrypt it, aggregate it using Paillier encryption, and then store the result of the aggregation in a database where it should be possible to decrypt the result. Now, if I share the key used in Paillier encryption to the database system, it could be possible to retrieve the granular data, but I want to prevent that while minizing security risks. How? By getting rid of the granular data as soon as we're done with. 

We encrypt the data using Paillier, then aggregate, and before sending anything to the database, we get rid of those individual readings from the Privacy Enhancement Subsystem. Then, we send the decryption key to the entities managing the database system so that they can operate on it (predictions, statistical analysis, bill calculation) If anything goes haywire, we're still good, since smart meters are designed to retain readings for a certain period. 

#### Predictions and the statistical analysis
For the predictions and the statistical analysis, the entirity of the data from n smart meters from the same region can be aggregated over a certain period of time (1 hour). No need for data on the individual families. 

#### Bill calculations
For the bill calculations, the data could be aggregated over a longer period of time, and then sent off. For example, for a single household, could send the total energy consumption over the last 2 hours instead of every 5 min. 

#### Paillier Encryption Algorithms
Modules considered:
- [python-paillier](https://github.com/data61/python-paillier): A python library that can be installed via `pip install phe`. Easy to use, and allows for constant addition and multiplication on an encrypted value, as well as the addition of encrypted values. 
- [pailliercryptolib](https://github.com/intel/pailliercryptolib_python): Python library best suited for Intel CPUs. Works on the Ubuntu operating system as well Red Hat Enterprise Linux. Could potentially be used by installing the necessary dependencies in a docker container. 

**Performance check:** The performance depends on the hardware used, as well as the length of the encryption and decryption keys chosen. Best length? 
TODO: with a big amount of data, verify how significantly the performance changes in terms of time.