#!/usr/bin/python

import os
import sys
import cgi

ROOT = "/home3/cburkins/public_html/family/pictures/search/iptcinfo"
sys.path.insert(0, ROOT)
from iptcinfo import IPTCInfo
import sys

fn = (len(sys.argv) > 1 and [sys.argv[1]] or ['/home3/cburkins/test.jpg'])[0]

# Create new info object
info = IPTCInfo(fn)

# Check if file had IPTC data
if len(info.data) < 4: raise Exception(info.error)

# Print list of keywords, supplemental categories, contacts
print info.keywords
print info.supplementalCategories
print info.contacts

# ----------------------------------------------------- End ------------------------------------------

