#!/usr/bin/env python

"""
Performs linear regression to determine if the mean ChipSeq signal upstream of a putative TSS
for a candidate sequence is predictive of expression by comparing to FPKM data.

Usage:  >./RegressThis.py <tab_file> <ctab_file>
        >./RegressThis.py 893-3K4me3.tab 893.ctab
"""

# Let's load the necessary modules...
from __future__ import division
import sys
import numpy as np
import matplotlib as mp
import statsmodels.api as sm

# Now need to open the files containing the data that we need to evaluate...
f = open( sys.argv[2] )
g = open( sys.argv[1] ) 


# Let's get the FPKM values from the ctab file first and put them into a dictionary.
chromosomes = ["2L", "2R", "3L", "3R", "4", "X"]

FPKM = {}

for line in f.readlines():
    ffields = line.rstrip( "\r\n" ).split( "\t" )
    
    if ffields[1] not in chromosomes:
        continue
    elif ffields[5] not in FPKM:    
        FPKM[ffields[5]] = ffields[11]
    elif ffields[5] in FPKM:
        FPKM[ffields[5]].append(ffields[11])
#    else
#        print "Somethin's RONG."
#        quit()
        
# Diagnostic
# print FPKM

# Next, let's get make an x series and y series from the FPKM values and the signal values.
x = []
y = []

for line in g.readlines():
    gfields = line.rstrip( "\r\n" ).split( "\t" )
    
    # Diagnostic:
    # print FPKM[gfields[0]]
    x.append( float(FPKM[gfields[0]]) )  
    y.append( float(gfields[5]) )

# Diagnostic:
# print len(x)
# print type(x)
# print len(y)
# print type(y)

# Now, do some regressssssing

model = sm.OLS(y, x)
results = model.fit()
print results.summary()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        