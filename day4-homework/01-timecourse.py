#!/usr/bin/env python

"""
Generates a plot of transcript expression levels over a time course.

Usage: ./01-timecourse <metadata.csv> <ctab.dir> <metadata2.csv> <ctab2.dir>
   eg: ./01-timecourse samples.csv ~/data/results/stringtie replicates.csv ~/data/results/stringtie

"""

# First, import all of the important stuff. Granted, in this case, we will not
# necessarily use all of it...
from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Need to import out metadata file, which will be the source of the filename data.
df_meta = pd.read_csv( sys.argv[1] )

# Also need the path that points to the folder in which the data are contained.
ctab_dir = sys.argv[2]

# Initialize empty lists, into which we will append the given transcript expression
# data. Would like to add a means of generalizing to as many genes and samples as 
# are necessary for any arbitrary dataset.
fem_Sxl = []
mal_Sxl = []

# Add a string that will be used for the xticks on the timecourse plot.
# Would like to generalize this for any arbitrary timecourse data.
stages = ["10", "11", "12", "13", "14A", "14B", "14C", "14D" ]

# Need to manipulate our metadata files to generate dataframes that indicate which
# of the data files will be used for extracting FPKM values. This splits our whole dataset
# into sample populations.  Would like to generalize this to any arbitrary sample population 
# descriptions for any arbitrary dataset. In this case, we want to generate a dataframe that
# contains the subset of the metadata file which corresponds to each of the two populations
# being investigated: male and female.
df_roi = df_meta[ "sex" ] == "female"
df_roi2 = df_meta[ "sex" ] == "male"

# Diagnostic:
# print df_roi
# print df_roi2

# Now that we generated a dataframe that can split the metadata file into the two separate
# populations, we will extract the list of sample identifiers for each of the populations.
# Would like to generalize this as well, to allow for any arbitrary set of populations in
# a dataset.
females = df_meta[ df_roi ][ "sample" ]
males = df_meta[ df_roi2 ][ "sample" ]

# Diagnostic:
# print females
# print males

# For the first sample population, we now iterate over each item, using the sample 
# identifiers that we parsed out of the metadata file and the path that was provided
# at the command line to get the filenames corresponding to each of the files containing the 
# sample  data we will be using for the plot.
for sample_id in females:
    filename = ctab_dir + "/" + sample_id + "/t_data.ctab"
    
    # Now that we have the filename, we generate dataframes containing all of the sample data.
    df = pd.read_table( filename )
    
    # In this case, we are interested in a particular transcript, for which we know the specific
    # identifier. Would like to generalize this as well, so we can provide more than any arbitrary
    # set of transcript identifiers. From this (/these) identifier(s), we generate a new dataframe
    # that contains only those samples corresponding to the transcript we are interested in.
    df_roi3 = df[ "t_name" ] == "FBtr0331261"
    
    # We now extract the FPKM values from that dataframe and append them to our empty list.
    fem_Sxl.append( df[ df_roi3 ][ "FPKM" ].values )

# We now repeat the previous sequence of steps for another population of interest. Would like to
# Generalize this process, such that we can do this for any arbitrary number of populations.
for sample_id in males:
    filename = ctab_dir + "/" + sample_id + "/t_data.ctab"
    df = pd.read_table( filename )
    df_roi3 = df[ "t_name" ] == "FBtr0331261"
    mal_Sxl.append( df[ df_roi3 ][ "FPKM" ].values )

# In this case, we have some replicated data for a few particular time points. We want to include 
# those  data as well, so we have to now collect that data. Would like to improve this, so we can 
# manage adding any additional timecourse data that is incomplete.
df_meta_rep = pd.read_csv( sys.argv[3] )
ctab_rep_dir = sys.argv[4]

fem_Sxl_rep = []
mal_Sxl_rep = []
df_roi2_rep = df_meta_rep[ "sex" ] == "male"

# Diagnostic:
# print df_roi_rep
# print df_roi2_rep

fem_reps = df_meta_rep[ df_roi_rep ][ "sample" ]
mal_reps = df_meta_rep[ df_roi2_rep ][ "sample" ]

# Diagnostic:
# print fem_reps
# print mal_reps

for sample_id in fem_reps:
    filename = ctab_rep_dir + "/" + sample_id + "/t_data.ctab"
    df_rep = pd.read_table( filename )
    df_roi3_rep = df_rep[ "t_name" ] == "FBtr0331261"
    fem_Sxl_rep.append( df_rep[ df_roi3_rep ][ "FPKM" ].values)
    
for sample_id in mal_reps:
    filename = ctab_rep_dir + "/" + sample_id + "/t_data.ctab"
    df_rep = pd.read_table( filename )
    df_roi3_rep = df_rep[ "t_name" ] == "FBtr0331261"
    mal_Sxl_rep.append( df_rep[ df_roi3_rep ][ "FPKM" ].values)

# Finally, we can plot the data that we collected.
plt.figure()
plt.title("Sxl expression across embryonic development")
plt.plot( fem_Sxl, 'r', label="female" )
plt.plot( mal_Sxl, 'b', label="male" )
# Include the replicates. Since we only have replicates for the last four time points in the 
# timecourse, we need to specify where our data will go.
plt.plot( [4, 5, 6, 7], fem_Sxl_rep, 'ro')
plt.plot( [4, 5, 6, 7], mal_Sxl_rep, 'bo')
plt.legend( loc="upper left" )
plt.xticks(range(8), stages, rotation="vertical")
plt.savefig( "timecourse.png" )
plt.xlabel( "developmental stage" )
plt.ylabel( "mRNA abundance (FPKM)" )
plt.show()



