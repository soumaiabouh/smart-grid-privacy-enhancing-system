# Report: Analysis of Smart Meters
## Introduction
_An introduction that describes and delineates, as clearly as possible, the case/situation you targeted._

- In Canada, 82% of installed meters are smart meters, with several provinces investing in research labs that focus on smart grids and their related technologies [[1](https://static4.arrow.com/-/media/arrow/files/pdf/0821/te_trend-paper-smart-metering_0521_en.pdf)].
- Smart meters do not directly manage energy distribution. Instead, they inform customers about their energy use and assist providers in optimizing energy distribution [[2](https://www.arrow.com/en/research-and-events/articles/what-is-a-smart-grid-and-how-does-it-work)].
- Smart meters help customers save on electricity bills and enable energy providers to reduce costs by detecting leaks and outages for quicker responses. Additionally, analyzing consumption data helps in understanding customer behavior, planning better services, and making strategic decisions for future investments and emergency planning [[1](https://static4.arrow.com/-/media/arrow/files/pdf/0821/te_trend-paper-smart-metering_0521_en.pdf)].
- Traditional systems track electricity use through devices attached to meters or clamps. This data is sent wirelessly to displays or online interfaces. The smart meters adopted in the UK and several other countries improved on this with two-way wireless communication, allowing energy providers, home devices, and displays to interact. These advanced displays can keep track of energy use over time and allow data transfer to computers using USB. Online interfaces provide detailed analysis through automatic graphs and spreadsheets [[3](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5353784)].
- A home equipped with a Smart Grid system necessarily implies that it contains a smart meter that collects electricity usage data at regular intervals, such as every 30 minutes. This frequent data collection may assist in enhancing grid management for operators and enables energy suppliers to issue accurate and timely bills to their customers [[4](https://ieeexplore.ieee.org/document/8534430)].


## Research Method
_A research method section that describes, precisely enough to be replicated, the procedures you have followed to collect your data._


## Results
_A results section, which provides a well-organized overview of the results you collected, with cross-references to the appendix._

- Beckel et al. (2014); fine-grained electricity consumption data, collected by smart meters, can lead to identifying specific characteristics that may reveal information about a home’s socio-economic status, dwelling and appliances with an accuracy of more than 70% for all households.  
- Monitoring electricity consumption can allow for others to make inferences about what appliances are being used, whether an individual is home or not, and even what program is being watched on TV. 
    - Appliances all have different energy usages. Reading these patterns reveals which is being used. 
    - Dennis Loehr and fellow researchers at Muenster University of Applied Sciences in Germany have demonstrated that a household electrical usage profile reveals the lighting patterns (amount of light and dark emitted on the display for individual frames); lighting patterns are unique for each TV program and movie and thus could be compared. Their results show that two 5-minute chunks of consecutive viewing without major interference of other appliances is sufficient to identify the content. 
- Onzo has stated directly that they utilize energy consumption data from smart meters to build a highly personalized profile for every energy customer. They tag the appliances being used in the home and use this virtualized profile to monetise their customer data by selling to third parties for the purpose of targeting customers with products and services relevant for that household. 
- Smart meters face risks like cyber-attacks, tampering, and data privacy issues. Both manufacturers and utility companies are normally responsible for protecting these meters and the data they send. To secure the meters and data, they may need to use strong communication rules, control who can access the system, and encrypt data whether it is stored or being sent. On the manufacturing side, security measures may include setting up device keys, security certificates, and specific settings to ensure the information is secure and trustworthy [[1](https://static4.arrow.com/-/media/arrow/files/pdf/0821/te_trend-paper-smart-metering_0521_en.pdf)].
- As a paper published in 2018 by Cleemput et al. demonstrated, it is possible that an attacker can completely remove the anonymity from users’ detailed metering data by employing a straightforward matching algorithm. The researchers examined whether a supplier could extract additional insights from collected electricity usage data. A supplier would normally have in their possession the SM IDs of the customers along with the detailed records of electricity consumed every half hour, which lacks personal identifiers. From the latter, it is trivial to calculate the aggregated monthly data that sums up total consumption per customer. The de-pseudonymization method involves analyzing customers' unique monthly aggregate consumption data, starting with the earliest month available. If a customer's monthly aggregate is unique, their detailed half-hourly data for that month directly identifies them. This process is repeated monthly, focusing on users not yet de-pseudonymized, progressively identifying individuals based on their consumption patterns [[4](https://ieeexplore.ieee.org/document/8534430)].


## Conclusions
_A conclusions section, which highlight the insights you can derive from the data you collected, with clear links to the evidence._

- From Beckel, we can conclude that it is possible to extract information from smart meters that consumers may prefer to keep private, including data related to income, employment status, status of relationship, or social class. 
- From Loehr, smart meters are able to become surveillance devices that monitor the behavior of customers and track personal routines 
- From Onzo, it's clear that utility companies utilizing smart meters have the capability to build generous personalized profiles of households. Homeowner data becomes more vulnerable as it is shared or traded. 

## Appendix
_An appendix, which contains larger data sets too cumbersome to put in the results section._

## References
