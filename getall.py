# ----------------------------------------------------------------------

def getall(theform, nolist=False):
    """
    Passed a form (cgi.FieldStorage
    instance) return *all* the values.
    This doesn't take into account
    multipart form data (file uploads).
    It also takes a keyword argument
    'nolist'. If this is True list values
    only return their first value.
    """
    data = {}
    for field in theform.keys():                
    # we can't just iterate over it, but must use the keys() method
        if type(theform[field]) ==  type([]):
            if not nolist:
                data[field] = theform.getlist(field)
            else:
                data[field] = theform.getfirst(field)
        else:
            data[field] = theform[field].value
    return data
	
# --------------------------------------------------------------------------
