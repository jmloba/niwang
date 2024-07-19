from django.urls import include, re_path,path
from django.contrib import admin
from . import views

app_name='accounts'

urlpatterns = [

  re_path(r'^signup/$',views.signup_view, name='signup_view'),
  
  re_path(r'^register/$',views.register_view, name='register_view'),

  re_path(r'^login/$',views.login_view, name='login_view'),
  
  re_path(r'^logout_view/$',views.logout_view, name='logout_view'),

  re_path(r'^forgot_password/$',views.forgot_password, name='forgot_password'),

  re_path(r'^reset_password/$',views.reset_Password, name='reset_Password'),

  path('reset_Password_validate/<uidb64>/<token>/', views.reset_Password_validate, name ='reset_Password_validate'), 

  
  

]