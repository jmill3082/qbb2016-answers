#!/usr/bin/env python

'''
This script reports the number of contigs in an assembly FASTA output file, as well as
the minimum, maximum, and average contig length and the N50 for the assembly.

Usage: >./contig-stats.py <input.fasta>
'''

# As usual, we want to import the modules/packages we'll be needing for the rest of the code.

import sys
import fasta
import numpy as np

# Let's initialize a list for the sequence lengths.

lengths = []

# Next, we want to actually open FASTA file with out assembly contigs and go through it one
# sequence at a time.

for ident, sequence in fasta.FASTAReader( open( sys.argv[ 1 ] ) ):
    
    # Now, for each of the sequences, we add the length of the sequence to the list.
    lengths.append( len( sequence ) )
    lengths = sorted( lengths )
    
# Diagnostic:
# print lengths

# We need to do some rithmatikin to get to the N50.

sum_of_lengths = sum( lengths )
half = ( sum_of_lengths / 2 )

# Diagnostic:
# print sum_of_lengths
# print half

# We want to count up to the N50.

count = 0
i = 0

for i in lengths:
    count = count + i  
    
    # Diagnostic:
    # print "i = %s." % i
    # print "count = %s." % count
    
    if count <= half:
        i = i + 1
        
    elif count > half:
        n50 = i
        break
    
# Now, let's get some other useful values.

contig_number = len( lengths )
minimum_length = min( lengths )
maximum_length = max( lengths )
average_length = np.mean( lengths )

# Finally, let's report some stuff.
print "The number of contigs is %s." % contig_number    
print "The maximum contig length is %s." % maximum_length
print "The minimum contig length is %s." % minimum_length
print "The average contig length is %s." % average_length
print "The N50 is %s." % n50    
       

    
    