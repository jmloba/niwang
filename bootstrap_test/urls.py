from django.urls import include, re_path,path
from django.contrib import admin
from . import views


app_name='bootstrap_test'

urlpatterns = [

  re_path(r'^flex_views/$',views.flex_views, name='flex_views'),
  re_path(r'^empfile_create/$',views.empfile_create, name='empfile_create'),


]