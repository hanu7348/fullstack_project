from django.urls import path
from . import views
urlpatterns = [
    path('fourdate_timeapp/', views.fourdate_timeapp, name='fourdate_timeapp'),
]