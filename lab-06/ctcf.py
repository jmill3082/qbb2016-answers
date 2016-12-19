#!/usr/bin/env python

"""
This script does something.

Usage:
    >./ctcf.py <input.heat>

"""

import sys
import h5py
import numpy as np

file = h5py.File( sys.argv[ 1 ] )
file.keys()
[u'0.counts', u'0.expected', u'0.positions', u'regions']

counts = file[ '0.counts' ][ ... ]
expected = file[ '0.expected' ][ ... ]
positions = file[ '0.positions' ][ ... ]
regions = file[ '0.regions' ][ ... ]

# Diagnostic:
# print counts
# print expected
# print positions
# print regions

# Used this to determine the shape of the arrays:
# print counts.shape
# print expected.shape
# print positions.shape
# print regions.shape

ratio = np.log( counts/expected )

# This is as much as I could understand... the data structure here is a complete mystery
# to me. I DID however go to Mike during the week we had the opportunity to do so. 



