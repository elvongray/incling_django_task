
"""
A simple representation of a school, classroom and student models
with the relationships between them.
"""

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from school.categories import Gender_Categories, School_Categories


@python_2_unicode_compatible
class School(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    address = models.TextField(blank=False)
    date_established = models.DateField()
    gender_allowed = models.CharField(choices=Gender_Categories)
    school_type = models.CharField(choices=School_Categories)

    def __str__(self):
        return '{}'.format(self.name)


@python_2_unicode_compatible
class Classroom(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    school = models.ForeignKey(School)
    capacity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)


@python_2_unicode_compatible
class Student(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    classroom = models.ForeignKey(Classroom)

    def __str__(self):
        return '{}'.format(self.name)
