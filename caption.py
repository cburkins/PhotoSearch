#!/usr/local/bin/python2.7

import os
import sys
import cgi

# Check for python v2.7 or better
if sys.version_info < (2, 7):
    print "\n   Must use python 2.7 or greater, exiting...\n"
    sys.exit()



ROOT = "/home3/cburkins/public_html/family/pictures/search/pyexifinfo/pyexifinfo"
sys.path.insert(0, ROOT)
import pyexifinfo as p


import json

filename = "/home3/cburkins/test.jpg"

if os.path.isfile(filename):
    print 'file exists: {0}'.format(filename) 
else:
    print "no such file"

#data = p.get_xml(filename)
#print(data)

# Extract all EXIF/XMP/IPTC from picture, seems to return a JSON structure as the first element of a list
datalist = p.get_json(filename)
# Get the first element of the list, which ends up being a JSON structure
jsonExif = datalist[0]

# Print out the entire JSON structure
#print( json.dumps(jsonExif, sort_keys=True, indent=4, separators=(',', ': ')) )


print (jsonExif['XMP:Description'])

# ----------------------------------------------------- End ------------------------------------------

