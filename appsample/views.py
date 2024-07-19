from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import  TodoForm
from django.contrib import messages, auth


from django.http import HttpResponse,JsonResponse

# Create your views here.

def todo_add(request):
  print(request.user.user.article_create)
  if request.user.user.todo_access_all:
    todos = Todo.objects.all()
  else :
    todos = Todo.objects.filter(user = request.user)


      
  # todo_3 = Todo.objects.get(pk=3)
  if request.method=='POST':
    # form = TodoForm(request.POST, instance=todo_3)
    form = TodoForm(request.POST)
    if form.is_valid():
      # form.save()
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()

      return redirect('appsample:todo_add')
  else:   
    form = TodoForm()
  
  context = {"form":form, "todos":todos}
  return render(request,'appsample/sample1.html', context)

def todo_delete(request,pk=None):
  todo =get_object_or_404(Todo,pk=pk)
  todo.delete()
  messages.success(request,'Successfuly deleted todo')

  context = {}
  return redirect('appsample:todo_add' )

def java_sample1(request):

  context = {}
  return render(request,'appsample/java_sample1.html', context)




