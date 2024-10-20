from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        return super().form_valid(form)
    