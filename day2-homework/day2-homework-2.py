#!/usr/bin/env python

"""
This program takes ctab file and replaces the FlyBase accession number with the UniProt accession number. 

Syntax:
day2-homework-2.py [ctab_file] [mapping_file] [options]
    -1  do not print ctab_file lines for which FlyBase accession numbers do not have a matching UniProt accession number.
    -2  print all lines of the ctab file, replacing the FlyBase accession numbers with the placeholder "---".

"""
import sys

if len(sys.argv) != 4:
    print "You must include a ctab_file a mapping_file AND an option."
    quit()
    
f = open( sys.argv[1] )
g = open( sys.argv[2] ) 
h = sys.argv[3]

replace = {}
for line in g.readlines():
    gfields = line.rstrip( "\r\n" ).split( "\t" )
    replace[gfields[0].strip()] = gfields[1] 
#   print replace    

for line in f.readlines():
    ffields = line.rstrip( "\r\n" ).split( "\t" )
    fb_val = ffields[8]    
    if fb_val in replace:
        ffields[8] = replace[fb_val]
        print "\t".join(ffields)
#       print fb_val
    else:
        if h == "-1":
            continue
        elif h == "-2":
            ffields[8] = "---"
            print "\t".join(ffields)
        
f.close()
g.close()
        
## mapping[fields[9]]