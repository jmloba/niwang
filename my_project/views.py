from django.http import HttpResponse
from django.shortcuts import render,redirect


def homepage(request):
   

   return redirect('articles:main_page')

def about(request):
   return render(request,'about.html')

