angular.
  module('schoolApp').
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.
      when('/classrooms', {
        template: '<classroom-list></classroom-list>'
      }).
      when('/classrooms/:classroomId', {
        template: '<classroom-detail></classroom-detail>'
      }).
      otherwise('/classrooms');
  }]);
