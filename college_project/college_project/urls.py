"""
URL configuration for college_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from app1.views import *
from app1.views import student_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',student_list, name='student_list'),
    path('add/',add_student,name='add_student'),
    path('update/<int:id>/',update_student,name='update_student'),
    path('delete/<int:id>/',delete_student,name='delete_student'),
]
