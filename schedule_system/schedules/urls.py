"""
URL configuration for schedule_system project.

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
# schedules/urls.py
# schedules/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('schedules/', views.schedule_list, name='schedule_list'),  # Страница расписания
    path('add/', views.add_schedule, name='add_schedule'),
    path('edit/<int:pk>/', views.edit_schedule, name='edit_schedule'),
    path('delete/<int:pk>/', views.delete_schedule, name='delete_schedule'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('edit_teacher/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('groups/', views.group_list, name='group_list'),
    path('add_group/', views.add_group, name='add_group'),
    path('edit_group/<int:pk>/', views.edit_group, name='edit_group'),  # Редактирование группы
    path('delete_group/<int:pk>/', views.delete_group, name='delete_group'),
    path('select_group/', views.select_group, name='select_group'),  # Выбор группы
    path('select_teacher/', views.select_teacher, name='select_teacher'),  # Выбор преподавателя
    path('group_schedule/<int:group_id>/', views.group_schedule, name='group_schedule'),  # Расписание группы
    path('teacher_schedule/<int:teacher_id>/', views.teacher_schedule, name='teacher_schedule'),  # Расписание преподавателя
]

