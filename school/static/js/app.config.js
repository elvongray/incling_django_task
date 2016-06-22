angular.
  module('schoolApp').
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.
      when('/classrooms', {
        template: '<classroom-list></classroom-list>'
      }).
      when('/classrooms/:classroomsId', {
        template: '<classroom-list></classroom-list>'
      }).
      otherwise('/classrooms');
  }]);
