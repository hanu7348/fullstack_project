from django.contrib import admin
from .models import Course, Student ,Project

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    filter_horizontal = ('courses',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('topic', 'languages_used', 'duration')