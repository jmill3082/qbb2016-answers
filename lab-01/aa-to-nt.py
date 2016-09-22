#!/usr/bin/env python

'''
This script takes an amino acid sequence file in FASTA format and compares it to a nucleotide sequence file in
FASTA format. The order for corresponding amino acid and nucleotide sequences must be the same in both files.
For each corresponding pair of amino acid and nucleotide sequences, it compares the amino acid to the corresponding
codon. dS and dN are calculated for each position. Statistics are calculated and a plot is generated for the dN/dS 
at each position.

Usage:  >./aa-to-nt.py <input-aa.fa> <input-nt.fa>

'''

# We want to import the modules/packages we'll be needing for the rest of the code.

import sys
import fasta
import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Let's make a codon table! 

codon_table = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

# In the end, we're going to be plotting the dN/dS for each position, so let's initialize
# our dN and dS dictionaries now.

dN = {}
dS = {}

# Now, let's open the input files.

aa_file = open( sys.argv[ 1 ] )
nt_file = open( sys.argv[ 2 ] )

# Since itertools likes lists and doesn't seem to care for files, we need to initialize
# lists for the amino acid and nucleotide sequences.

aa_list = [ ]
nt_list = [ ]

# It turns out we'll be manipulating the nucleotide list to produce a new list with extended gaps.
# So we're going to need a new list to work with after that.

new_nt_list = [ ]

# We want to sequentially cut out our sequences from our input files and append them to the lists.

for ident, sequence in fasta.FASTAReader( aa_file ):
    aa_list.append( sequence )

    # Diagnostic:
    # print aa_list
    
for ident, sequence in fasta.FASTAReader( nt_file ):
    nt_list.append( sequence )

    # Diagnostic:
    # print nt_list

# Now we need to call izip to start the comparison.

for aa, nt in itertools.izip( aa_list, nt_list ):
    
    # Let's make a new nucleotide sequence, gapping it appropriately, according to the
    # gaps in the amino acid sequence.
    
    new_nt = []
    
    # We will be keeping track of our nucleotide position, so we need to initialize a position.
    i = 0
    
    for j in aa:
        if j == "-":
            new_nt.append( '---' )
        else:
            new_nt.append( nt[ i : i + 3 ] )
            i += 3
    
    # What we actually have up to this point is a list of sequences. We need to join that list
    # to make our reference sequence.
    
    new_nt_list.append( "".join( new_nt ) )
    
    # We need to go sequence by sequence now in our nucleotide sequence list and work with it.
    # The first sequence in the list is going to be our reference sequence, so...
    
ref = new_nt_list[ 0 ]
    
# Diagnostic:
# print ref
# print "reference sequence is %s bases" % len( ref )
# print "reference sequence contains %s codons" % float( ( len( ref) / 3 ) )
   
# Now we need to put keys into our dictionary corresponding to the base position, and we also
# Need to initialize those values to zero.
    
for k in range( 0, ( len( ref ) - 3 ), 3 ):
    n = k + 1
    dN[ n ] = int( 0 )
    dS[ n ] = int( 0 )

# Diagnostic:
# print dN
# print dS

# Finally we can work on comparing some sequences. We will go sequence by sequence in the
# new nucleotide list.

# Diagnostic:
# cod_match = 0
# cod_mismatch = 0
# ref_cod_fail = 0
# test_cod_fail = 0
    
