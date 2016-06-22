angular.
  module('schoolApp').
  factory('ClassRooms', ['$resource', function($resource) {
    return $resource('/api/v1/classrooms/:classroomId');
  }]);