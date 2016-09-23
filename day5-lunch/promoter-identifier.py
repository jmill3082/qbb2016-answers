#!/usr/bin/env python

"""
Creates a .bed file with the approximate promoter regions...
"""

# Let's import all of the standard stuff we probably need...
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = open( sys.argv[1] )

chromosomes = ["2L", "2R", "3L", "3R", "4", "X"]

for line in f.readlines():
    fields = line.rstrip( "\r\n" ).split( "\t" )
    
    if fields[1] not in chromosomes:
        continue
    
    else:    
        if "+" in fields[2]:
            print fields[1] + "\t" + str(int(fields[3]) - 500) + "\t" + str(int(fields[4]) + 500) + "\t" + fields[5]
        elif "-" in fields[2]:
            print fields[1] + "\t" + str(int(fields[4]) + 500) + "\t" + str(int(fields[3]) - 500) + "\t" + fields[5]









 