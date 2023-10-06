# Machine Translation Decoder
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
This produces a total corpus log probability (LM+TM) of -1377.089720. A description of the Beam Search Algorithm can be found in the MathDescription.pdf. 

2. Coverage Vector
This produces a total corpus log probability (LM+TM) of -1259.093581. A description of the Coverage Vector Algorithm can be found in the MathDescription.pdf. 


# Results
The code results should produce a total corpus log probability (LM+TM) of -2026.070383 (see figure below)
<img width="1710" alt="image" src="https://github.com/nicoledeprey/MachineTranslation_hw3/decode-ext_resuts.jpg">


  

# Contributors
This code was developed by Janvi Prasad, Nicole Deprey, and Hirtika Mirghani.
