

# Machine Translation Alignment Tool
# Overview
This tool is designed to perform a beam-search decoder which is capable of reordering between a source language (e.g., French) and a target language (e.g.,English) based on parallel bilingual corpora.

# Table of Contents
1. Installation
2. Usage
3. Algorithms
4. Results
5. Contributors


# Installation
1. Make sure you have python and github on your system


2. Clone the repository to your local machine:  
   **git clone https://github.com/nicoledeprey/MachineTranslation_hw3.git**


3. Navigate to the project directory:  
**cd hw3**




# Usage
Running the Decoder


1. Train the alignment models using the following command:
**python decode > training**

2. To compute accuracy, run:
**Get-Content training | python compute-model-score**


4. To run the machine translation in one command, you can run: 
**python decode | python compute-model-score**

# Algorithms

1. Beam Search 

2. Coverage Vector


# Results
The code results should produce a total corpus log probability (LM+TM) of -2026.070383 (see figure below)
<img width="1710" alt="image" src="https://github.com/janvi-prasad/MachineTranslation_HW2/assets/60441779/b621a58e-4c8d-4bc5-9ad4-a92c28afcd3f">


  

# Contributors
This code was developed by Janvi Prasad, Nicole Deprey, and Hirtika Mirghani.
