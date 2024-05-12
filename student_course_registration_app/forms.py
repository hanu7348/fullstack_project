from django import forms
from .models import Student, Course, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'courses', 'project']  # Use 'project' instead of 'projects'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-select', 'data-toggle': 'dropdown'}),
            'project': forms.SelectMultiple(attrs={'class': 'form-select', 'data-toggle': 'dropdown'}),  # Use 'project' instead of 'projects'
        }

     

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('topic', 'languages_used', 'duration')
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'languages_used': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }
