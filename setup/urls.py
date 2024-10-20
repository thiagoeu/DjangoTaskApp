
from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView, TaskUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit')
]
