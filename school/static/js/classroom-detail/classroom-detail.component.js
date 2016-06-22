angular.
  module('classroomDetail').
  component('classroomDetail', {
    templateUrl: 'static/js/classroom-detail/classroom-detail.template.html',
    controller: ['$routeParams', 'ClassRooms',
      function classroomDetailController($routeParams, ClassRooms) {
        var self = this;
        self.classroom = {}
        ClassRooms.get({classroomId: $routeParams.classroomId}, function(classroom) {
          self.classroom = classroom;
        })
      }]
  });
