#!/usr/bin/env python

import sys
f = open( sys.argv[1] )

mapsum = 0
lines = 0

for line in f.readlines():
    fields = line.rstrip( "\r\n" ).split( "\t" )
    if line.startswith( "@" ):
        continue
    elif fields[2] == "*":
        continue
    else:
        mapsum = mapsum + int(fields[4])
        lines += 1

mapavg = mapsum/lines

print "Average MAPQ Score = %d" % mapavg
            
f.close()
