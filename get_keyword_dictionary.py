
from dictionary_list_push import *

# --------------------------------------------------------------------------

def get_keyword_dictionary(Image_Metadata):

	# old keyword dictionary
	#     key : filename
	#     value : list of keywords
	#
	# new keyword dictionary
	#      key : filename
	#      value : dictionary
	#         key : cateogry (P=ListOfPeople, L=ListofLocations, Y=ListofYears, R=ListOfRatings)
	#         value : list matching the category

	keyword_dictionary = {}

	f = open(Image_Metadata, 'r') 

	# Sort through the Image_Metadata file, there's one line for each file
	for line in f:

		# Strip off carrage return and/or newline
		line = line.rstrip('\r\n')
	
		# Split the line on ':::' and return 1st item
		filename = line.partition(':::')[0]

		# Split the line on ':::' and return 2nd item (the values)
		tags = line.partition(':::')[2]

		# Double-check for empty list
		if (len(tags) == 0):
			tag_list = []
		else:
			tag_list = tags.split(',,,')

		picture_keyword_dictionary = {}
		for keyword in tag_list:
			
			# Category can be P, L, E, Y, R (People, Location, Event, Year, Rating)
			category = keyword[0:1]
			value = keyword[2:]
			dictionary_list_push(value, category, picture_keyword_dictionary)
			
		keyword_dictionary[filename] = picture_keyword_dictionary
	
	f.close()
	
	return keyword_dictionary

# ----------------------------------------------------------------------
