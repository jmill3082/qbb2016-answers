#!/usr/bin/env python

"""
This script takes the eigenvec output file from plink2 after running PCA and
produces a scatter plot for the two principal components.

Usage:
    >pcaplot.py <input.eigenvec>

"""

# First, as always, let's import the packages that we'll need.
import sys
import matplotlib.pyplot as plt

# Now, we'll open our input eigenvec file.
f = open( sys.argv[1] )

# We'll initialize a couple of arrays for our eigenvectors.
eig1 = []
eig2 = []

# Let's now make sure that we have an appropriately delimited format for our plot.
for line in f.readlines():
    ffields = line.rstrip( "\r\n" ).split( " " )
    
    # Let's append our two arrays with the principal components.
    eig1.append( ffields[ 2 ] )
    eig2.append( ffields[ 3 ] )
    
# Diagnostic:
# print eig1
# print eig2

plt.figure()
plt.scatter( eig1, eig2, color = "blue" )
plt.xlabel( "eig1" )
plt.ylabel( "eig2" )
plt.title( " Principal Components" )
plt.savefig( "pcaplot.png" )
plt.show()
