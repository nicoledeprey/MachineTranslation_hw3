#!/usr/bin/env python
import argparse
import sys
from collections import defaultdict
 
parser = argparse.ArgumentParser()
 
parser.add_argument("-d", "--data",
                    default="data/hansards",
                    help="Data filename prefix (default=data/hansards).")
 
parser.add_argument("-e", "--english",
                    default="e",
                    help="Suffix of English filename (default=e).")
 
parser.add_argument("-f", "--french",
                    default="f",
                    help="Suffix of French filename (default=f).")
 
parser.add_argument("-o", "--out",
                    default="dice.a",
                    help="Output path (default=dice.a).")
 
parser.add_argument("-t", "--threshold",
                    default=0.5,
                    type=float,
                    help="Threshold for aligning with Dice's coefficient "
                          "(default=0.5).")
parser.add_argument("-n", "--num_sentences",
                    default=999999,
                    type=int,
                    help="Number of sentences to use for training and "
                          "alignment.")
args = parser.parse_args()
f_data = "%s.%s" % (args.data, args.french)
e_data = "%s.%s" % (args.data, args.english)
 
bitext = [[sentence.strip().split() for sentence in pair] for
          pair in zip(open(f_data), open(e_data))][:args.num_sentences]
 

# Gets English+foreign vocabulary + uniformly initializes translation table
e_vocabulary = set()
f_vocabulary = set()
translation_table = {}
 
for (f, e) in bitext:
    for e_i in e:
        translation_table[e_i] = defaultdict(lambda : 1.0)
        e_vocabulary.add(e_i)
    for f_i in f:
        f_vocabulary.add(f_i)
       
# Iterates until convergeance  
for i in range(10):
   
    count = defaultdict(float)
    e_count = defaultdict(float)
   
    for (f, e) in bitext:        
        for f_i in f:    
            Z = 0
           
            for e_j in e:
                Z += translation_table[e_j][f_i]
               
            for e_j in e:
                c = translation_table[e_j][f_i] / float(Z)
                count[(f_i, e_j)] += c
                e_count[e_j] += c
               
    for pair in count:
            translation_table[pair[1]][pair[0]] = count[pair] / e_count[pair[1]]
 
# Writes out the aligments so they can be scored
 
for (f, e) in bitext:
    for (i, f_i) in enumerate(f):
        highest = 0
        index = 0
        for (j, e_j) in enumerate(e):
            if translation_table[e_j][f_i] > highest:
                highest = translation_table[e_j][f_i]
                index = j
        sys.stdout.write("%i-%i " % (i, index))
    sys.stdout.write("\n")
 
 #python3 ibm1.py -n 100000 | python3  score-alignments  -> gives an AER value of 0.369