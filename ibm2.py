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
                    default="ibm2.a",
                    help="Output path (default=ibm2.a).")

parser.add_argument("-t", "--threshold",
                    default=0.5,
                    type=float,
                    help="Threshold for aligning with IBM Model 2 (default=0.5).")

parser.add_argument("-n", "--num_sentences",
                    default=999999,
                    type=int,
                    help="Number of sentences to use for training and alignment.")

args = parser.parse_args()
f_data = "%s.%s" % (args.data, args.french)
e_data = "%s.%s" % (args.data, args.english)

bitext = [[sentence.strip().split() for sentence in pair] for
          pair in zip(open(f_data), open(e_data))][:args.num_sentences]

# Initialize IBM Model 2 parameters
e_vocabulary = set()
f_vocabulary = set()
translation_table = {}
alignment_probabilities = {}

for (f, e) in bitext:
    for e_i in e:
        translation_table[e_i] = defaultdict(lambda: 1.0)
        e_vocabulary.add(e_i)
    for f_i in f:
        f_vocabulary.add(f_i)

# E-step: Estimate alignment probabilities using Model 2
for i in range(50):
    count = defaultdict(float)
    total = defaultdict(float)

    for (f, e) in bitext:
        for f_i in f:
            Z = 0

            for e_j in e:
                Z += translation_table[e_j][f_i]

            for e_j in e:
                c = translation_table[e_j][f_i] / float(Z)
                count[(f_i, e_j)] += c
                total[e_j] += c

    for pair in count:
        alignment_probabilities[pair] = count[pair] / total[pair[1]]

    # M-step: Estimate translation probabilities and fertility probabilities
    for (f, e) in bitext:
        for f_i in f:
            Z = 0

            for e_j in e:
                Z += alignment_probabilities[(f_i, e_j)]

            for e_j in e:
                translation_table[e_j][f_i] += alignment_probabilities[(f_i, e_j)] / Z

# Writes out the alignments so they can be scored
for (f, e) in bitext:
    for (i, f_i) in enumerate(f):
        highest = 0
        index = 0
        for (j, e_j) in enumerate(e):
            if alignment_probabilities[(f_i, e_j)] > highest:
                highest = alignment_probabilities[(f_i, e_j)]
                index = j
        sys.stdout.write("%i-%i " % (i, index))
    sys.stdout.write("\n")
