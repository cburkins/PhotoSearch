#!/usr/bin/python2.7

import os
import sys
import cgi

ROOT = "/home3/cburkins/public_html/family/pictures/search/pyexifinfo/pyexifinfo"
sys.path.insert(0, ROOT)
import pyexifinfo as p


import json

filename = "/home3/cburkins/test.jpg"

if os.path.isfile(filename):
    print 'file exists: {0}'.format(filename) 
else:
    print "no such file"

data = p.get_xml(filename)
#print(data)


#data = p.get_json(filename)
# print( json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')) )





# ----------------------------------------------------- End ------------------------------------------

