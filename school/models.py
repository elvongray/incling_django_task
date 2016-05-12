
"""
A simple representation of a school, classroom and student models
with the relationships between them.
"""

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from school.categories import Gender_Categories, School_Categories, Gender


@python_2_unicode_compatible
class School(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    address = models.TextField(blank=False)
    date_established = models.DateField()
    gender_allowed = models.CharField(max_length=1, choices=Gender_Categories)
    school_type = models.CharField(max_length=20, choices=School_Categories)

    def __str__(self):
        return '{}'.format(self.name)

    def number_of_students(self):
        return self.students.count() or 0
    number_of_students.short_description = 'Number of students'

    def number_of_classrooms(self):
        return self.classrooms.count() or 0
    number_of_classrooms.short_description = 'Number of classrooms'


@python_2_unicode_compatible
class Classroom(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    school = models.ForeignKey(School, related_name='classrooms')
    capacity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

    def number_of_student(self):
        return self.classroom_students.count() or 0


@python_2_unicode_compatible
class Student(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    address = models.TextField(blank=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender)
    school = models.ForeignKey(School, related_name='students', null=True)
    classroom = models.ForeignKey(Classroom, related_name='classroom_students')

    def __str__(self):
        return '{}'.format(self.name)
