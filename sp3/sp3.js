var app = angular.module('app', ['ui.bootstrap']);

app.controller('CarouselDemoCtrl', function($scope, $location) {
	
	console.log("hi");
	$scope.myInterval = 120000;
	$scope.slides = [
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
		     { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" }
		     ];
	
	var getKeyboardEventResult = function (keyEvent, keyEventDesc)
	    {
		return keyEventDesc + " (keyCode: " + (window.event ? keyEvent.keyCode : keyEvent.which) + ")";
	    };
	
	$scope.onKeyPress = function ($event) {
	    $scope.onKeyPressResult = getKeyboardEventResult($event, "Key press");
	    console.log("KeyPress");
	};

    });

// $(document).keydown(function(e) {
//     if (e.keyCode === 37) {
//        // Previous
//        $(".carousel-control.left").click();
//        return false;
//     }
//     if (e.keyCode === 39) {
//        // Next
//        $(".carousel-control.right").click();
//        return false;
//     }
// });


