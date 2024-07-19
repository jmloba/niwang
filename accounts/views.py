from django.shortcuts import render, redirect
# from .models import Article
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CreateUserForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from articles.models import UserAccess,User
from accounts.models import UserProfile
from articles.forms import UserAccessForm
from accounts.utils import detectUser, send_verification_email

from django.utils.http import  urlsafe_base64_decode 
from django.contrib.auth.tokens import default_token_generator  

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      print(f'form is valid *****')
      user = form.save()
      login(request,user)

      # log the user in 

      return redirect('articles:article_list')
  else:  
    form = UserCreationForm()  
  context = { 'form':form}
  return render(request,'accounts/signup.html',context)

def login_view(request):
  if request.method=='POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      if 'next' in request.POST:
        return redirect(request.POST.get('next'))
      else :  
        return redirect('articles:main_page')

  else:
    form = AuthenticationForm()

  context = { 'form':form}
  return render(request,'accounts/login.html',context)

def logout_view(request):
    
  logout(request)
  return redirect('accounts:login_view')
  # if request.method=='POST':
  #   logout(request)
  #   return redirect('articles:main_page')

def register_view(request):
  form= CreateUserForm()
  if request.method =='POST':
    form= CreateUserForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    useraccessform = UserAccessForm(request.POST)
    
    if form.is_valid() :
      print(f' **** form is valid')    
      if useraccessform.is_valid() :
        print(f' **** user form is valid')    
        if profile_form.is_valid():
          print(f' **** profileuser  form is valid')    

      
          user=form.save()
          useraccess = useraccessform.save(commit=False)
          useraccess.user = user
          # useraccess.location = profile_form.cleaned_data['location']
          # useraccess.age = profile_form.cleaned_data['age']          
          useraccess.save()


          profile = profile_form.save(commit=False)
          profile.user= user 
          print(f' data taken by profile : {profile.user}')
          profile.save()
          print('*****user was saved ********')
          messages.success(request,f'account was created for {user}')

          return redirect('accounts:login_view')
        else: 
          print(f' **** profileuser  form is  not valid')    
      else:
        print(f' **** useraccess  form is  not valid')    
    
      
      


    else :
      messages.error(request,'form is not valid'  )
      return redirect('accounts:register_view')
  else:
    form = CreateUserForm()
    useraccessform = UserAccessForm()  
    profile_form = UserProfileForm()

  context={'form':form, 'useraccessform': useraccessform ,'profile_form':profile_form}

  return render(request,'accounts/register.html', context )  
  
def forgot_password(request):
  if request.method =='POST':
    email=request.POST['email']
    if User.objects.filter(email=email).exists():
      print(f'---->>>> email exitst')
      user=User.objects.get(email__exact=email)
      # send reset password email
      mail_subject= 'Reset Password' 
      email_template = 'accounts/email/reset_password_email.html'

      print('---->>>> before send verification  *************')
      send_verification_email(request,user,mail_subject,email_template)
      print('---->>>> after send verification  *************')
      messages.success(request,'We have sent you the link thru your email')
      return redirect('accounts:login_view')
    else:
      messages.success(request,'Account does not exist')
      return redirect('accounts:forgot_password') 
  
  return render(request,'accounts/forgot_password.html',  )  




''' for email activation '''

def activate(request, uidb64, token):
   # Activate the user by setting the is_active status to true
  try: 
    uid =  urlsafe_base64_decode(uidb64).decode()
    user =User._default_manager.get(pk=uid)
    
  except(TypeError,ValueError,OverflowError,User.DoesNotExist):
    user=None


  if user is not None and default_token_generator.check_token(user,token):
    user.is_active = True
    user.save()
    messages.success(request,'Congratulations, Your account is now active')
    return redirect('accounts:login_view')
  else:
    messages.error(request,'Invalid activation link')
    return redirect('accounts:login_view')

def reset_Password(request):
  if request.method =='POST':
    password1=request.POST['password1']
    password2=request.POST['password2']
    messages.info(request,f'password1:{password1}  password2 :{password2} ')
    if password1==password2:
      pk = request.session.get('uid')
      user =User.objects.get(pk=pk)
      user.set_password(password1)
      user.is_active = True
      user.save()
      messages.success(request,'Password reset successfull')
      return redirect('accounts:login_view')
    else:
      messages.success(request,'Password does not match')
      return redirect('accounts:reset_Password')

    #   user.is_active = True
    #   user.save()
    #   messages.success(request,'Congratulations, Your account is now active')
    #   return redirect('myAccount')
  return render(request,('accounts/reset_Password.html'))


def reset_Password_validate(request, uidb64, token):
  try: 
    ''' note uid is a primary key from the link'''
    uid =  urlsafe_base64_decode(uidb64).decode()
    user =User._default_manager.get(pk=uid)
  except(TypeError,ValueError,OverflowError,User.DoesNotExist):
    user=None  

  if user is not None and default_token_generator.check_token(user,token):
    request.session['uid']= uid
    messages.info(request,'Please reset you password')


    return redirect('accounts:reset_Password')
  else:
    messages.error(request,'This link has been expired')
    return redirect('accounts:login_view')


  # return render(request,('accounts/reset_Password_validate.html'))




