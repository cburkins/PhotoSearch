
var SearchRoot = "http://www.burkins.com/family/pictures/search/";

// ----------------------------------------------------------------------------

/*

Description : 
	- This is a partner file to index.html.  Both files are needed together
	- It contains all the associated javascript routines for the html form
	
Subroutines :
	- YearKeypress : Called each time a key is pressed in Year field on html form
	- RatingKeypress : Called each time a key is pressed in rating field on html form
	- UpdateScreenWithSelectedItem : Adds a row to the list of keywords, called by Javascript callbacks below
	- InsertHiddenField : User has selected keyword, hides keyword in form for later reference by show_pictures.py
	- UpdateTotal : Via AJAX, updates the "Total" row within the table
	- Javascript callback for "people" field : On selection of item in list, calls UpdateScreenWithSelectedItem
	- Javascript callback for "places" field : On selection of item in list, calls UpdateScreenWithSelectedItem
	- Javascript callback for "events" field : On selection of item in list, calls UpdateScreenWithSelectedItem
	- ClearForm : Clear the form (both hidden fields and visable data)
	- SubmitVerify : Used on form submission, to double-check that there is at least one keyword

*/

// ----------------------------------------------------------------------------

/* 
Description : Called each time a key is pressed in Year field on html form

Input : event

*/

