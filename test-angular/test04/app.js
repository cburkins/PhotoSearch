var app = angular.module('ui.bootstrap.demo', ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);


// Pretty sure this directive is allowing direct communication with the carousel controller
app.directive('carouselControls', function() {
   return {
      require: '^uibCarousel',
      link: function(scope, element, attrs, carouselCtrl) {
         scope.goNext = function() {
            carouselCtrl.next();
         };
         scope.goPrev = function() {
            carouselCtrl.prev();
         };
      }
   };
})


angular.module('ui.bootstrap.demo').controller('CarouselDemoCtrl', function($scope) {
   // delay (ms) between automatic slide advancement
   $scope.myInterval = 60000;
   // true means that you cannot wrap around the end
   $scope.noWrapSlides = true;
   // Index of slide to start with first      
   $scope.active = 0;


   // Called when a keyboard key is pressed down
   $scope.keyPress = function(eve) {
      $scope.key_code = eve.which;
      if (eve.which === 37) {
         $scope.goPrev();
      }
      if (eve.which === 39) {
         $scope.goNext();
      }
      console.log("KeyPress: code is " + $scope.key_code)
   }

   // Called when a keyboard key is released up
   $scope.keyRelease = function(eve) {
      console.log("KeyRelease: code is " + eve.which)
   }


   $scope.slides = [
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 04.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 03.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 31-2.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 21.jpg" }
   ];
   $scope.slidesAll = [
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.52.51.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.10.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-18 14.02.22.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-16 18.44.43.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-01 Misc/slides/2013-06-17 13.11.26.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 04.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-12 Longwood Christmas/slides/2013-12 Longwood Christmas 03.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 31-2.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 21.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 03-2.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 Longwood with Owen/slides/Longwood w Owen 10-2.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 21.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 18.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 45.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 10.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 11.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 12.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 09.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 01.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-08 JK Wedding/slides/JKWedding 08.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 39.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 15.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 23.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 09.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 08.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 40.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 38.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 32.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 17.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 12.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 44.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 13.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 07.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 45.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 42.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 16.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 30.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 41.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 24.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 43.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 11.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 37.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 14.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 36.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 06.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 31.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 10.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 46.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 05.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Owen/slides/2013-09 Owen Sept Pics 35.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 013.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 008.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 006.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 004.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 045.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 057.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 055.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 015.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 058.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 052.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 049.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 018.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 014.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 061.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 017.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 063.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 005.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 041.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 054.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 016.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 023.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 056.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 042.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 062.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 048.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 059.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 024.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 021.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 060.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 053.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 034.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 047.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 022.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 050.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 040.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 039.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 046.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-09 Mt Gretna/slides/Mt Gretna 2013 007.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 32.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 18.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 29.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 24.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 31.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 17.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 26.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 27.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 13.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 19.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 28.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 33.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-02 Adirondacks Winter/slides/Adirondacks Winter 2013 25.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 065.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 092.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 093.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 009.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 099.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 077.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 045.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 008.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 066.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 084.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 041.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 060.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 025.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 078.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 097.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 071.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 087.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 069.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 054.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 090.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 076.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 010.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 098.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 095.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 089.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 055.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 072.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 017.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 094.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 021.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 013.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 023.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 088.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 016.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 007.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 070.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 086.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 018.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 015.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 085.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 075.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 058.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 046.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 083.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 050.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 068.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 047.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 020.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 091.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 073.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 001.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 011.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 064.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 014.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 067.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 100.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 049.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 027.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 036.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 040.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 057.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 037.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 012.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 096.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 074.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 079.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 039.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 082.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 026.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 019.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-04 Belgium/slides/Belgium Apr 2012 022.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 12.14.27.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-20 09.31.41.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-10 07.55.52.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-28 10.51.58.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-28 10.51.20.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-01 15.30.26.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-08 10.32.34.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 12.09.52.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-15 18.41.23.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-21 18.56.34.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-09 17.00.37.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 11.57.33.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-25 11.33.51.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-29 08.02.53.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-13 11.07.36.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-28 17.24.46.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 11.54.17.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-09 16.57.07.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 12.06.52.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-16 12.18.37.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-28 11.01.16.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-13 19.39.55.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-18 15.16.26.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-18 14.44.38.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-09 07.51.51.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-30 11.54.35.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-09 18.40.12.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-26 17.40.41.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-14 18.57.25-1.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-10 17.37.02.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-10 07.44.56 HDR.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-19 08.19.34.jpg" },
      { image: "http://www.burkins.com/family/pictures/album/Pictures 2013/2013-11 Owen/slides/2013-11-10 07.52.00 HDR.jpg" }
   ];



});