#!/usr/bin/env python

"""
Makes a histogram of log(FPKM) values from a ctab file.
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Try plt.style,use('538')
# Try plt.style.use('ggplot')
# Look up matplotlib galleries for more inspiration

df = pd.read_table( sys.argv[1] )
df_roi = df[ "FPKM" ] > 0
df_hist = df[ df_roi ][ "FPKM" ]

# Diagnostic
# print type(df_roi)
# print df_roi
# print type(df_hist)
# print df_hist

hist_values = np.log10(df_hist)

# Diagnostic
# print hist_values

# Determining the min and max values in the array for binning purposes
# print min(hist_values)
# print max(hist_values)

plt.figure()
plt.hist(hist_values, range = [-4, 4], bins = 50)
plt.savefig( "FPKM-hist.png" )
plt.title( "Frequency of log(FPKM)" )
plt.xlabel( "log(FPKM)" )
plt.ylabel( "occurrences of log(FPKM)" )
plt.show()

