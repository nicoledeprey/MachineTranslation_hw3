Machine Translation Alignment Tool
Overview
This tool is designed to perform word alignment for machine translation tasks using IBM Model 2. It translates and aligns words between a source language (e.g., French) and a target language (e.g.,English) based on parallel bilingual corpora.


Table of Contents
1. Installation
2. Usage
3. Mode
4. Sample Data
5. Results
6. Contributors


Installation
1. Make sure you have python and github on your system


2. Clone the repository to your local machine:
git clone https://github.com/janvi-prasad/MachineTranslation_HW2.git


3. Navigate to the project directory:
cd hw2




Usage
Training and Alignment


1. Train the alignment models using the following command:
Python ibm2.py -n 100000 > alignment
This will train IBM Model 2, estimating word alignment probabilities and stores the output in the file alignment.


2. To compute accuracy, run:
Get-Content alignment | python score-alignments 


3. To run the machine translation in one command, you can run: 
python ibm2.py -n 100000 | python score-alignments 
Models
Model Type: 


1. IBM Model 1: 
* IBM Model 1, is a simpler model for word alignment. It estimates the conditional probability of a foreign word given an English word. 
* It primarily estimates translation probabilities for each foreign word given an English word. 
* It calculates alignment probabilities based on the Dice coefficient.


* #python3 ibm1.py -n 100000 | python3 score-alignments -> gives an AER value of 0.369




2. IBM Model 2: 
* IBM Model 2, an extension of IBM Model 1. Model 2 incorporates a fertility model, which accounts for the number of words in the target language generated from a source language word. 
* It estimates both word translation probabilities and fertility probabilities. In addition to translation probabilities, Model 2 estimates fertility probabilities, which represent how many times a source word generates target words. 
* Alignment probabilities are calculated using Model 2, which involves both the E-step and M-step to estimate alignment and translation probabilities.


* #python3 ibm2.py -n 100000 | python3 score-alignments -> gives an AER value of 0.339943




Sample Data
Sample bilingual corpora and pre-trained models are provided for demonstration purposes. You can use these to quickly test the alignment tool. A description of the files are below.


* ‘hansards.e’ is the English side.
* ‘hansards.f’ is the French side.
* ‘hansards.a’ is the alignment of the first 37 sentences. The notation i-j means the word as position i of the French is aligned to the word at position j of the English. Notation i?j means they are probably aligned. Positions are 0-indexed.


Results
The code results should produce an alignment error rate of 0.339943 (see figure below)


  



Contributors
This code was developed by Janvi Prasad, Nicole Deprey, and Hirtika Mirghani.