from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='app_forms'

urlpatterns = [

  
  re_path(r'^sample_course/$',views.sample_course, name='sample_course'),
  re_path(r'^topics/$',views.topics, name='topics'),

 

  #-------- ------- ------- ------- ------- ------- 
  # foreignkey
  #-------- ------- ------- ------- ------- ------- 
  re_path(r'^product_category/$', views.product_category, name='product-category'),

  re_path(r'^category_save/$', views.category_save, name='category-save'),

  re_path(r'^category_delete/$', views.category_delete ,name='category-delete'),

  #-------- ------- ------- ------- ------- ------- 
  # desphixs
  #-------- ------- ------- ------- ------- ------- 
  re_path(r'^desphixs/$', views.desphixs_start, name='desphixs_start'),

  re_path(r'^desphixs_save_student/$', views.desphixs_save_student, name='desphixs-save-student'),

  re_path(r'^desphixs_edit_student/$', views.desphixs_edit_student, name='desphixs-edit-student'),
  re_path(r'^desphixs_delete_student/$', views.desphixs_delete_student, name='desphixs-delete-student'),
  #-------- ------- ------- ------- ------- ------- 
  # caleb curry - forms
  #-------- ------- ------- ------- ------- ------- 
  re_path(r'^caleb_start/$', views.caleb_start, name='caleb-start'),


  #-------- ------- ------- ------- f
  # form sets
  #  https://www.youtube.com/watch?v=X9KPahGEG24&list=PLaUQIPIyD0z43DiRKM0x8YNEB-1QNCOwR&index=3
  #-------- ------- ------- ------- ------- ------- 

  re_path(r'^sample_formset/$', views.sample_formset, name='sample-formset'),


]