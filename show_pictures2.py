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
keyword_dictionary = get_keyword_dictionary(Image_Metadata)
	
# Get list of pictures that have all matching keywords
matching_filenames = get_matching_pictures_advanced(search_dictionary, keyword_dictionary)

# At this point, matching_filenames is a simple list of full-path filenames
	
# Change the full path of each filename to match the web server
matching_filenames_corrected = []
for filename in matching_filenames:

	# SRC_PATH and DST_URL are defined in FS_common.py
	# SRC_PATH is the full-pathname as defined on my local computer before getting pushed up to webserver
	# DST_URL is the full-pathname where the pictures are located on the Web server
	matching_filenames_corrected.append(filename.replace(SRC_PATH, DST_URL))

# OK, now ready to start construction the HTML page
# We've got a list of image, each with a full path name (that matches the layout on the webserver)
	
# ---------------------------------
# --------- Start of form ---------
# ---------------------------------

# Create the HTML header and Font Awesome	
print """
<html>
<head>
<title>Family Search</title>
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
</head>
"""

# CSS Setup, include jQuery library and Cycle plugin
print """
<body>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
<script src="http://malsup.github.io/jquery.cycle2.js"></script>
<script src="http://malsup.github.io/jquery.cycle2.center.js"></script>
"""

# Setup main div for entire doc and internal CSS style sheets
#.cycle-overlay { font-family: tahoma, arial; position: absolute; bottom: 0; width: 70%; margin:auto; z-index: 600; background: black; color: white; padding: 15px; opacity: .6;}

print """
<div id="main">

<style>
.cycle-slideshow { width: auto; height: 70%; margin: auto; border: 1px solid #bbb; background: #ffc }
.cycle-slideshow img { width: auto; height: 100%; opacity: 0; filter:alpha(opacity=0); }
.lower-caption { width: 80%; margin:auto; border:3px solid #bbb; background: #eee }
.caption { font-size: 100%; }
.caption-category { font-weight: bold; color: red; }
.cycle-overlay { font-family: tahoma, arial; position:absolute; bottom:0; width:70%; margin:auto; z-index:600; background:black; color:white; padding:15px; opacity: .6;}
</style>
"""

# Put the Prev and Next links onto the page for the slideshow
# The id=next is what makes this link work.  Cycle2 Slideshow looks for that ID
print """
<div class=center style="text-align: center; font-size: 200%;">
  <a href=# id="prev"><i class="fa fa-arrow-circle-left" style="font-size:100%; color:black;"></i> Prev</a>
  &nbsp;&nbsp;&nbsp;
  <a href=# id="next">Next <i class="fa fa-arrow-circle-right" style="font-size:100%; color:black;"></i></a>
</div>
"""

# Setup div for Cycle2 slideshow
print """
<div class="cycle-slideshow"
     data-cycle-fx="scrollHorz"
     data-cycle-timeout="0"
     data-cycle-prev="#prev"
     data-cycle-next="#next"
     data-cycle-center-horz="true"
     data-cycle-center-vert="true"
     data-cycle-caption="#lower-custom-caption"
     data-cycle-caption-template="<center>Slide {{slideNum}} of {{slideCount}}</center><br>{{cycleTitle}}"
     >
"""

# Loop through matching images, and contrsuct HTML to support the Cycle jQuery tool
for image in matching_filenames_corrected:
	local_path = image.replace("http://www.burkins.com", "/home3/cburkins/public_html")
	metadata_path = image.replace(DST_URL, SRC_PATH)

        # keyword dictionary
        #      key : filename
        #      value : dictionary
        #         key : cateogry (P=ListOfPeople, L=ListofLocations, Y=ListofYears, R=ListOfRatings)
        #         value : list matching the category                                          

        if "Y" in keyword_dictionary[metadata_path]:
                year = str(((keyword_dictionary[metadata_path])["Y"])[0])
        else:
                year = 'Unknown'
                
        if "P" in keyword_dictionary[metadata_path]:
                peopleList = (keyword_dictionary[metadata_path])["P"]
                 # Convert the list of People into a comma-separated string
                people = ",".join(peopleList)
        else:
                people = 'Unknown'

        if "L" in keyword_dictionary[metadata_path]:
                locationList = (keyword_dictionary[metadata_path])["L"]
                 # Convert the list of People into a comma-separated string
                locations = ",".join(locationList)
        else:
                locations = 'Unknown'

        captionYear = 'Year = {0}'.format(year)
        captionPeople = 'People: {0}'.format(people)
        captionLocations = 'Location: {0}'.format(locations)
        
        title = '<span class=caption>{0}<BR>{1}<BR>{2}</span>'.format(captionYear, captionPeople, captionLocations)
    
        print '<img src="{0}", data-cycle-title="{1}">'.format(image, title)

        # Example      <img src="http://malsup.github.io/images/p1.jpg">

# End of slideshow <div>
print """
</div>
"""

# overlay
print """
<div class="cycle-overlay"></div>
"""


# empty element for caption 
print """
<div id="lower-custom-caption" class="lower-caption" style="font-size:150%"></div>
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

# end of main div
print """
</div>
</body>
</html>
"""

# ----------------------------------------------------- End ------------------------------------------

