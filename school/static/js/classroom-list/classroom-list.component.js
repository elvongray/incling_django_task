angular.
  module('classroomList').
  component('classroomList', {
    templateUrl: 'static/js/classroom-list/classroom-list.template.html',
    controller: ['ClassRooms', function classroomListController(ClassRooms) {
      var self = this;
      self.classrooms = [];
      ClassRooms.query().$promise.then(function(data){
        self.classrooms = angular.fromJson(angular.toJson(data));
      });
    }]
  });