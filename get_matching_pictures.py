
import sys
from dictionary_list_push import *
from get_keyword_dictionary import *


# ----------------------------------------------------------------------

def get_matching_pictures(search_list, keyword_dictionary):

	# search_list         = list of keywords to look for in metadata
	# keyword_dictionary  = data dictionary, one entry for each picture, lists all keywords

	matching_filenames = []	
	
	# Look for people keywords
	for filename in list(keyword_dictionary.keys()):
		if set([x.lower() for x in search_list]).issubset(set([x.lower() for x in keyword_dictionary[filename]])):
			matching_filenames.append(filename)

	return matching_filenames
	
# --------------------------------------------------------------------------
def get_matching_pictures_category (category, search_dictionary, pictures_dictionary):

	# At the moment, the search dictionary has several lists for each picture, with the following keys
	#    People : list of all the requested people
	#    Locations : list of all the requested places
	#    Events : list of all the requested events
	#    Ratings : list of all the requested events
	

	# The keyword dictionary has several lists for each picture, with keys as follows
	#    P : List of people in that picture
	#    L : List of locations in that picture
	#    E : List of events in that picture
	#    Y : List of years in that picture
	#    R : List of ratings in that picture
	#    A : List of artists for that picture
	
	
	# This will eventually hold a list of all filenames that match up against the search dictionary
	matching_filenames = [];
			
	matching_keyword_dictionary = {};
	
	# Make sure that the search dictionary actually contains the requested category, if not, we just exit
	if (category in search_dictionary):

		search_list = search_dictionary[category];

		# Look through each search term
		for search_term in search_list:
		
			matching_keyword_dictionary = {}
	
			# Loop through each filename
			for filename in list(pictures_dictionary.keys()):

				# Get dictionary for just this one picture
				filename_dictionary = pictures_dictionary[filename]
				
				# Zero out the keywords list
				keywords = [];
				
				# Flatten out the dictionary.  We're looking through each possible part of
				# dictionary (P, L, E, Y), and putting all keywords into one list
				if ((category == "People") and ('P' in filename_dictionary)):
					keywords.extend(filename_dictionary['P'])
				if ((category == "Locations") and ('L' in filename_dictionary)):
					keywords.extend(filename_dictionary['L'])
				if ((category == "Events") and('E' in filename_dictionary)):
					keywords.extend(filename_dictionary['E'])					
				if ((category == "Years") and('Y' in filename_dictionary)):
					keywords.extend(filename_dictionary['Y'])					
				if ((category == "Ratings") and('R' in filename_dictionary)):
					keywords.extend(filename_dictionary['R'])					
				if ((category == "Artists") and('A' in filename_dictionary)):
					keywords.extend(filename_dictionary['A'])					


				# Make sure there is at least one keyword
				if (len(keywords) >0):
				
					# Loop through all the keywords for this picture
					for keyword in keywords:			

						# One at a time, compare each keyword (for this picture) against our search term
						if (keyword.lower().rfind(search_term.lower()) >= 0):
							matching_keyword_dictionary[filename] = filename_dictionary


			# OK, done with looping through filenames, so save off the resulting (smaller) dictionary of pictures
			pictures_dictionary = matching_keyword_dictionary
		
	# Now return the dictionary for the pictures that matched up
	return pictures_dictionary


# --------------------------------------------------------------------------

def get_matching_pictures_advanced (search_dictionary, pictures_dictionary):


	pictures_dictionary = get_matching_pictures_category ("People", search_dictionary, pictures_dictionary)

	pictures_dictionary = get_matching_pictures_category ("Events", search_dictionary, pictures_dictionary)

	pictures_dictionary = get_matching_pictures_category ("Locations", search_dictionary, pictures_dictionary)

	pictures_dictionary = get_matching_pictures_category ("Artists", search_dictionary, pictures_dictionary)

	
	# Handling a range of ratings is tricky.  We need to make a separate call for each rating, and add them up
	category="Ratings";
	if (category in search_dictionary):
		search_list = search_dictionary[category];
		desired_rating = search_list[0];
		sys.stderr.write(desired_rating + "\n");
		if (len(desired_rating) == 3):
			# We're dealing with a range of ratings (e.g. 3-5, see, it's got 3 characters in the string)
			first_rating = desired_rating[0:1]
			last_rating = desired_rating[2:3]
			sys.stderr.write("First rating = " + first_rating + "\n");
			sys.stderr.write("Last rating = " + last_rating + "\n");
			temp_dict = {};
			for rating in range(int(first_rating), int(last_rating) + 1):
				sys.stderr.write(str(rating) + "\n")
				search_dictionary[category] = [str(rating)];
				
				# Call search for just this one rating, but then concatenate these results to all the other results using update method of dictionary
				temp_dict.update(get_matching_pictures_category ("Ratings", search_dictionary, pictures_dictionary));

			pictures_dictionary = temp_dict;
		else:
			# Desired rating is only a single rating
			pictures_dictionary = get_matching_pictures_category ("Ratings", search_dictionary, pictures_dictionary)
	
	
	
	
	# Handling a range of years is tricky.  We need to make a separate call for each year, and add them up
	category="Years";
	if (category in search_dictionary):
		search_list = search_dictionary[category];
		desired_year = search_list[0];
		sys.stderr.write(desired_year + "\n");
		if (len(desired_year) == 9):
			# We're dealing with a range of years (e.g. 1970-1978, see, it's got 9 characters in the string)
			first_year = desired_year[0:4]
			last_year = desired_year[5:9]
			sys.stderr.write("First year = " + first_year + "\n");
			sys.stderr.write("Last year = " + last_year + "\n");
			temp_dict = {};
			for year in range(int(first_year), int(last_year) + 1):
				sys.stderr.write(str(year) + "\n")
				search_dictionary[category] = [str(year)];
				
				# Call search for just this one year, but then concatenate these results to all the other results using update method of dictionary
				temp_dict.update(get_matching_pictures_category ("Years", search_dictionary, pictures_dictionary));

			pictures_dictionary = temp_dict;
		else:
			# Desired year is only a single year
			pictures_dictionary = get_matching_pictures_category ("Years", search_dictionary, pictures_dictionary)

	
			
	# We only need to return the list of pictures which match up, so extract that from the dictionary
	matching_filenames = pictures_dictionary.keys();
	
	# If the year is missing from the picture, set it as 9999
	for key,value in pictures_dictionary.items():
		if not('Y' in value):
			value['Y'] = ['9999'];

	# Extract a simple list of filenames and associated year
	filename_year_hash = {};
	for key,value in pictures_dictionary.items():
		filename_year_hash[key] = value['Y'][0];
	
	# Sort the list of filenames (key) by year (value)
	matching_filenames = sorted(filename_year_hash, key=filename_year_hash.get);	
	
	return matching_filenames

# --------------------------------------------------------------------------	
# --------------------------------------------------------------------------	
# --------------------------------------------------------------------------	
