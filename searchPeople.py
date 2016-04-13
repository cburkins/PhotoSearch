#!/usr/bin/python
import os
import sys
import json
import cgi

# Import a few variables from a file called FS_common.py in local directory (e.g. KM_Keyword_Cache)
from FS_common import *

# Import all functions from a file called search_keywords.py in local directory 
# There's only one function in there, and it's called "search_keywords"
from search_keywords import *

# Reads in the list of keywords, searches them, and spits out a JSON data structure for JavaScript
# This script is being called by the jQuery Autocomplete function.  Autocomplete expects that this
# script will parse for a field called "term", and then return a list in JSON format
#
# We are going to use the "term" value to filter a large list of keywords.  We are going to return
# a subset of the keywords which contain the "term" value

# TEST: You can test this script by calling it in a browser, and passing in a search term
# e.g. http://example.com/searchPeople.py?term=Bob

# ------------------------------------------------------------------------------------

# We were invoke via a GET request (e.g. http://example.com?term=Bob)
# We need to get the vvalue associated with "term"
theform = cgi.FieldStorage();
searchterm = theform.getvalue("term");

# Define the file that contains the full list of keywords
KEYWORD_FILE = KM_Keyword_Cache;

# Call an external python subroutine that will filter the list as follows
# Filter out a subset of keywords for certain category (e.g. people)
# Within that category, filter keywords that contain the searchterm (e.g. Bob)
# Return a simple python list containing matching keywords (e.g. ['Bob', 'Bobby'])
matching_keyword_list = search_keywords("people", searchterm, KEYWORD_FILE);

# Convert the simple python list to a JSON data structure
JSON_Matching_Keywords = json.JSONEncoder().encode(matching_keyword_list);

# Output the JSON data structure to stdout
print "Content-Type: text/json"
print
print JSON_Matching_Keywords;

# -------------------------------------- End -----------------------------------------
