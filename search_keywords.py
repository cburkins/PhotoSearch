#!/usr/bin/python
import sys
import time

# ------------------------------------------------------------------------------------

# Args
#   type (string) : people, events, or places
#   search_term (string) : search term that we're looking for in the keywords
#   keyword_file (string) : filename on the web server where can find find a list of keywords
#
# Limit our search to sub-category of keywords based on "type" argument.  Within that subset,
# return a list of all keywords that contain the search term somewhere within the keyword.  
# The search is case-insenstive


def search_keywords(type, search_term, keyword_file):

	PlacesList = [];
	EventsList = [];
	PeopleList = [];
	ArtistsList = [];
	matching_keywords = [];
		
	f=open(keyword_file, 'r');
	for keyword in f:
		keyword = keyword.rstrip();
		if (keyword.startswith("L:")):
			PlacesList.append(keyword);
		elif (keyword.startswith("E:")):
			EventsList.append(keyword);
		elif (keyword.startswith("A:")):
			ArtistsList.append(keyword);
		else:
			PeopleList.append(keyword);
	f.close();
	
	if (type == "people"):
		all_keywords = PeopleList
	elif (type == "events"):
		all_keywords = EventsList
	elif (type == "places"):
		all_keywords = PlacesList
	elif (type == "artists"):
		all_keywords = ArtistsList;
		all_keywords = ['A:Chad Burkins', 'A:Jim Heimbecker', 'A:Tom Burkins', 'A:Art Powl', 'A:Meghan Burkins'];

	
	for keyword in all_keywords:
		sys.stderr.write('Keyword = ' + keyword + '\n');
		if (keyword.lower().find(search_term.lower()) > -1):
			matching_keywords.append(keyword)
			
	sys.stderr.write('\n');
	return matching_keywords
	
# -------------------------------------- End -----------------------------------------
