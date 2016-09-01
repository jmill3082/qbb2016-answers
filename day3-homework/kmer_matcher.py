#!/usr/bin/env python

"""
Match kmers from a query fasta file to kmers in a target fasta file. Returns the identity of the sequence in which a match was found,
the kmer sequence that was matched, and the positions in the target sequence and query sequence, respectively.

usage: kmer-matcher.py <target.fa> <query.fa> <k>
"""

import sys
import fasta

k = int( sys.argv[3] )

for ident, sequence in fasta.FASTAReader( open(sys.argv[1]) ):
    sequence = sequence.upper()
    T_kmer_positions = {}
   
    for i in range( 0, len(sequence) - k ):
        kmer = sequence [i : i + k ]
        if kmer not in T_kmer_positions:
            T_kmer_positions[ kmer ] = [ i ]
        elif kmer in T_kmer_positions:
            T_kmer_positions[ kmer ].append( i )

        for ident2, sequence2 in fasta.FASTAReader( open(sys.argv[2]) ):
            sequence2 = sequence2.upper()
            for j in range( 0, len(sequence2) - k ):
                kmer = sequence2 [j : j + k ]
                if kmer in T_kmer_positions:              
                    print ident, "\t", kmer, "\t", "Position in target %s" % T_kmer_positions[ kmer ], "\t", "Position in query: %s" % j
