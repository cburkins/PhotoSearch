var app = angular.module('app', ['ui.bootstrap']);

app.config(function () {
	angular.element(document).bind('keyup', function (e) {
		if (e.keyCode === 39) {
		    console.log("Right arrow");
		    // jQuery ?
		    $(".carousel-control.right").click();
		}
		else if (e.keyCode === 37) {
		    console.log("Left arrow");
		    // jquery ?
		    $(".carousel-control.left").click();
		}
		else {
		    console.log("Key code: " + e.keyCode);
		}
	    });
    });

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

app.controller('CarouselDemoCtrl', function($scope, $location) {
	
	$scope.myInterval = 120000;
	$scope.slides = [
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" }
		     ];
	
    });

// -------------------------------------------------------------------------------------------------------------------------
// -------------------------- End ------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------
