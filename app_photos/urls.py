from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='app_photos'

urlpatterns = [
 
  re_path(r'^photos_main/$',views.photos_main, name='photos_main'),
 

]
