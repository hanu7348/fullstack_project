from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student,Project
from .forms import StudentForm, CourseForm,ProjectForm
from django.views.generic import ListView, DetailView

from .models import Course, Student, Project
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    courses = Course.objects.all()
    projects = Project.objects.all()
    students = Student.objects.all()
    return render(request, 'registration/index.html', {
        'courses': courses,
        'projects': projects,
        'students': students,
    })

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'registration/register_student.html', {'form': form})

def register_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'registration/register_course.html', {'form': form})

def student_list(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'registration/student_list.html', {'students': students, 'course': course})

def register_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            # Redirect to a success page or another view
            return redirect('index')
            #return redirect('project_detail', project_id=project.pk)

    else:
        form = ProjectForm()
    return render(request, 'registration/register_project.html', {'form': form})



def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'registration/project_details.html', {'project': project})



def project_student_list(request, project_id):
    project = Project.objects.get(id=project_id)
    students = project.students.all()
    return render(request, 'registration/student_list.html', {'students': students, 'project': project})


def student_list_new(request):
    students = Student.objects.all()
    return render(request, 'registration/stu_list.html', {'students': students})

class StudentListView(ListView):
    model = Student
    template_name = 'registration/stu_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'registration/student_detail.html'
    context_object_name = 'student'


from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def search_students(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        query = request.GET.get('query', '')
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
        results = []
        for student in students:
            student_data = {
                'id': student.id,
                'name': f"{student.first_name} {student.last_name}",
                'email': student.email,
                'courses': [course.name for course in student.courses.all()]
            }
            results.append(student_data)
        return JsonResponse({'results': results})
    return render(request, 'registration/search.html')