from django.shortcuts import redirect, render
from .forms import PhotoForms
from django.http import JsonResponse
from accounts.utils import is_ajax

# Create your views here.
def photos_main(request):
  form = PhotoForms(request.POST or None, request.FILES or None)
  data ={}
  if is_ajax(request):
    if form.is_valid():
      form.save()
      data['name'] = form.cleaned_data.get('name')
      data['status']='ok'
      return JsonResponse(data)
  
  context={'form':form,}
  
  return render(request,'app_photos/photos_main.html', context )  
