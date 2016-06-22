angular.
  module('classroomList').
  component('classroomList', {
    templateUrl: 'static/js/classroom-list/classroom-list.template.html',
    controller: ['ClassRooms', function classroomListController(ClassRooms) {
      this.classrooms = ClassRooms.query();
    }]
  });