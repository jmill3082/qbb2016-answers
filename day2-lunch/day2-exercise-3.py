#!/usr/bin/env python

import sys
f = open( sys.argv[1] )

count = 0

for line in f.readlines():
    if "NH:i:1" in line:
        count += 1
    else:
        continue

print count
   
f.close()
