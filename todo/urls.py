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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from planner.views.home_views import HomeView
from planner.views.task_views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView
from planner.views.users_views import UserRegistrationView, ProfileUpdateView, ProfileDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name = 'home'),
    path('tasks/', TaskListView.as_view(), name = 'task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name = 'task_create'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name = 'task_detail'),
    path('tasks/<int:pk>/edit', TaskUpdateView.as_view(), name = 'task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name = 'task_delete'),
    path('profile/update/', ProfileUpdateView.as_view(), name = 'profile_update'),
    path('profile/', ProfileDetailView.as_view(), name = 'profile_detail'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'home'), name = 'logout'),
    path('register/', UserRegistrationView.as_view(), name = 'register'),
]
