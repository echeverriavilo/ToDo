"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from planner.views import (HomeView, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('tasks/', TaskListView.as_view(), name = 'task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name = 'task_create'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name = 'task_detail'),
    path('tasks/<int:pk>/edit', TaskUpdateView.as_view(), name = 'task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name = 'task_delete'),
    path('accounts/', include('django.contrib.auth.urls'))
]
