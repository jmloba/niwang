from django.shortcuts import get_object_or_404, render, redirect
from .models import Article, UserAccess
from app_booking.models import Room
from . import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.template.defaultfilters import slugify

# Create your views here.
def main_page(request):
  main_page = 'main_page'
  rooms = Room.objects.all()
  context={"main_page": main_page, 'rooms' : rooms}
  return render(request,'article/main_page.html', context) 

@login_required(login_url='accounts:login_view')
def article_list(request):
  articles = Article.objects.all().order_by('date')
  context ={ 'articles':articles}
  return render(request,'article/article_list.html', context)


@login_required(login_url='accounts:login_view')
def article_list2(request):
  articles = Article.objects.all().order_by('date')
  context ={ 'articles':articles}
  return render(request,'article/article_list2.html', context)


def article_detail(request,slug):
  article = Article.objects.get(slug=slug)
  if article:
    context={"article": article}
  else :
    print ('--->>>> no data')
    return redirect('article_list') 
  return render(request,'article/article_details.html', context)

@login_required(login_url='accounts:login_view')
def article_detail_view(request,pk=None):
  article = Article.objects.get(pk=pk)
  context = {'pk':pk, 'article':article}
  return render(request,'article/article_detail_2.html',context)

@login_required(login_url='accounts:login_view')
def article_delete(request,pk=None):
  article =get_object_or_404(Article,pk=pk)
  article.delete()
  messages.success(request,'Successfuly deleted the article')
  
  return redirect('articles:article_list')


@login_required(login_url='accounts:login_view')
def article_create(request):
  # accessing OneToOnefield
  # access rights
  u = UserAccess.objects.get(user=request.user)
  
  if u.article_create is None:
    return redirect('articles:main_page')

  if request.method=='POST':
    form = forms.CreateArticleForm(request.POST, request.FILES)

    if form.is_valid():
      instance = form.save(commit = False)
      instance.author = request.user
      instance.save()
      return redirect('articles:article_list')
    else :
      messages.info(request, form.errors)
  else:  
    form = forms.CreateArticleForm()
  context={'form': form }
  return render(request,'article/article_create.html', context) 



def home_page(request):
  home_page = 'home_page'
  context={"home_page": home_page}
  return render(request,'article/homepage.html', context) 

