from rest_framework import viewsets

from serializers import ClassroomSerializer, StudentSerializer

from models import Classroom, Student


class ClassroomsViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
