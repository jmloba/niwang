from django.contrib import messages
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import  CourseForm ,CreateStudentForm2, UploadForm, CategoryForm

from .models import Student, Course , Category, Product

from django.shortcuts import get_object_or_404, render, redirect
from accounts.utils import is_ajax
from django.db import IntegrityError

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def topics(request):
  return render(request,'app_forms/topics.html'  )

def sample_course(request):
  courses = Course.objects.all()
  if request.method == 'POST':
    form_course = CourseForm(request.POST)

    if form_course.is_valid():
      course = form_course.cleaned_data['course']
      instance = Course.objects.create(course=course)
      instance.save()
      return redirect('app_forms:sample_course') 
    else:
      return redirect('app_forms:sample_course')  

  else:  
    form_course = CourseForm()
  context={'form_course':form_course,"courses":courses}
  return render(request,'app_forms/sample_course.html', context )  

def get_course(request):
  course = Course.objects.get(course=request.course) 
  return course
# ------------ --------------------------------------------------------
# product-category  --https://www.youtube.com/watch?v=5QPirQpUk74&t=4947s
# ------------ --------------------------------------------------------
def product_category(request):
  category = Category.objects.all()
  form =CategoryForm() 
  context={'category':category, 'form': form}
  return render(request,'app_forms/product_category.html', context ) 

def category_save(request):
  if request.method =='POST':
    name = request.POST['name']
    category  = Category( name=name)
    category.save()
    response ={"status":"Saved", "id":category.id,"name":category.name }
    return JsonResponse(response)
  
  else:
    response ={"status":"Not Saved"}
    return JsonResponse(response)
  

  
  
def category_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    category = Category.objects.get(pk=id)
    print(f'student to delete : {category}')
    category.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  
# ------------ --------------------------------------------------------
# cairo coders - https://www.youtube.com/watch?v=PBT6bQIBom4
# ------------ --------------------------------------------------------  
   
# ------------ --------------------------------------------------------
#desphixs CRUD AJAX
# ------------ --------------------------------------------------------
@csrf_exempt
def desphixs_start(request):
  students=Student.objects.all()
  form = CreateStudentForm2()
  context={'form': form,"students":students}
  return render(request,'app_forms/desphixs.html', context )  

@csrf_exempt
def desphixs_save_student(request):
  if request.method == "POST":  
    sid=request.POST["stuid"]  # stuid  -> from form type hidden
    name = request.POST['name']
    email = request.POST['email']
    course = request.POST['course']

    if sid =='':
      student = Student(name=name, email=email, course=course)  
    else:  
      student = Student(id=sid, name=name, email=email, course=course)
    student.save()

    student_val=Student.objects.values()
    student_data=list(student_val)



    return JsonResponse({"status": "Saved", "student_data": student_data})
  else:
    return JsonResponse({"status": "not saved"})
    
@csrf_exempt
def desphixs_delete_student(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    student = Student.objects.get(pk=id)
    print(f'student to delete : {student}')
    student.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  


  
@csrf_exempt
def desphixs_edit_student(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    student = Student.objects.get(pk=id)
    student_data = {"id":student.id , "name": student.name, "email": student.email, "course": student.course}
    print(f"----->>>  *** edit student pk: {id}")

    return JsonResponse(student_data)
  else:
    return JsonResponse({"status":"not edited"})

# ------------ --------------------------------------------------------
#caleb curry - forms

def caleb_start(request):
  if request.POST:
    form = UploadForm(request.POST, request.FILES)
    print(request.FILES)
    if form.is_valid():
      form.save()
      return redirect('app_forms:topics') 
  else:
    form=UploadForm()


  context={'form':form}
  return render(request,'app_forms/caleb_start.html', context )  

# ------------ --------------------------------------------------------
#  formset
# ------------ --------------------------------------------------------
def sample_formset(request):
  studlist = Student.objects.all()

  
  if (request.method=='POST'):
    form=CreateStudentForm2(request.POST)
    if (form.is_valid()):
      student_name =form.changed_data['name']
      student = Student.objects.create(name=student_name)
      student.save()
      return HttpResponse('Student was created : '+student_name)

  Student_Formset = formset_factory(CreateStudentForm2, extra = 1 )
  # student_formset = Student_Formset()
  student_formset = Student_Formset( initial = [{"name":'John'},{"name":'Nike'}])

  context={'formset': student_formset,"studlist": studlist}
  return render(request,'app_forms/sample_formset.html', context ) 
