# PhotoSearch

This is a rudimentary web application for searching through pictures based on the metadata within their EXIF tags.  This application doesn't actually search through all the EXIF tags, it's dependent on the presence of two files which contain the EXIF tag information.

1. <code>**Image_Metadatav2**</code> : Contains one line for each picture, along with all keywords for that picture
2. <code>**.KM_keyword_cache**</code> : Simply list of all unique keywords, one per line

