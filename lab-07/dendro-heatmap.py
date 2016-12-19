#!/usr/bin/env python
import sys
import scipy.cluster.hierarchy as hac
import numpy as np
import pandas as pd
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
import pylab
import scipy
import pydendroheatmap as pdh
try: import cPickle as pickle
except: import pickle


f = open( sys.argv[ 1 ] )
colHeaders = f.next().strip().split()[ 1: ]
rowHeaders = []
dataMatrix = []

for line in f:
    data = line.strip().split( '\t' )
    rowHeaders.append( data[ 0 ] )
    dataMatrix.append( [ float( x ) for x in data[ 1: ] ] )
dataMatrix = np.array( dataMatrix )

linkageMatrix_cellType = hac.linkage( dataMatrix )
linkageMatrix_gene = hac.linkage( np.transpose( dataMatrix ) )

heatmapOrder = hac.leaves_list( linkageMatrix_cellType )
orderedDataMatrix = dataMatrix[ heatmapOrder, : ]
rowHeaders = np.array( rowHeaders )
orderedRowHeaders = rowHeaders[ heatmapOrder, ]

heatmap_array = orderedDataMatrix
cellType_dendrogram = linkageMatrix_gene
gene_dendrogram = linkageMatrix_cellType
heatmap = pdh.DendroHeatMap( heat_map_data = heatmap_array, left_dendrogram = gene_dendrogram, top_dendrogram = cellType_dendrogram)
heatmap.title = 'Gene Expression by Cell Type'
heatmap.xlabel = 'Cell Type'
heatmap.ylabel = 'Gene'
heatmap.show()
heatmap.colormap = heatmap.yellowBlackBlue
heatmap.export( 'dendro-heatmap.png' )