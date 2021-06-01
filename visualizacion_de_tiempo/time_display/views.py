from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

def index(request):
    return HttpResponse("Para ver la el tiempo y la hora vaya a http://127.0.0.1:8000/time")

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "date": strftime("%A, %B %w, %Y", localtime()),
        "time2":strftime("%H:%M", localtime()),
    }
    return render(request,'index.html', context)

