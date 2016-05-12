from django.contrib import admin

from .models import School, Classroom, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'number_of_students', 'number_of_classrooms'
    )


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'school', 'capacity', 'number_of_student'
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'date_of_birth', 'gender', 'classroom', 'school'
    )
