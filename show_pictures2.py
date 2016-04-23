#!/usr/bin/python

# ------------------------------------------------------------------------
# Basic Description : This module gets called with a list of keywords,
# and will use a JQuery applet to show them.  
#
#
# NOTE: If you're updating paths, also look in
#   - FS_common.py
#   - index.html
#   - show_pictures.py
#  
# 
# Entry point
# - This standalone python code, and is called from index.html (via the submit button)
#
# Input Parameters : 
# - picsize : String that should be "Large", "Medium", or "Small". Indicates the desired size of pictures
# - Keyword : If only one keyword, then it's a string.  If more than one keyword, it's a list. (e.g. Chad Burkins, Meghan Burkins, L:Gralan Drive)
 
# Action : 
# - Parse the desired keywords
# - Find all matching pictures
# - Display them with a JQuery applet called Cycle
#
# Output : 
# - Produces an HTML file which calls the jQuery Cycle2 plugin
# - Pretty sure there's a separate line for each photo, need to verify that
#
# Dependencies :
# - JQuery library : http://www.burkins.com/family/pictures/search/jquery-1.10.2.min.js
# - JQuery applet Cycle : http://www.burkins.com/family/pictures/search/jquery.cycle.all.3.03.js
# - variable:Image_Metadata defined in FS_common.py (file location of Image Metadata library)
# - file:get_keyword_dictionary.py defines subroutine get_keyword_dictionary()
# - file:get_matching_pictures.py defines subroutine get_matching_pictures_advanced()
#
# Subroutins :
# - get_dimensions : Given a jpg filename, opens it, and gets the x,y dimensions
# - scale_dimensions : Given x,y and max x,y, create a new x,y (to scale) that fits inside max x,y
# - 
#
# To Do
# - Buttons to skip forward 10 pictures
#
# ------------------------------------------------------------------------

print "Content-Type: text/html"
print

import os
import sys
import cgi

ROOT = "/home3/cburkins/public_html/family/search"
sys.path.insert(0, ROOT)

# Import my local code
from FS_common import *
from get_matching_pictures import *


# ------------------------------------------------------------------------

fileList = []
search_list = []

# ---------------------------------------------------------------------------------------------------
# -------------------------------------- Main  ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

theform = cgi.FieldStorage()

params = []
search_list = []


# Using hidden value passed via form, build a search dictionary (used later)
# Keywords (People, Places, Events) are in one big list associated with the key "Keyword"
# Parse through that list, and create seperate lists in a dictionary called "search_dictionary"
# Careful, if there's only one term, it's a string, if more than one, it's a list.  
# Need a list for next section of code, so if needed, convert single item to a list
keyword_item = theform.getvalue("Keyword");
if (isinstance(keyword_item, str)):
	keyword_list = [keyword_item]
else:
	keyword_list = keyword_item;
	

# Clear the search dictionary	
search_dictionary = {}

# Construct the search_dictionary (contains the keywords that we're searching for)
# L = Location
# E = Event
# Y = Year
# R = Rating
# A = Artist
# Everything else is a person
	
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


# Get the dictionary of all keywords in my pictures (this is a big dictionary)
# This does NOT query each image, it just parses the static Image_Metadata file (which has one line per picture)
# Pathname of each pic is the local path on my Linux machine at home (e.g. /mnt/ChadDocs/My Webs/www.burkins.com/)
keyword_dictionary = get_keyword_dictionary(Image_Metadata)
	
# Slim down list of pictures to those that have all matching keywords (that were given in search form by users)
matching_filenames = get_matching_pictures_advanced(search_dictionary, keyword_dictionary)

# At this point, matching_filenames is a simple list of full-path filenames
# Pathname is still relative to my home Linux machine (e.g. /mnt/ChadDocs/My Webs/www.burkins.com/)
	
# OK, now ready to start construction the HTML page
	
# ---------------------------------
# --------- Start of form ---------
# ---------------------------------

# Create the HTML header, get Font Awesome, get the local external CSS style sheet	
print """
<html>
<head>
<title>Family Search</title>
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="show_pictures2.css">
</head>
"""

# CSS Setup, include jQuery library and Cycle plugin
print """
<body>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
<script src="http://malsup.github.io/jquery.cycle2.js"></script>
<script src="http://malsup.github.io/jquery.cycle2.center.js"></script>
"""

