# PhotoSearch

This is a rudimentary web application for searching through pictures based on the metadata within their EXIF tags.  This application doesn't actually search through all the EXIF tags, it's dependent on the presence of two files which contain the EXIF tag information.

Image_Metadatav2: Contains one line for each picture, along with all keywords for that picture
.KM_keyword_cache: Simply list of all unique keywords, one per line

