from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='articles'

urlpatterns = [

  # re_path(r'^article_list$',views.article_list, name='article_list'),
  
  re_path(r'^article_list$',views.article_list, name='article_list'),  

  re_path(r'^article_create$',views.article_create, name='article_create'),
  re_path(r'^main_page$',views.main_page, name='main_page'),
  re_path(r'^home$',views.home_page, name='home_page'),

  re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail, name='article_detail'),

  path('article/detail/<int:pk>/', views.article_detail_view, name='article-detail-view'),


  path('article/delete/<int:pk>/', views.article_delete, name='article_delete'),


]