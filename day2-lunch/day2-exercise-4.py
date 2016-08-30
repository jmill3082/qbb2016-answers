#!/usr/bin/env python

import sys
f = open( sys.argv[1] )

count = 1

for line in f.readlines():
    fields = line.rstrip( "\r\n" ).split( "\t" )
    if line.startswith( "@" ):
        continue
    elif fields[2] == "*":
        continue
    else:
        if count <= 10:
            print fields[2]
            count += 1
        else:
            continue
            
f.close()
