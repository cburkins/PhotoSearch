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
# - Produces an HTML file
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

ROOT = "/home3/cburkins/public_html/cgi-bin/site-packages"
sys.path.insert(0, ROOT)
from PIL import Image

≈çROOT = "/home3/cburkins/public_html/family/search"
sys.path.insert(0, ROOT)

# Import my local code
from FS_common import *

from get_matching_pictures import *


# ------------------------------------------------------------------------

fileList = []
search_list = []
max_width = 800
max_height = 600

# ---------------------------------------------------------------------------------------------------

# Get pixel dimensions of a picture

def get_dimensions(filepath):
    width, height = Image.open(open(filepath)).size
    return width,height

# ---------------------------------------------------------------------------------------------------

# Given a max width and height, scale a picture to be contained inside that

def scale_dimensions(width, height, max_width, max_height):

    new_width = width * (max_height / float(height))
    new_height = max_height

    if (new_width > max_width):
        new_width = max_width
        new_height = height * (max_width / float(width))

    return int(new_width), int(new_height)

# ---------------------------------------------------------------------------------------------------
# -------------------------------------- Main  ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

theform = cgi.FieldStorage()

params = []
search_list = []


# Set the default picture size (can be overridden in user-submitted form)
picsize = 'Small'

# Based on the user-selected radio button from previous page, set picture size
# Ratio of 1.42 works well (e.g. 1000x700)
picsize = theform.getvalue("picsize");
if (picsize == 'Large'):
    max_width = 1000
    max_height = 700
elif (picsize == 'Medium'):
    max_width = 650
    max_height = 457
else : 
    max_width = 500
    max_height = 350


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


# go through list of filenames, and keep only filenames with "jpg" somewhere in filename
# images = [elem for elem in fileList if 'jpg' in elem]

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

	
# ---------------------------------
# --------- Start of form ---------
# ---------------------------------
	
print """
<!DOCTYPE html>
<head>
<title>Family Search</title>
<style type="text/css">
"""

# img_src = '<img src="' + image + '" width=' + str(new_width) + ' height=' + str(new_height) + ' alt="' + caption + '" />'
#print img_src

slideshow_width = max_width + 32
slideshow_height = max_height + 32
print_string = '.slideshow {  width: ' + str(slideshow_width) + 'px; height: ' + str(slideshow_height) + 'px; margin: auto; containerResize: 0;  }'
print print_string

print """
.slideshow img { padding: 15px; border: 1px solid #ccc; background-color: #eee; }
</style>

<!-- include jQuery library -->
<script type="text/javascript" src="http://www.burkins.com/family/pictures/search/jquery-1.10.2.min.js"></script>


<!-- include Cycle plugin -->

<!-- On 2013-12-14, commented out v2.72 of the cycle jquery app, and added local copy of v3.03 -->
<script type="text/javascript" src="http://www.burkins.com/family/pictures/search/jquery.cycle.all.3.03.js"></script>
<script type="text/javascript">

$.fn.cycle.defaults.nowrap = 1;

$(document).ready(function() {
    $('.slideshow').cycle({
		fx: 'scrollHorz',  // choose your transition type, ex: fade, scrollUp, shuffle, etc...
        next:   '#next2', 
        prev:   '#prev2',
		timeout: 0,
		after:     onAfter,
		containerResize: 0
		});
});

function onAfter(curr,next,opts) {
	var caption = 'Image ' + (opts.currSlide + 1) + ' of ' + opts.slideCount + '<br>' + this.alt;
	$('#caption').html(caption);
<!--	$('#caption').html(this.alt);  -->
}
</script>
</head>

<body>

    <center><div class="nav"><a id="prev2" href="#">Prev</a> -------- <a id="next2" href="#">Next</a></div></center>

	<div class="slideshow">
"""

# Loop through matching images, and contrsuct HTML to support the Cycle jQuery tool
for image in matching_filenames_corrected:
	local_path = image.replace("http://www.burkins.com", "/home3/cburkins/public_html")
	metadata_path = image.replace(DST_URL, SRC_PATH)
	width,height = get_dimensions(local_path)
	new_width,new_height = scale_dimensions(width, height, max_width, max_height)

        if "Y" in keyword_dictionary[metadata_path]:
            year = str(((keyword_dictionary[metadata_path])["Y"])[0])
        else:
            year = 'Unknown'

#	caption = "Local Path = " + local_path
#	caption = "Metadata Path = " + metadata_path
	caption = "Year = " + year + "<BR><BR><font color=#929292>Filename = " + local_path

	img_src = '<img src="' + image + '" width=' + str(new_width) + ' height=' + str(new_height) + ' alt="' + caption + '" />'
	print img_src


print """
		</div>
<center><p id="caption"></p></center>

</body>
</html>
"""

# ----------------------------------------------------- End ------------------------------------------

