from django.shortcuts import render
from .models import Task



# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks' : tasks})