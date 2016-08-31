#!/usr/bin/env python

"""
This program parses the fly.txt file from UniProt, which contains cross-referencing information for switching between UniProt and FlyBase. The output of this file contains
only two columns - the first is the FlyBase accession number and the second is the UniProt accession number.
"""
import sys

f = open( sys.argv[1] )

for line in f.readlines():
    if "DROME" in line:
        fields = line.split()
        if len(fields) == 4:   
            print fields[3], "\t" , fields[2]
#            print line
    else:
        continue
        
f.close()
        
