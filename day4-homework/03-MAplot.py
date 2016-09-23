#!/usr/bin/env python

"""
Makes an MA plot from two ctab files.
Usage:  > 03-MAplot.py <ctab_file-1> <ctab_file-2> 
"""
from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

FPKM1 = df[ "FPKM" ].values
FPKM2 = df2[ "FPKM" ].values

FPKMX = np.log2(FPKM1 + 1)
FPKMY = np.log2(FPKM2 + 1)

# Diagnostic:
# print FPKM1
# print type(FPKM1)
# print FPKM2
# print type(FPKM2)

M = (FPKMX - FPKMY)
A = (1/2)*(FPKMX + FPKMY)

# Diagnostic
# print M
# print type(M)
# print A
# print type(A)

plt.figure()
plt.scatter( A, M, alpha=0.1 )
plt.title( "MA Plot" )
plt.ylabel( "M" )
plt.xlabel( "A" )
plt.savefig( "MA-plot.png" )
plt.show()