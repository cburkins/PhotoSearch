#!/usr/bin/python
import sys
import sys
import cgi

from FS_common import *
from dictionary_list_push import *
from get_matching_pictures import *
from get_keyword_dictionary import *

print "Content-Type: text/plain"
print ""

theform = cgi.FieldStorage()
search_dictionary = {}

# Careful, if there's only one term, it's a string, if more than one, it's a list.  Need a list for next code section
keyword_item = theform.getvalue("Keyword");
if (isinstance(keyword_item, str)):
	keyword_list = [keyword_item]
else:
	keyword_list = keyword_item;

	
	
for keyword in keyword_list:
	
	if (keyword.startswith("L:")):

		# Strip off the L: at beginning of keyword
		keyword = keyword[2:]
		
		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'Locations', search_dictionary)

	elif (keyword.startswith("E:")):

		# Strip off the E: at beginning of keyword
		keyword = keyword[2:]

		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'Events', search_dictionary)

	elif (keyword.startswith("Y:")):

		# Strip off the Y: at beginning of keyword
		keyword = keyword[2:]

		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'Years', search_dictionary)

	elif (keyword.startswith("R:")):

		# Strip off the R: at beginning of keyword
		keyword = keyword[2:]

		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'Ratings', search_dictionary)

	elif (keyword.startswith("A:")):

		# Strip off the A: at beginning of keyword
		keyword = keyword[2:]

		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'Artists', search_dictionary)


	else:
		search_dictionary = dictionary_list_push(keyword, 'People', search_dictionary)


# Get a copy of the keyword dictionary from disk
keyword_dictionary = get_keyword_dictionary(Image_Metadata)

matching_count = len(get_matching_pictures_advanced(search_dictionary, keyword_dictionary))

print matching_count
