#!/usr/bin/env python

"""
This script produces Manhattan plots for each qassoc file output from Plink2.

Usage:
    >./manhattan.py <input.qassoc>

"""

# As usual, we'll begin by importing packages we'll want to use.
import sys
import matplotlib.pyplot as plt
import numpy as np

# Then, we'll open our input file, so we can start working with it.
# In this case, we're opening multiple files, which we will indicate using a 
# wildcard at the command prompt. So, we want to make sure our code will 
# accomodate that. Our sys.argv must be written for an array.
for f in sys.argv[1:]:

# We're going to retain the title of the input file for our output, so
# let's strip that bit of info out of the filename. Only the extension will change.
    title = f.split(".")[1]

# Now, we need to initialize some arrays, which we'll be working with.
    x = []
    y = []

    x2 = []
    y2 = []

# We want to read the input file, line-by-line.
    for i, line in enumerate(open(f)):
        if i == 0:
            continue
            
        # Let's make sure our data are delimited appropriately.
        fields = line.rstrip("\r\n").split()
        
        # We are going to get separate the data. We want to separate based on p-value
        # so we can color code our plot.
        if float(fields[-1]) < 0.00001:
            x2.append(i)
            y2.append(- np.log10(float(fields[-1])) )
        else:
            x.append(i)
            y.append(- np.log10(float(fields[-1])) )

    # Now that we have our two arrays, let's make the plots.
    plt.figure()
    plt.plot( x, y, "b." )
    plt.plot( x2, y2, "r." )
    plt.title( "Manhattan Plot for %s" % title ) 
    plt.xlabel( "Position" )
    plt.ylabel( "log10(P)" )
    plt.savefig( "Manhattan_%s.png" % title )
    plt.show()
