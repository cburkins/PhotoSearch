
# --------------------------------------------------------------------------


def dictionary_list_push (entry, category, dictionary_list):

	if (category in dictionary_list):
		dictionary_list[category].append(entry)
	else:
		dictionary_list[category] = [entry]

	return dictionary_list
	
# --------------------------------------------------------------------------
