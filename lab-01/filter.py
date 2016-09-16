#!/usr/bin/env python

'''
This script takes an aligned FASTA file, output from BLAST, and removes gaps, as well as any sequences that are shorter than the query sequence.
The script requires an input text file obtained from BLAST search, as well as the query file used for the BLAST search in FASTA format. Output is 
stdout in FASTA format.
Usage:
            >./filter.py <input.file> <query.fa> 
'''

# We want to import the modules/packages we'll be needing for the rest of the code.

import sys
import fasta

# First, let's get the length of the query, which we will use later.

for ident, sequence in fasta.FASTAReader( open( sys.argv[ 2 ] ) ):

        query_length = len( sequence )
    
    # Diagnostic:
    # print ident, sequence
    
# Now, let's open the input file and read each line to filter out the sequences that we want to align.

f = open( sys.argv[ 1 ] )

for line in f.readlines():
    
    # And the first thing that we'll do is a conditional, to ensure that we'll only
    # use processor time for the sequences we are interested in.
    
    # Diagnostic:
    # print line
    
    fields = line.rstrip( "\r\n" ).split( "\t" )
    
    # Diagnostic:
    # print fields[0]
    # print fields[1]
    # print fields[2]
        
    if int(fields[1]) != 1:
        
        # Diagnostic:
        # print fields[0]
        
        continue
        
    elif int(fields[2]) < len( sequence ):    
        
        # Diagnostic:
        # print fields[0]
        
        continue
        
    else:
        fields[3] = fields[3].replace( '-', '' )  
        
        # Diagnostic:
        # print fields[0]
        # print fields[1]
        # print fields[2]
        
        print ">" + fields[0]
        print fields[3]
        
        
f.close() 
    