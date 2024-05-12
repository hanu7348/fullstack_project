from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    context = {'datetime': now}
    return render(request, 'current_datetime.html', context)

