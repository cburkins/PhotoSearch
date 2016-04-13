import os
import sys
import cgi

# ------------------------------------------------------------------------
# Basic Description : This module gets called with a list of keywords,
# and will use a JQuery applet to show them.
#
# To Do
#
# - Buttons to skip forward 10 pictures
# ------------------------------------------------------------------------

print "Content-Type: text/html"
print


# ------------------------------------------------------------------------


theform = cgi.FieldStorage()



# ---------------------------------
# --------- Start of form ---------
# ---------------------------------
	
print """
<head>
<title>Family Search</title>
</head>
<body>
<pre>
"""

# Using hidden value passed via form, build a search dictionary (used later)
for keyword in theform.getvalue("Keyword"):
	print keyword
	


print """
</pre>
</body>
</html>
"""

# ---------------------------- End -------------------------------