print """
<div class="cycle-slideshow"
     data-cycle-fx="scrollHorz"
     data-cycle-timeout="0"
     data-cycle-prev="#prev"
     data-cycle-next="#next"
     data-cycle-center-horz="true"
     data-cycle-center-vert="true"
     data-cycle-caption-template="Slide {{slideNum}} of {{slideCount}}"
     >

  <!-- empty element for caption, CSS will place in top-right of picture -->
  <div class="cycle-caption"></div>

  <!-- empty elemen for overlay, CSS will place at bottom of picture -->
  <div class="cycle-overlay"></div>
"""

# Loop through matching images, and contrsuct HTML to support the Cycle jQuery tool
# Pathname on the home linux machine (e.g. /mnt/ChadDocs)
for imageHomeFile in matching_filenames:
        
        # Pathname on the web server (e.g. http://www.burkins.com)
        imageWebURL = imageHomeFile.replace(SRC_PATH, DST_URL)

        # keyword dictionary
        #      key : filename
        #      value : dictionary
        #         key : cateogry (P=ListOfPeople, L=ListofLocations, Y=ListofYears, R=ListOfRatings)
        #         value : list matching the category                                          

        # Find the Year in the picture metadata
        if "Y" in keyword_dictionary[imageHomeFile]:
                year = str(((keyword_dictionary[imageHomeFile])["Y"])[0])
        else:
                year = 'Unknown'
                
        # Find the people in the picture metadata
        if "P" in keyword_dictionary[imageHomeFile]:
                peopleList = (keyword_dictionary[imageHomeFile])["P"]
                # Remove the flag element **PIK***
                if '**PIK**' in peopleList: peopleList.remove('**PIK**')
                # Convert the list of People into a comma-separated string
                people = ", ".join(peopleList)
        else:
                people = 'Unknown'

        # Find the locations in the picture metadata
        if "L" in keyword_dictionary[imageHomeFile]:
                locationList = (keyword_dictionary[imageHomeFile])["L"]
                 # Convert the list of Locations into a comma-separated string
                locations = ", ".join(locationList)
        else:
                locations = 'Unknown'

        # Find the events in the picture metadata
        if "E" in keyword_dictionary[imageHomeFile]:
                eventList = (keyword_dictionary[imageHomeFile])["E"]
                 # Convert the list of Events into a comma-separated string
                events = ", ".join(eventList)
        else:
                events = 'Unknown'

        # Create a caption-line for each element, insert a span tag for CSS formatting
        captionYear = '<span class=caption-category>Year:</span> {0}'.format(year)
        captionPeople = '<span class=caption-category>People:</span> {0}'.format(people)
        captionLocations = '<span class=caption-category>Location:</span> {0}'.format(locations)
        captionEvents = '<span class=caption-category>Event:</span> {0}'.format(events)
        
        # Create the full multi-line title to be displayed in the overlay at the bottom of the picture
        # Use a single span so we can apply CSS, and insert line breaks
        title = '<span class=caption>{0}<BR>{1}<BR>{2}<BR>{3}</span>'.format(captionYear, captionPeople, captionLocations, captionEvents)
    
        # Insert the complete HTML img tag for this picture into the slideshow <div>
        print '<img src="{0}", data-cycle-desc="{1}">'.format(imageWebURL, title)

        # Example      <img src="http://malsup.github.io/images/p1.jpg">
        # Complex Ex:  <img src="http://malsup.github.io/images/p1.jpg" data-cycle-desc="<span class=caption-category>People:</span> Bob Burkins, Chad Burkins, Tom Burkins<br><span class=caption-category>Location:</span> Walt Disney World<br>" >


# End of slideshow <div>
print """
</div>
"""

# Enable the right-arrow and left-arrow keys to operate Next and Prev for the slideshow
print """
<script type="text/javascript">
  $(document.documentElement).keyup(function (e) {
     if (e.keyCode == 39) { $('.cycle-slideshow').cycle('next'); }
     if (e.keyCode == 37) { $('.cycle-slideshow').cycle('prev'); }
  });
</script>
"""

# end of body and html
print """
</body>
</html>
"""

# ----------------------------------------------------- End ------------------------------------------

