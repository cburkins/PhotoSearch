#!/usr/local/bin/python2.7

# Import system libs
import os
import sys
import json
import argparse

# import a local copy of pyexifinfo, which is just a wrapper for Phil Harvey's amazing EXIFTOOL
# EXIFTOOL started out as maninpulating EXIF tags within JPG images, but can not do MUCH more
# can read/write EXIF, IPTC, XMP, etc
LIBROOT = "/home3/cburkins/public_html/family/pictures/search/pyexifinfo/pyexifinfo"
sys.path.insert(0, LIBROOT)
import pyexifinfo as pyexifinfo

# --------------------------------------------------------------------------------------------------

# Input: a filename
# Output: Reads all EXIF/XMP/IPTC tags, and returns a JSON data structure for all tags to the caller

def getPhotoAllTags (filename):

    # Check for python v2.7 or better
    if sys.version_info < (2, 7):
        print "\n   Must use python 2.7 or greater, exiting...\n\n"
        sys.exit()

    # Verify that given filename exists
    if not (os.path.isfile(filename)):
        print '\n\n  File does NOT exist: {0}\n   Exiting...\n\n'.format(filename) 
        sys.exit()

    # Extract all EXIF/XMP/IPTC from picture, seems to return a JSON structure as the first element of a list
    datalist = pyexifinfo.get_json(filename)
    # Get the first element of the list, which ends up being a JSON structure
    jsonExif = datalist[0]

    # Return the entire JSON data structure (for the photo metatags) to the caller
    return jsonExif


# --------------------------------------------------------------------------------------------------

# Input: a filename and a desired tag
# Output: Reads all EXIF/XMP/IPTC tags, returns the desired tag as a string

def getPhotoTag(filename, desiredTag):

    jsonExif = getPhotoAllTags(filename)

    return jsonExif[desiredTag]

# --------------------------------------------- Main -----------------------------------------------

# Create a command-line args parser
parser = argparse.ArgumentParser()
# Add a mandatory positional argument to get the filename
parser.add_argument("filename", help="JPG filename to parse for tags")
# Add an optional argument to get the desired tag
parser.add_argument("-t", "--tag", action='store', dest='tag', help="Destired EXIF/XMP tag. If omitted, show all tags")

sys.exit()

# Parse the given command-line args.  If illegal args are passed, then program exits here
# NOTE: Unless told otherwise, argparse always treats arguments as strings
args = parser.parse_args()

filename = args.filename
tag = args.tag

# Get desired filename (e.g. "/home3/cburkins/test.jpg")
#filename = sys.argv[1]

# Get desired tag (e.g. "XMP:Description")
#tag = sys.argv[2]

# Get all photo tags and print them
allTags = getPhotoAllTags(filename)
print( json.dumps(allTags, sort_keys=True, indent=4, separators=(',', ': ')) )

# Get a single EXIF/XMP tag from the picture, and print it
tagContents = getPhotoTag(filename, tag)
print "Tag Contents: {0}".format(tagContents)

# --------------------------------------------------------------------------------------------------
# ----------------------------------------------------- End ----------------------------------------
# --------------------------------------------------------------------------------------------------

