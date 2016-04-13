#!/usr/bin/python
import os
import sys
import json
import cgi

# Import my local code
from FS_common import *
from search_keywords import *

# Reads in the list of keywords, searches them, and spits out a JSON data structure for JavaScript

# ------------------------------------------------------------------------------------

theform = cgi.FieldStorage();
searchterm = theform.getvalue("term");

KEYWORD_FILE = KM_Keyword_Cache;

matching_keyword_list = search_keywords("places", searchterm, KEYWORD_FILE);

JSON_Matching_Keywords = json.JSONEncoder().encode(matching_keyword_list);

print "Content-Type: text/json"
print
print JSON_Matching_Keywords;

# -------------------------------------- End -----------------------------------------