function YearKeypress(event)
{
	// I think this is for Internet Explorer (IE)
	if (!event) event=window.event;

	var keyCode = event.which;
	if (keyCode == undefined) {
		keyCode = event.keyCode;
    }
	if (keyCode == 13) {
		// Enter was pressed, return false
//		alert (document.getElementById('year').value);
	
		// Check to see if user entered a valid four digit year, or a valid range of years (e.g. 1972, 1972-1974 are both valid)
		if (! ((/^[0-9][0-9][0-9][0-9]$/.test(document.getElementById('year').value)) ||
				(/^[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$/.test(document.getElementById('year').value)))) {
			alert ("You did not enter a valid four digit year or range of years (e.g. 1987 or 1990-1994)");
			return false;
		}

		// Capture the year entered
		search_term = "Y:" + document.getElementById('year').value;
		
		// Insert the new keyword in the table on the bottom of form
		UpdateScreenWithSelectedItem(search_term);

		// Insert the new keyword as a hidden field in the form
		InsertHiddenField(search_term);

		// Update total row of table
		UpdateTotal();	
			
		// Clear the field and turn background to white
		document.getElementById('year').value = "";
		document.familySearchForm.year.style.backgroundColor="#FFFFFF";
		
		// Return false, otherwise the form will see the <enter> key, and try to submit the form
		return false;
	}
	else {
		
		// New keystroke has not been added to field yet, so need to figure it out
		value = document.getElementById('year').value + String.fromCharCode(keyCode);
				
		// Change background color (green for valid year, red for partial or invalid year)
		if (! ((/^[0-9][0-9][0-9][0-9]$/.test(value)) ||
				(/^[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$/.test(value)))) {
			// Input field currently *does not* contain a valid year, so turn background to red
			document.familySearchForm.year.style.backgroundColor="#FF6666";
		}
		else {
			// Input field currently contains a valid year, so turn background to green
			document.familySearchForm.year.style.backgroundColor="#99FF66";
		}
		return keyCode;
	}

	//	alert ("The Unicode key code of the released key: " + keyCode);
	
}

// ------------------------------------------------------------------


/* 

Description : Called each time a key is pressed in Year field on html form

Input : event

*/

function RatingKeypress(event)
{
	// I think this is for Internet Explorer (IE)
	if (!event) event=window.event;

	var keyCode = event.which;
	if (keyCode == undefined) {
		keyCode = event.keyCode;
    }
	if (keyCode == 13) {
		// Enter was pressed, return false
//		alert (document.getElementById('year').value);
	
		// Check to see if user entered a valid four digit year, or a valid range of years (e.g. 3 or 3-5 are both valid)
		if (! ((/^[1-5]$/.test(document.getElementById('rating').value)) ||
				(/^[1-5]-[1-5]$/.test(document.getElementById('rating').value)))) {
			alert ("You did not enter a valid rating or range of ratings (e.g. 3 or 3-5)");
			return false;
		}

		// Capture the year entered
		search_term = "R:" + document.getElementById('rating').value;
		
		// Insert the new keyword in the table on the bottom of form
		UpdateScreenWithSelectedItem(search_term);

		// Insert the new keyword as a hidden field in the form
		InsertHiddenField(search_term);

		// Update total row of table
		UpdateTotal();	
			
		// Clear the field and turn background to white
		document.getElementById('rating').value = "";
		document.familySearchForm.rating.style.backgroundColor="#FFFFFF";
		
		// Return false, otherwise the form will see the <enter> key, and try to submit the form
		return false;
	}
	else {
		
		// New keystroke has not been added to field yet, so need to figure it out
		value = document.getElementById('rating').value + String.fromCharCode(keyCode);
				
		// Change background color (green for valid rating, red for partial or invalid rating)
		if (! ((/^[1-5]$/.test(value)) ||
				(/^[1-5]-[1-5]$/.test(value)))) {
			// Input field currently *does not* contain a valid rating, so turn background to red
			document.familySearchForm.rating.style.backgroundColor="#FF6666";
		}
		else {
			// Input field currently contains a valid year, so turn background to green
			document.familySearchForm.rating.style.backgroundColor="#99FF66";
		}
		return keyCode;
	}

	//	alert ("The Unicode key code of the released key: " + keyCode);

	
}

// --------------------------------------------------------------------------

UpdateScreenWithSelectedItem = function(elemID) {

	// Create a row in table, and insert selected item
	var numrows=document.getElementById('myTable').rows.length;
	var index = numrows - 1;
	var x=document.getElementById('myTable').insertRow(index); 
	x.setAttribute("id", elemID); 
	var y=x.insertCell(0);
	var z=x.insertCell(1); 
	y.innerHTML=elemID; 
	z.innerHTML="No call";

	// Call to find out how many pictures have this selected keyword
	if (window.XMLHttpRequest)  {
		// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
	else {
		// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			// Update the pic count in the correct row of the table
			document.getElementById(elemID).cells[1].innerHTML=xmlhttp.responseText;
		}
	}
	var ajax_call = SearchRoot + "/numPics.py?Keyword=" + elemID;
	xmlhttp.open("GET",ajax_call,true);
	xmlhttp.send();

}

// ----------------------------------------------------------------------------

InsertHiddenField = function(elemID) {

	// Create a new hidden field, and append it to the form within the DOM
	currentElement = document.createElement("input");
	currentElement.setAttribute("type", "hidden");
	currentElement.setAttribute("name", "Keyword");
	currentElement.setAttribute("id", "hiddenID");
	currentElement.setAttribute("value", elemID);
	document.forms['familySearchForm'].appendChild(currentElement);

}

// ----------------------------------------------------------------------------

UpdateTotal = function() {

	// Loop through hidden fields, looking at them
	var total = 0;
	var start = document.getElementsByName("Keyword");
	var startlength = start.length;
	var numKeywords = start.length;
//			document.getElementById("totalRow").cells[1].innerHTML=numKeywords;
	
	var keywords;
	for(var i = (start.length - 1); i >= 0; i--) {

		var elemarray = document.getElementsByName("Keyword");
		var obj = elemarray[i];
		if (keywords == undefined) {
		   keywords = "Keyword=" + obj.value
		}
		else {
		   keywords = keywords + "&Keyword=" + obj.value
		}
				
	}
//			alert("Keywords = " + encodeURI(keywords));

	// Call to find out how many pictures have this selected keyword
	var xmlhttpa;
	if (window.XMLHttpRequest)  {
		// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttpa=new XMLHttpRequest();
	}
	else {
		// code for IE6, IE5
		xmlhttpa=new ActiveXObject("Microsoft.XMLHTTP");
	}
	
	// This will receive the answer back from the HTTP request above
	xmlhttpa.onreadystatechange=function() {
		if (xmlhttpa.readyState==4 && xmlhttpa.status==200) {
			// Update the pic count in the correct row of the table
			document.getElementById("totalRow").cells[1].innerHTML=xmlhttpa.responseText;
		}
	}
	
	// Put the AJAX call in motion to query and receive the number of pics matching keywords
	var ajax_call = SearchRoot + "/numPics.py?" + encodeURI(keywords);
	xmlhttpa.open("GET",ajax_call,true);
	xmlhttpa.send();

}


// ----------------------------------------------------------------------------
  
  
// Create a JavaScript function that will be associated with People search field
// (function () <code>) creates a function, and return it to the parent scope (i.e. index.html)
// $ sign is used to define/access jQuery
// $ sign signifies that this is JavaScript
// This is shorthand for the jQuery document ready event
// So $() is the same as $( document ).ready()
// So this code is run when the DOM (or document) is ready on the screen

// This is also might be an anonymous self-invoking function (i.e. a function without a name)

$(function() {

	// Select element of HTML with id of "people", and associate jQuery autocomplete function with it
	// jQuery syntax is tail-made for selecting HTML elements and performing some action on the elements
	$( "#people" ).autocomplete({
		
		// Define the list to be searched as the user is typing in the field
		// In this case, we are defining a String, so jQuery assumes we are calling a URL
		// In this case, we are calling a python script via HTTP
		// If the user typed "Bob" into the form field, then a 
		// a GET request is constructed http://example.com?term=Bob
		// Script must parse for the "term" field, and return JSON data
		source: SearchRoot + "/searchPeople.py",

		// jQuery Autocomplete option: Mininum number of characters needed in field before search (i.e. source is called)	
		minLength:1,
		
		// jQuery Autocomplete option: Amount of idle time (in milliseconds) that we wait until be begin to search (default is 300)
		delay:100,

		// Function called when user selects item from drop-down list
		select: function(event, ui) {

			// Clear the search field
			// Set the value of the matched element to "" (i.e. the empty string)
			$('#people').val("");
			// I'm not sure what this does....
			$('#autocomplete').val("");

			// Insert the new keyword (from autocomplete) into the table on the bottom of form
			UpdateScreenWithSelectedItem(ui.item.label);

			// Insert the new keyword as a hidden field in the form
			InsertHiddenField(ui.item.label);

			// Update total row of table
			UpdateTotal();
			
			// By returning false, it keeps the form from being submitted when the user hits <enter>
			return(false);
		}
	});
});

  
// ----------------------------------------------------------------------------

// Create a JavaScript function that will be associated with Artist search field
$(function() {
	
	$( "#artist" ).autocomplete({
		
		source: SearchRoot + "/searchArtist.py",

		// Mininum number of characters needed from user before search starts	
		minLength:1,
		
		// Amount of idle time (in milliseconds) that we wait until be begin to search (default is 300)
		delay:100,

		// Function called when user selects item from drop-down list
		select: function(event, ui) {

			// Clear the search field
			$('#artist').val("");
			$('#autocomplete').val("");

			// Inser the new keyword in the table on the bottom of form
			UpdateScreenWithSelectedItem(ui.item.label);

			// Insert the new keyword as a hidden field in the form
			InsertHiddenField(ui.item.label);

			// Update total row of table
			UpdateTotal();
			
			// By returning false, it keeps the form from being submitted when the user hits <enter>
			return(false);
		}
	});
});

// ----------------------------------------------------------------------------

// Create a JavaScript function that will be associated with Places search field

$(function() {
	
	// Guessing here: Define the autocomplete function for the form input field with an id of "places"
    // This is part of something called "DOM Traversal and Manipulation"	
	$( "#places" ).autocomplete({
		
		source: SearchRoot + "/searchPlaces.py",

		// Mininum number of characters needed from user before search starts	
		minLength:1,

		// Amount of idle time (in milliseconds) that we wait until be begin to search (default is 300)
		delay:100,		
		
		// Function called when user selects item from drop-down list
		select: function(event, ui) {

			// Clear the search field
			$('#places').val("");
			$('#autocomplete').val("");

			// Inser the new keyword in the table on the bottom of form
			UpdateScreenWithSelectedItem(ui.item.label);

			// Insert the new keyword as a hidden field in the form
			InsertHiddenField(ui.item.label);

			// Update total row of table
			UpdateTotal();
			
			// By returning false, it keeps the form from being submitted when the user hits <enter>
			return(false);
		}
	});
});

// ----------------------------------------------------------------------------
	
// Create a JavaScript function that will be associated with Events search field
$(function() {
	
	$( "#events" ).autocomplete({
		
		source: SearchRoot + "/searchEvents.py",

		// Mininum number of characters needed from user before search starts	
		minLength:1,

		// Amount of idle time (in milliseconds) that we wait until be begin to search (default is 300)
		delay:100,		
		
		// Function called when user selects item from drop-down list
		select: function(event, ui) {

			// Clear the search field
			$('#events').val("");
			$('#autocomplete').val("");

			// Inser the new keyword in the table on the bottom of form
			UpdateScreenWithSelectedItem(ui.item.label);

			// Insert the new keyword as a hidden field in the form
			InsertHiddenField(ui.item.label);

			// Update total row of table
			UpdateTotal();
									
			// By returning false, it keeps the form from being submitted when the user hits <enter>
			return(false);
		}
	});
});

// ----------------------------------------------------------------------------

if(typeof(window.external) != 'undefined'){

//yes, this is evil browser sniffing, but only IE has this bug

document.getElementsByName = function(name, tag){
    if(!tag){
        tag = '*';
    }
    var elems = document.getElementsByTagName(tag);
    var res = []
    for(var i=0;i<elems.length;i++){
        att = elems[i].getAttribute('name');
        if(att == name) {
            res.push(elems[i]);
        }
    }
    return res;
}

}

// ----------------------------------------------------------------------------

function ClearForm () {

    // Query how many keywords are hidden in the form
	var numKeywords = document.getElementsByName("Keyword").length;

	// Number of rows includes the header and total, so add 2
	var numRows = numKeywords + 2;
	
	for(var i = (numKeywords - 1); i >= 0; i--) {
	
		var elemarray = document.getElementsByName("Keyword");

		var obj = elemarray[i];
		// obj.id and and obj.value are two useful methods
		
 		document.forms['familySearchForm'].removeChild(obj)
	
		// Delete corresponding row in table (offset by +1 since 1st row is actually header)
		document.getElementById('myTable').deleteRow(i+1)
		
	}

	// Clear the year input field and make sure background is white
	document.getElementById('year').value = "";
	document.familySearchForm.year.style.backgroundColor="#FFFFFF";
	
	// Clear the totals row in the table
	document.getElementById("totalRow").cells[1].innerHTML=0;
}

// ----------------------------------------------------------------------------

function SubmitVerify (form) {

    var numKeywords = document.getElementsByName("Keyword").length;

	ErrorMessage = "You must enter at least one search term using the blank fields (People, Places, Events). " +
	"Just start typing in one of the fields, and the form will give you helpful suggestions that match. " +
	"Keep typing to narrow the number of suggestions, or use the down arrow and enter to select one of the suggestions\n\n"
	
	if (numKeywords > 0) {
		return true;
	}
	else {
		alert(ErrorMessage);
		return false;
	}
}

// ----------------------------------------------------------------------------
// ----------------------------------------------------------------------------
// ----------------------------------------------------------------------------
