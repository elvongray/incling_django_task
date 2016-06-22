from rest_framework import serializers

from models import Classroom, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'name', 'address', 'date_of_birth', 'gender'
        )


class ClassroomSerializer(serializers.ModelSerializer):
    classroom_students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ('id', 'name', 'capacity', 'classroom_students')
