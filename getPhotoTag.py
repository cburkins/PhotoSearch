#!/usr/local/bin/python2.7

import os
import sys
import json
# import a local copy of pyexifinfo, which is just a wrapper for Phil Harvey's amazing EXIFTOOL
# EXIFTOOL started out as maninpulating EXIF tags within JPG images, but can not do MUCH more
# can read/write EXIF, IPTC, XMP, etc
# This is our local working directory (current location)
CWD = os.getcwd()
# Append the subdirectory for pyexifinfo
LIBROOT = CWD + "/pyexifinfo/pyexifinfo" 
# Add this to our library search path
sys.path.insert(0, LIBROOT)

EXIFTOOLPATH = "/home3/cburkins/public_html/family/pictures/Image-ExifTool-10.67"

# pyexifinfo simply makes an OS call to find "exiftool" executable in the system PATH
# Override that, and force it to find our local copy first by inserting our local dir first within the path
oldPath = os.environ["PATH"]
os.environ["PATH"] = EXIFTOOLPATH + os.pathsep + oldPath
 
# And it turn, that "exiftool" command line will look for it's own library, so we have to update the LIB path
os.environ["PERL5LIB"] = CWD + EXIFTOOLPATH + "/lib"

# Import pyexifinfo library
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

    if desiredTag in jsonExif.keys():
        return jsonExif[desiredTag]
    else:
        return None

# --------------------------------------------- Main -----------------------------------------------

if __name__ == "__main__":

    # Import system libs
    import argparse

    # Create a command-line args parser
    parser = argparse.ArgumentParser()
    # Add a mandatory positional argument to get the filename
    parser.add_argument("filename", help="JPG filename to parse for tags")
    # Add an optional argument to get the desired tag
    parser.add_argument("-t", "--tag", action='store', dest='tag', help="Destired EXIF/XMP tag. If omitted, show all tags")
    # Add an optional flag for verbose output
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity") 

    # Parse the given command-line args.  If illegal args are passed, then program exits here
    # NOTE: Unless told otherwise, argparse always treats arguments as strings
    args = parser.parse_args()
    # User gave correct command-line args
    filename = args.filename
    tag = args.tag
    
    if args.verbose:
        print "verbosity turned on"
        
    if args.verbose:
        print "Filename: {0}".format(filename)
        print "Desired tag: {0}".format(tag)
            
    # Check to see if user requested a specific EXIF tag on the command-line
    if tag is None:
        # User did not request a specific EXIF tag, so get ALL photo tags and print them
        allTags = getPhotoAllTags(filename)
        print( json.dumps(allTags, sort_keys=True, indent=4, separators=(',', ': ')) )
    else:
        # User requested a specific EXIF tag, so get EXIF/XMP tag from the picture, and print it
        tagContents = getPhotoTag(filename, tag)
        print "Tag Contents: {0}".format(tagContents)

# End of Main

# --------------------------------------------------------------------------------------------------
# ----------------------------------------------------- End ----------------------------------------
# --------------------------------------------------------------------------------------------------

