from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='appsample'

urlpatterns = [

  re_path(r'^todo_add/$',views.todo_add, name='todo_add'),
  path('delete/<int:pk>/',views.todo_delete, name='todo_delete'),

  
  re_path(r'^java_sample1/$',views.java_sample1, name='java_sample1'),
 
]