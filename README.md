# PhotoSearch

This is a rudimentary web application for searching through pictures based on the metadata within their EXIF tags.  It's part of a larger ecosystem that I've developed for my own use.  There are three parts: a desktop application for tagging each picture with keywords, an online photo album based on jAlbum that can display all the metadata, and PhotoSearch (this piece) which allows me to search through all the pictures based on EXIF tags (e.g. a picture containing my wife and me which was taken between 2008 and 2010)

## Installation

It's not meant to be production-ready, it's really just an exercise for me, and I might as well share the code in case it's useful to someone else.

With that said, here how's to install it:
- exiftool: Update the file "getPhotoTag.py", specifically the variable EXIFTOOLPATH

Here's a good way to get exiftool
<code>wget https://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-10.67.tar.gz</code>
This can be copied into any directory (e.g. the directory right above this cloned repository)



## Usage

This application doesn't actually search through all the EXIF tags, it's dependent on the presence of two files which contain the EXIF tag information.

1. <code>**Image_Metadatav2**</code> : Contains one line for each picture, along with all keywords for that picture
2. <code>**.KM_keyword_cache**</code> : Simply list of all unique keywords, one per line

## History

I've been working on this program for years.  Very slowly.  It feels rather like I'm sitting on my front porch, and whittling on a stick.

## Dependencies

- jquery (included with code)
- Python 2.7 (likely already on the host machine)
- JavaScript (certainly built into the browser)
- exiftool (see Installation above)

## Tests of function functionality (sp directories)

- sp1
- sp2
- sp3
- sp4
- sp5
- sp6
- sp7
