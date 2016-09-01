#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

df_roi = (df[ "gene_name" ] == "Sxl") & (df[ "FPKM" ] > 0) 
df_Sxl_exp = df[ df_roi ]
df_FPKM_log = np.log(df_Sxl_exp[ "FPKM" ] )

df2_roi = (df[ "gene_name" ] == "Sxl" ) & (df[ "FPKM" ] > 0)
df2_Sxl_exp = df2[ df2_roi ]
df2_FPKM_log = np.log(df2_Sxl_exp[ "FPKM" ] )

plt.figure()
plt.plot( df_FPKM_log )
plt.plot( df2_FPKM_log )
plt.title( "log(FPKM) of Sxl in SRR072893 and SRR072915" )
plt.legend(loc = 'upper left')
plt.savefig( "Sxl_expression.png" )
plt.show()