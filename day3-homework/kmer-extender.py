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

# Now that we have our query dictionary, let's work with the target sequences one at a time.
for ident, sequence in fasta.FASTAReader( open(sys.argv[1]) ):
    
    # In case the sequence has any differences in case, which could cause problems in string matching, 
    # make all sequence upper case.
    sequence = sequence.upper()

    # We want to get ALL of the possible matches, so we will do an exhaustive search at EVERY nucleotide.
    for i in range( 0, len(sequence) - k ):
        kmer = sequence [i : i + k ]
        
        # Now what we want to do is check the query dictionary to see if the kmer from the target exists.
        # If not, we will continue on down the line. If so, then we need to perform the extension matching.
        if kmer not in Q_kmer_positions:
            continue
        elif kmer in Q_kmer_positions:
            
            # Diagnostic:
            # print kmer, Q_kmer_positions[ kmer ]
            
            for kmer, value in Q_kmer_positions.iteritems():
            
                # Diagnostic:
                print kmer, i, j
                # Let's start at the first nucleotide in the kmer match and start moving to the left.
                # while (2 + 2 == 4):
                


''''            
   
          
            
            
                # RIGHT EXTENSION
                # We check to see if the query sequence is in the target sequence dictionary.
                # We will modify both the target and the query sequences, and keep checking to see if they match.
                # As long as they match, we want to repeat this process.
                if Q_kmer in T_kmer_positions:
                    
                    # If the query is in the target dictionary, we add one to the length of the kmer and get the new (k+1)mer sequence 
                    k = k + 1
                    Q_kmer = sequence2[ j : j + k ]
                     
                    # Now we check the new (k+1)mer against the target sequence. If the (k+1)mer is found in the target,
                    # then we need to add a new entry in the dictionary.
                    for i in range( 0, len(sequence) - k):
                        
                        # Here we will add new entries to the dictionary for the new (k+1)mers, so we can match the new query sequence
                        # to the positions of the matching sequence in the target.
                        if Q_kmer in sequence:                            
                            for i in range( 0, len(sequence) - k ):
                                T_kmer = sequence [i : i + k ]
                                    
                                # If the new (k+1)mer is not already in the dictionary, then we need to add the key and put the position
                                # into the dictionary. If it is already in the dictionary, then we need to append the dictionary with
                                # the new position of the (k+1)mer.
                                if T_kmer not in T_kmer_positions:
                                    T_kmer_positions[ T_kmer ] = [ i ]
                                elif T_kmer in T_kmer_positions:
                                    T_kmer_positions[ T_kmer ].append( i )
                            break            
                                    
                    # Diagnostic 
                    print T_kmer,
                    print "in sequence %s." % ident, 
                    print "Position(s) in target: %s." % T_kmer_positions[ T_kmer ],
                    print "Position in query: %s." % j
                        
                # Now that we have exited the loop and identified the next base to the right that does not match,
                # clip the unmatched query base from the query sequence before proceeding to the left extension    
                # k = k - 1
                # Q_kmer = sequence2[ j : j + k ]
                # T_kmer = Q_kmer
                
                # Diagnostic
                # print ident, 
                # print T_kmer, 
                # print "Position(s) in target %s" % T_kmer_positions[ T_kmer ],
                # print "Position in query: %s" % j
                
             
                # Left extension    
                    while Q_kmer in T_kmer_positions:
                        i = i - 1       
                        T_kmer = sequence[ i : i + k ]
                        T_kmer_positions[ T_kmer ].append( i )
                        j = j - 1
                        Q_kmer = sequence2[ j : j + k]
                
                # Clip the unmatched base
                    j = j + 1
                    i = i + 1
                    T_kmer = sequence[ i : i + k ]
                
                    
                    print ident, 
                    print T_kmer, 
                    print "Position(s) in target %s" % T_kmer_positions[ T_kmer ],
                    print "Position in query: %s" % j
'''