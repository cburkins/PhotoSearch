#!/usr/bin/python

import os
import sys
import cgi

ROOT = "/home3/cburkins/public_html/family/pictures/search/pyexifinfo/pyexifinfo"
sys.path.insert(0, ROOT)
import pyexifinfo as p


import json

filename = "/home3/cburkins/test.jpg"

data = p.get_json(filename)
# print( json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')) )





# ----------------------------------------------------- End ------------------------------------------

