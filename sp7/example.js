angular.module('ui.bootstrap.demo', ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);
angular.module('ui.bootstrap.demo').controller('CarouselDemoCtrl', function ($scope) {
	$scope.myInterval = 5000;
	$scope.noWrapSlides = false;
	$scope.active = 0;
	var slides = $scope.slides = [];
	var currIndex = 0;
	$scope.slides = [
		  { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg"},
		  { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
		  { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
		  { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
		  { image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" }
		  ];
	
	
	for (var i = 0; i < 5; i++) {
	    $scope.slides[i]["text"] = "Caption for Slide " + i;
	    $scope.slides[i]["id"] = i;
	}
	
	console.log(slides);
	console.log($scope.slides);
	$scope.addSlide = function() {
	    var newWidth = 600 + slides.length + 1;
	    slides.push({
		    image: '//unsplash.it/' + newWidth + '/300',
			text: ['Nice image','Awesome photograph','That is so cool','I love that'][slides.length % 4],
			id: currIndex++
			});
	};
	
	$scope.randomize = function() {
	    var indexes = generateIndexesArray();
	    assignNewIndexesToSlides(indexes);
	};
	
	// Randomize logic below
	
	function assignNewIndexesToSlides(indexes) {
	    for (var i = 0, l = slides.length; i < l; i++) {
		slides[i].id = indexes.pop();
	    }
	}
	
	function generateIndexesArray() {
	    var indexes = [];
	    for (var i = 0; i < currIndex; ++i) {
		indexes[i] = i;
	    }
	    return shuffle(indexes);
	}
	
	// http://stackoverflow.com/questions/962802#962890
	function shuffle(array) {
	    var tmp, current, top = array.length;
	    
	    if (top) {
		while (--top) {
		    current = Math.floor(Math.random() * (top + 1));
		    tmp = array[current];
		    array[current] = array[top];
		    array[top] = tmp;
		}
	    }
	    
	    return array;
	}
    });

// --------------------------------------------------------------------------------------------------
// ------------------- End --------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------
