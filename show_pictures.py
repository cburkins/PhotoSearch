#!/usr/local/bin/python2.7

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

# Import my local code (which is located in the same directory as this script)
# Needs a file called FS_common.py
from FS_common import *
# Needs a file called get_matching_pictures.py
from get_matching_pictures import *
# Needs a file called getPhotoTag
from getPhotoTag import *

# ------------------------------------------------------------------------

fileList = []
search_list = []

# ---------------------------------------------------------------------------------------------------
# -------------------------------------- Main  ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# Read HTML form from standard input, and put into a dictionary
# returns a variable of type "instance"
theform = cgi.FieldStorage()

params = []
search_list = []

# Using hidden value passed via form, build a search dictionary (used later)
# Desired Keywords (e.g. People, Places, Events) are in one big list associated with the key "Keyword"
# Careful, if there's only one term, it's a string, if more than one, it's a list.  
# Need a list for next section of code, so if needed, convert single item to a list

# From the HTML form, get value from the field "Keyword"
keyword_item = theform.getvalue("Keyword");

if (isinstance(keyword_item, str)):
        # Convert single item to a list
	keyword_list = [keyword_item]
else:
        # it's a list, so multiple desired keywords, so just copy the list
	keyword_list = keyword_item;
	

# Initialize the search dictionary to be the empty dictionary	
search_dictionary = {}

# Parse through desired keyword list, and create seperate lists in a dictionary called "search_dictionary"
# Construct the search_dictionary (contains the keywords that we're searching for)
# L = Location
# E = Event
# Y = Year
# R = Rating
# A = Artist
# Everything else is a person

# Loop through desired keywords, and construct a dictionary that will be used to search through all pictures	
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

       	elif (keyword.startswith("N:")):

		# Strip off the N: at beginning of keyword
		keyword = keyword[2:]

		# Add keyword to search_dictionary
		search_dictionary = dictionary_list_push(keyword, 'numberPeople', search_dictionary)



	else:
		search_dictionary = dictionary_list_push(keyword, 'People', search_dictionary)


# Get the dictionary of all keywords in my pictures (this is a big dictionary)
# Parses the static Image_Metadata file (which has one line per picture)
# Pathname of each pic is the local path on my Linux machine at home (e.g. /mnt/ChadDocs/My Webs/www.burkins.com/)
keyword_dictionary = get_keyword_dictionary(Image_Metadata)
	
# Slim down list of pictures to those that have all matching keywords (that were given in search form by users)
matchingPictures = get_matching_pictures_advanced(search_dictionary, keyword_dictionary)

# OK, now ready to start construction the HTML page
	
# ---------------------------------
# --------- Start of form ---------
# ---------------------------------

# Create the HTML header, get Font Awesome, get the local external CSS style sheet
# The CSS version is just a trick to force the browser to load CSS when I change that file	
print """
<html>
<head>
<title>Family Search</title>
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="show_pictures.css?version=1.44">
</head>
"""

# Include jQuery library and Cycle plugin
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

     <!-- empty element for caption (used for picture x/y count, CSS will place in top-right of picture -->
     <div class="cycle-caption"></div>
"""

# Loop through matching images, and contrsuct HTML to support the Cycle jQuery tool
# Pathname on the home linux machine (e.g. /mnt/ChadDocs/My Webs/www.burkins.com/01 - Web Albums/Family Pics - Turtle - Production/album/Pictures 2000s)
for imageHomeFile in matchingPictures:
        
        # Pathname on the web server (e.g. http://www.burkins.com/family/pictures/album/Pictures 2000s)
        imageWebURL = imageHomeFile.replace(SRC_PATH, DST_URL)

        # Filesystem pathname on the web server (e.g. /home3/cburkins/public_html/family/pictures/album/Pictures\ 2000s)
        localPhotoFile = imageHomeFile.replace(SRC_PATH, Root)

        # Short filename
        shortFilename = os.path.basename(localPhotoFile)

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
                
        # Find the Year in the picture metadata
        if "X" in keyword_dictionary[imageHomeFile]:
                dateTime = str(((keyword_dictionary[imageHomeFile])["X"])[0])
        else:
                dateTime = 'Unknown'
                
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

        # Get the photo description (caption) from the photo itself (i.e. open the file, and read metadata)
        if not (os.path.isfile(localPhotoFile)):
                descr = "File missing: {0}".format(localPhotoFile)
        else:
                # Get the photo's caption
                descr = getPhotoTag(localPhotoFile, "XMP:Description")
                if descr is None:
                        descr="No caption" 
                # If caption is an integer, cast to a string
                if type(descr) is int:
                        descr = str(descr)
                # convert to string by encoding with utf-8 character set
                # Could use str() instead, but that sometimes fails with error if it can't encode correctly
                descr = descr.encode('utf-8')
                # Replace double-quotes with HTML-friendly version of same
                temp = descr.replace('\"', '&quot')
                descr = temp

        # Create a caption-line for each element, insert a span tag for CSS formatting
        captionFilename = '<span class=caption-category>Filename:</span> {0}'.format(shortFilename)
        captionYear = '<span class=caption-category>Year:</span> {0}'.format(year)
        captionDateTime = '<span class=caption-category>Date Time:</span> {0}'.format(dateTime)
        captionPeople = '<span class=caption-category>People:</span> {0}'.format(people)
        captionLocations = '<span class=caption-category>Location:</span> {0}'.format(locations)
        captionEvents = '<span class=caption-category>Event:</span> {0}'.format(events)
        captionDescr = '<span class=caption-category>Caption:</span> {0}'.format(descr)
        
        # Create the full multi-line title to be displayed in the overlay at the bottom of the picture
        # Use a single span so we can apply CSS, and insert line breaks
        title = '<span class=caption>{0}<BR>{1}<BR>{2}<BR>{3}<BR>{4}<BR>{5}<BR>{6}</span>'.format(captionFilename, captionYear, captionDateTime, captionPeople, captionLocations, captionEvents, captionDescr)
    
        # Insert the complete HTML img tag for this picture into the slideshow <div>
        print '<img src="{0}", data-cycle-desc="{1}">'.format(imageWebURL, title)

        # Example      <img src="http://malsup.github.io/images/p1.jpg">
        # Complex Ex:  <img src="http://malsup.github.io/images/p1.jpg" data-cycle-desc="<span class=caption-category>People:</span> Bob Burkins, Chad Burkins, Tom Burkins<br><span class=caption-category>Location:</span> Walt Disney World<br>" >


# End of slideshow <div>
print """
<div class="cycle-overlay"></div>
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

