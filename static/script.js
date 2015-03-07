var myApp = angular.module('twitterApp', []);

myApp.controller('twitterController', function ($scope, $http) {
  $scope.tweets = [];

  $scope.updateTweets = function (q) {
    $http.get('/api/search/' + q).success(function (data) {
      $scope.tweets = data.data;
    });
  };
});