#!/usr/bin/env python

"""
Match kmers from a query fasta file to kmers in a target fasta file. Returns the identity of the sequence in which a match was found,
the kmer sequence that was matched, and the positions in the target sequence and query sequence, respectively.

usage: kmer-matcher.py <target.fa> <query.fa> <k>
"""

import sys
import fasta

# kmer length is defined by the 3rd argument after the command when called in the command line.
# In the command line, the data type is string, so it must be converted to data type integer.
k = int( sys.argv[3] )

# Let's work first with the query sequence, store it, and then work line-by-line with the targets...

# Make a blank dictionary to put each unique kmer into with corresponding positions in the query sequence.
# Since we are going to be referring to the query more often, it makes sense to hash this one, rather 
# than hashing the target
Q_kmer_positions = {}

# Now, we can import the query sequence, and using the FASTAReader build the dictionary.
for ident2, sequence2 in fasta.FASTAReader( open(sys.argv[2]) ):
    
    # In case the sequence has any differences in case, which could cause problems in string matching, 
    # make all sequence upper case
    sequence2 = sequence2.upper()

    # Now, we will take each kmer in the query sequence we are working with, and make the dictionary.
    for j in range( 0, len(sequence2) - k ):
        kmer = sequence2[j : j + k ]

        # For each kmer, determine if it is new. There are only two cases. Either it is new, or it is not.
        # If it is new, add the kmer as a key and put the position into a new list. 
        # If it is not new, append the list with the new position.
        if kmer not in Q_kmer_positions:
            Q_kmer_positions[ kmer ] = [ j ]
        elif kmer in Q_kmer_positions:
            Q_kmer_positions[ kmer ].append( j )

        # Diagnostic:
        # print Q_kmer_positions

hits = {}

# Now that we have our query dictionary, let's work with the target sequences one at a time.
for ident, sequence in fasta.FASTAReader( open(sys.argv[1]) ):
    
    # In case the sequence has any differences in case, which could cause problems in string matching, 
    # make all sequence upper case.
    sequence = sequence.upper()
    
    # We want to get ALL of the possible matches, so we will do an exhaustive search at EVERY nucleotide.
    for i in range( 0, len(sequence) - k ):
        kmer = sequence [ i : i + k ]
        
        # Now what we want to do is check the query dictionary to see if the kmer from the target exists.
        # If not, we will continue on down the line. If so, then we need to perform the extension matching.
        if kmer not in Q_kmer_positions:
            continue
        elif kmer in Q_kmer_positions:
            
            # Diagnostic:
            # print ident
            # print kmer, sequence.index( kmer ), Q_kmer_positions[ kmer ]
            # print "\n"
            # I'm good up to here, I think. All of the kmers are reporting with the position on the target
            # as well as the list of positions in the query.
            
            target_start = i
            target_end = int( i ) + k - 1
            query_start = sequence2.index( kmer )
            query_end = int( sequence2.index( kmer ) ) + k - 1
            
            # Diagnostic:
            # print i, target_end
            # print Q_kmer_positions[ kmer ]
            # print sequence2.index( kmer ), query_end
            # print "\n"
            # Things seem to be going good up to this point. I have sequence names, kmers, and indices for 
            # both sequences.
            
            while sequence[ target_end ] == sequence2[ query_end ]:
                
                target_end += 1
                query_end += 1
                if target_end == len( sequence ) or query_end == len( sequence2 ):
                    break
                elif sequence[ int(target_end) ] != sequence2[ int(query_end) ]:
                    break
            
            if len( sequence[ target_start : target_end] ) > k:
                if ident not in hits:
                    hits[ ident ] = [ sequence[ target_start : target_end ] ]
                elif ident in hits:
                    hits.update( { ident : ( sequence[ target_start : target_end ], "Matched sequence of length: %s " % len( sequence[ target_start : target_end ]) + "on Target from %s " % target_start + "to %s " % target_end + "and Query from %s " % query_start + "to %s" % query_end ) } )
            
            # Diagnostic:    
            # print ident
            # print sequence[ target_start : target_end ]
            # print "Matched length: %s " % len( sequence[ target_start : target_end ] )
            # print "Target length: %s " % len( sequence )
            # print "Query lenfth: %s " % len(sequence2 )
            # if target_end == len( sequence ):
            #     print "The target reached the end of the sequence"
            # elif query_end == len( sequence2 ):
            #     print "The query reached the end of the sequence"
            # elif (target_end < len( sequence ) ) & (query_end < len( sequence2 ) ):
            #     print "Neither sequence reached its end"
            #     print "Next target: %s " % sequence[ int(target_end) + 1 ]
            #    print "Next query: %s " % sequence2[ int(query_end) + 1 ]
            #    print "\n"
            
for ident in sorted( hits, key = len, reverse = True ):                
    print ident, hits

# This does not print the output in a nice, line-by-line format.
# I will need to come back and change this at a later date, to prettify the output.
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            