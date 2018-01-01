angular.module('ui.bootstrap.demo', ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);


angular.module('ui.bootstrap.demo').controller('CarouselDemoCtrl', function ($scope) {
  $scope.myInterval = 5000;
  $scope.noWrapSlides = false;
  $scope.active = 0;
  var currIndex = 0;


    $scope.slides = [
         { id:0, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
         { id:1, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
         { id:2, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
         { id:3, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
         { id:4, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
         { id:5, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" },
         { id:6, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 04.jpg" },
         { id:7, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 03.jpg" },
         { id:8, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 31-2.jpg" },
         { id:9, text:"text goes here", image:"http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 21.jpg" }
         ];

         console.log($scope.slides)
});