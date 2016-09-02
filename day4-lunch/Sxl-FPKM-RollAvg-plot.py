#!/usr/bin/env python

"""
Plots the rolling average of FPKM for each chromosome in two separate ctab files. Requires setting the window size for the rolling average.

Usage: >./Sxl-FPKM-RollAvg-plot.py [ctab_file_1] [ctab_file_2] [window_size]

"""
# First, import all of the standard packages and modules needed to make the dream a reality.

from __future__ import division
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Let's stop the program from going any further if the user has not entered the correct number
# of arguments at the command line. 
if len( sys.argv ) != 4:
    print "You must designate TWO ctab files AND a window size!!!"
    quit()

# Now, we need to generate dataframes to work with from our command line entries, as well as 
# define the window size for future use.
df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )
window = int( sys.argv[3] )

# Now, I recognize that this is an inefficient way of approaching this problem, by attacking each
# of the chromosomes individually, and hard-coding them into the program. I would like to make this 
# the more general case, but since I already had the code, I decided just to copy/paste/modify, which
# took me very little time at all. Granted, this provides more opportunity for failure, since there
# are so many individual details to change - missing one could mess it up and make it harder to debug.

df_roi_2L = df[ "chr" ] == "2L"
df_chrom_2L = df[ df_roi_2L ]
smoothed_df_2L = df_chrom_2L[ "FPKM" ].rolling( window ).mean()

df2_roi_2L = df2[ "chr" ] == "2L"
df2_chrom_2L = df2[ df2_roi_2L ]
smoothed_df2_2L = df2_chrom_2L[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome 2L, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_2L, label="SRR072893" )
plt.plot( smoothed_df2_2L, label="SRR072915" )
plt.legend(loc="upper left")
plt.savefig( "smoothed_2L.png" )
plt.show()

# Repeat ad nauseum....
df_roi_2R = df[ "chr" ] == "2R"
df_chrom_2R = df[ df_roi_2R ]
smoothed_df_2R = df_chrom_2R[ "FPKM" ].rolling( window ).mean()

df2_roi_2R = df2[ "chr" ] == "2R"
df2_chrom_2R = df2[ df2_roi_2R ]
smoothed_df2_2R = df2_chrom_2R[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome 2R, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_2R, label="SRR072893" )
plt.plot( smoothed_df2_2R, label="SRR072915")
plt.legend( loc="upper left")
plt.savefig( "smoothed_2R.png" )
plt.show()

df_roi_3L = df[ "chr" ] == "3L"
df_chrom_3L = df[ df_roi_3L ]
smoothed_df_3L = df_chrom_3L[ "FPKM" ].rolling( window ).mean()

df2_roi_3L = df2[ "chr" ] == "3L"
df2_chrom_3L = df2[ df2_roi_3L ]
smoothed_df2_3L = df2_chrom_3L[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome 3L, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_3L, label="SRR072893" )
plt.plot( smoothed_df2_3L, label="SRR072915")
plt.legend( loc="upper left")
plt.savefig( "smoothed_3L.png" )
plt.show()

df_roi_3R = df[ "chr" ] == "3R"
df_chrom_3R = df[ df_roi_3R ]
smoothed_df_3R = df_chrom_3R[ "FPKM" ].rolling( window ).mean()

df2_roi_3R = df2[ "chr" ] == "3R"
df2_chrom_3R = df2[ df2_roi_3R ]
smoothed_df2_3R = df2_chrom_3R[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome 3R, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_2R, label="SRR072893" )
plt.plot( smoothed_df2_2R, label="SRR072915")
plt.legend( loc="upper left")
plt.savefig( "smoothed_3R.png" )
plt.show()

df_roi_4 = df[ "chr" ] == "4"
df_chrom_4 = df[ df_roi_4 ]
smoothed_df_4 = df_chrom_4[ "FPKM" ].rolling( window ).mean()

df2_roi_4 = df2[ "chr" ] == "4"
df2_chrom_4 = df2[ df2_roi_4 ]
smoothed_df2_4 = df2_chrom_4[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome 4, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_4, label="SRR072893" )
plt.plot( smoothed_df2_4, label="SRR072915" )
plt.legend( loc="upper right")
plt.savefig( "smoothed_4.png" )
plt.show()

df_roi_X = df[ "chr" ] == "X"
df_chrom_X = df[ df_roi_X ]
smoothed_df_X = df_chrom_X[ "FPKM" ].rolling( window ).mean()

df2_roi_X = df2[ "chr" ] == "X"
df2_chrom_X = df2[ df2_roi_X ]
smoothed_df2_X = df2_chrom_X[ "FPKM" ].rolling( window ).mean()

plt.figure()
plt.title( "Chromosome X, FPKM rolling mean (size=200)" )
plt.plot( smoothed_df_X, label="SRR072893" )
plt.plot( smoothed_df2_X, label="SRR072915" )
plt.legend( loc="upper right")
plt.savefig( "smoothed_X.png" )
plt.show()




