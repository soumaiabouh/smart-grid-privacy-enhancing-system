# Smart Grid Privacy-Enhancing System

A comprehensive research and implementation project for protecting consumer privacy in smart meter systems while maintaining functionality for energy billing and demand analysis.

## Overview

This project addresses critical privacy concerns in smart grid technologies. Fine-grained energy consumption data collected by smart meters can reveal personal routines, household characteristics, occupancy patterns, and appliance usage—even with just one week of data. The Smart Grid Privacy-Enhancing System provides a solution through multi-layered encryption and data aggregation techniques to preserve consumer privacy without sacrificing the utility company's need for billing and energy analysis.

## Project Structure

### m1 - Domain Research & Analysis
Foundational research into smart meter technology and privacy implications.

- **Domain.md**: Comprehensive analysis of smart meters including:
  - Smart meter technology and global adoption trends
  - Energy disaggregation techniques (ILM and NILM)
  - Privacy risks and inference capabilities from consumption data
  - Real-world case study examining how personal information can be extracted from smart meter readings

- **Contributions.md**: Team contributions and project milestones
- **additional-documents/**: Supporting research materials and datasets

### m3 - System Architecture & Design
Detailed architectural design and comparative analysis.

- **Architecture.md**: Complete system architecture specification including:
  - System purpose and privacy requirements
  - Comparative analysis of existing smart meter security solutions
  - Functional requirements for data privacy, encryption, and communication
  - Stakeholder analysis (utilities, consumers, analysts)
  - Privacy by design principles implementation

- **CONTRIBUTING.md**: Guidelines for contributions

### m5 - Prototype Implementation
Complete working prototype of the privacy-enhancing system.

- **README.md**: Installation and usage instructions
- **Prototype.md**: Detailed implementation report including:
  - System component descriptions and design decisions
  - Encryption architecture (AES, Paillier homomorphic encryption, RSA)
  - Data flow and aggregation strategies
  - Code structure and class diagrams

- **Contributing.md**: Contribution guidelines
- **src/**: Python implementation of the system
  - `main.py`: Main entry point for system simulation
  - `smart_meter.py`: Smart meter simulation with AES encryption
  - `privacy_enhancing_system.py`: Core privacy module with Paillier encryption
  - `data_concentrator.py`: Data aggregation and collection
  - `mdms_manager.py`: Meter Data Management System integration
  - `user_centric_system.py`: Secure user interface for data access
  - `data/`: Sample datasets (2016 apartment electrical usage data from UMass)
  
- **mdms-ui/**: Web-based user interface
  - Node.js/Express.js application for viewing aggregated data and managing access
  - User authentication and role-based access control
  - Real-time dashboard for energy monitoring

## Key Features

- **Multi-layer Encryption**: AES encryption at smart meters → Paillier homomorphic encryption in Privacy Enhancing System → RSA for user access
- **Homomorphic Encryption**: Enables billing calculations and analysis directly on encrypted data without decryption
- **Data Aggregation**: Neighborhood-level aggregation prevents identification of individual consumption patterns
- **User Privacy**: Customers can access their detailed consumption data with secure authentication, while utility companies only receive aggregated/averaged data
- **Privacy by Design**: System follows privacy-first principles while maintaining all smart grid functionality

## Installation

### Requirements

- Python 3.7+
- Node.js and npm
- pip package manager

### Setup

Install required Python packages:

```bash
pip install pycryptodome
pip install phe
pip install tqdm
pip install openpyxl
pip install pymongo
```

Install Node.js dependencies:

```bash
npm install express mongoose
```

## Usage

### 1. Privacy Enhancing System

Navigate to `m5/src/` and run the main system:

```bash
python main.py
```

This simulates:
- Multiple smart meters collecting energy consumption data
- Encryption and aggregation in the Privacy Enhancing System
- Data transmission to the Meter Data Management System

### 2. Meter Data Management System (MDMS) UI

Navigate to `m5/src/mdms-ui/` and start the web interface:

```bash
node app.js
```

Access the dashboard with:
- **Username**: `adminTester`
- **Password**: `password`

The UI displays aggregated energy consumption data and system metrics.

### 3. User-Centric System (UCS)

For users to access their detailed consumption data:

```bash
python user_centric_system.py
```

Users can authenticate and securely view their individual smart meter readings.

## Architecture Highlights

- **Smart Meter**: Generates consumption readings and encrypts with AES before transmission
- **Data Concentrator**: Collects data from multiple meters
- **Privacy Enhancing System (PES)**: Decrypts AES → Re-encrypts with Paillier → Aggregates before sending to MDMS
- **MDMS**: Stores aggregated/averaged data for billing and analysis
- **User-Centric System**: Provides secure individual access to personal consumption data
- **MDMS UI**: Visualization and management interface for utility providers

## Team

**Group 7**: Ella Reck, Soumaia Bouhouia, Felicia Sun, Vanessa Akhras

## References

The project includes comprehensive citations to academic research on smart meter privacy, energy disaggregation, cryptographic techniques, and privacy-by-design principles. See the documentation in m1 and m3 for detailed references.
