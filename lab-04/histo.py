#!/usr/bin/env python

"""
This script produces a histogram for minor allele frequency, given an input frqx file output from Plink2.

Usage:
    >./histo.py <input.frqx>

"""

# First, as always, let's import the packages that we'll need.
import sys
import matplotlib.pyplot as plt


# Now, we'll open our input frqx file.
f = open( sys.argv[1] )

# Let's initialize an array for the allele frequencies.
allelefreq = []

# Alright, now we start working on filling that array.
# We'll want to skip our header, so...
for line in f:
    if line.startswith("CHR"):
        continue

# Now, we need to extract the needed info, but we'll want to make sure the file is delimited correctly.        
    fields = line.rstrip("\r\n").split("\t")
    minor = float(fields[4])
    major = float(fields[6])
    allelefreq.append( (minor / (minor + major)))
    

plt.figure()
plt.hist(allelefreq)
plt.xlabel( "Minor Allele Frequency" )
plt.ylabel( "Occurences" )
plt.title("Minor Allele Frequency")
plt.savefig("allelefreq_histo.png")
plt.show()    