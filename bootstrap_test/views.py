from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User





# Create your views here.

def flex_views(request):
    context = { }
    return render(request,'bootstrap_test/flex_views.html',context)

def empfile_create(request):
    joven =123
    context={'joven':joven}
    return render(request,'bootstrap_test/create_empfile.html', context)

