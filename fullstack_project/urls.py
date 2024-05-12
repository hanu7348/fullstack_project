from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('current_datetime/', include('datetimeapp.urls')),
    path('datetime-offsets/', include('fourdate_timeapp.urls')),
    path('home/', include('listfruitapp.urls')),
    path('', include('portfolioapp.urls')),
    path('', include('student_course_registration_app.urls')),
    path('', include('books.urls')),
    path('', include('registration.urls')),
    
]
