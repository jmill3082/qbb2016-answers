#!/usr/bin/env python

"""
Makes an density plot of the FPKM values for a single ctab file, using gaussian kernel density estimation.
Usage:  > 04-density-plot.py <ctab_file>

"""

# First, let's import all of the important stuff for maths.
from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# A simple Google query produces several webpages referencing the scipy.stats gaussian_kde module.
from scipy.stats import gaussian_kde

# We need to read in our data from the ctab file.
df = pd.read_table( sys.argv[1] )

# Once we have the ctab file, we can select only the data from the dataframe that we will def need
# to generate the plot.
FPKM = df[ "FPKM" ].values

# Code for calculating the density and determining the linspace for the plot
density = gaussian_kde( FPKM )
xs = np.linspace( np.min( FPKM ), 100, 1000 )

# Now, using all of the regular matlibplot commands, we generate a nice plot - could use a little TLC
# like adjusting the title font size, etc.
plt.figure()
plt.plot( xs, density (xs) )
# Want to add a means of generalizing the title to include any sample name, rather than SRR072893...
plt.title( "FPKM for SRR072893" )
plt.xlabel( "FPKM" )
plt.ylabel( "Density" )
# Want to add a means of generalizing the filename to append the sample name after "Density"...
plt.savefig( "FPKM_Density.png" )
plt.show()