for m, seq in enumerate( new_nt_list ):
        
    # We need to go ahead and skip the first sequence.
        
    if m == 0:
        continue

    # Diagnostic:
    # print m, seq
    
        
    # Okay, so I lied before. NOW we can finally do the comparisons.
    # Let's break up the sequences into codons...
        
    for pos in range(0, ( len( ref ) - 3 ), 3 ):
        ref_cod = ref[ pos : pos + 3 ]
        test_cod = seq[ pos : pos + 3 ]
        
        # Diagnostic:
        # print ref_cod
        # print test_cod
            
        # If the codons match, there is neither a synonymous nor a nonsynonymous change,
        # so we will want to skip to the next codon.
            
        if ref_cod == test_cod:
            
            # Diagnostic:
            # print "ref_cod == test_cod"
            # cod_match += 1
            # print "codon matches %s" % cod_match   
            
            continue
            
        # We are going to ignore ambiguous calls, since we aren't sure which base would
        # be correct for a particular ambiguous call. This also ignores gaps in the 
        # reference codon, which we want.
            
        if ref_cod not in codon_table:
            
            
            # Diagnostic:
            # print "reference codon not in codon table"
            # ref_cod_fail += 1
            # print "reference codon failures = %s" % ref_cod_fail
            
            continue
            
        elif test_cod not in codon_table:
            
            # Diagnostic:
            # print "reference codon not in codon table"
            # test_cod_fail += 1
            # print "test codon failures = %s" % test_cod_fail
            
            continue
            
        elif ref_cod != test_cod:    
            
            # If neither of the above conditions are true, then we need to determine whether
            # there is a change or if the test sequence is gapped.
            
            if codon_table[ ref_cod ] == codon_table[ test_cod ]:
                
                # Diagnostic
                # print "codon mismatch"
                # cod_mismatch += 1
                # print "there are %s codon mismatches" % cod_mismatch
                   
                # It might be true that the test goes past the reference, in which case it does not
                # matter, so we'll just move on
                    
                if pos + 1 not in dS:
                   continue
                        
                elif pos + 1 in dS:
                    dS[ pos + 1 ] += 1
            
                elif test_cod == '---':
                    
                    # We do the same check here for the key at a given position.
                    
                    if pos + 1 not in dN:
                       continue
                        
                    elif pos + 1 in dN:
                        dN[ pos + 1 ] += 1
            
            elif codon_table[ ref_cod ] != codon_table[ test_cod ]:
                
                # And again... 
                
                if pos + 1 not in dN:
                   continue
                    
                elif pos + 1 in dN:
                    dN[ pos + 1 ] += 1

# Diagnostic:
# print dN
# print dS

# Okay, now we need to initialize a list for our dN/dS values along the sequence.

dN_over_dS = []

# We also want to have the total dN and dS for the purpose of statistics, as well as a list of
# the difference of dN and dS at each position.

sum_dN = 0
sum_dS = 0
diff_dN_dS = []

# Let's make our ratios. If the denominator is zero, we have undefined - we don't like that. If the numerator is zero, 
# then the ratio is zero. So, let's make either case equal to zero. We'll also start with summing the dN and dS values 
# and filling our list of differences.

for key in dN:
    if dN[ key ] == 0:
        
        # Diagnostic:
        # print "dN = 0 for %s" % key
        
        dN_over_dS.append( 0 )
        diff_dN_dS.append( float( dN[ key ] - dS[ key ] ) )
        sum_dN += dN[ key ]
        sum_dS += dS[ key ]
    
    elif dS[ key ] == 0:
        
        # Diagnostic:
        # print "dS = 0 for %s" % key
        
        dN_over_dS.append( 0 )
        diff_dN_dS.append( float( dN[ key ] - dS[ key ] ) )
        sum_dN += dN[ key ]
        sum_dS += dS[ key ]
    
    # Here we will get the ratio, which we have to adjust since we'll be dealing with logs.
    
    else:    
        dN_over_dS.append( np.log( dN[ key ] + 1 ) / np.log( dS[ key ] + 1 )  )
        diff_dN_dS.append( float( dN[ key ] - dS[ key ] ) )
        sum_dN += dN[ key ]
        sum_dS += dS[ key ]

# Diagnostic:
# print dN_over_dS
# print diff_dN_dS
    
# We also want to use z score to determine whether a value is significantly different from the 
# mean.

z_diff_dN_dS = stats.zscore(diff_dN_dS)

# Diagnostic:
# print z_dN_over_dS
# print z_diff_dN_dS    

# Now, let's plot...

plt.figure()
for i, z in enumerate( z_diff_dN_dS ):
    if z < 3:
        plt.scatter( i, z, color="blue" )
    else:
        plt.scatter( i, z, color="red" )                
plt.title( "Significant Positive Selection Sites by Codon" )
plt.ylabel( "z-score of dN/dS" )
plt.xlabel( "Codon Position" )
plt.savefig( "dN_dS.png" )
plt.show()

# Finally, let's be a good coder and close the files we previously opened, since we are done.

aa_file.close()
nt_file.close()







































