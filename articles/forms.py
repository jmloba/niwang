from django import forms

from articles import models
from .models import UserAccess, Article
 

class CreateArticleForm(forms.ModelForm):
  class Meta :
    model = models.Article
    fields= ('title','body', 'thumb' )
    widget ={
      'title': forms.TextInput(attrs={"class":"form-control"}),
      'body': forms.Textarea(attrs={"class":"form-control"}),
      'thumb': forms.ClearableFileInput(attrs={
        'class':'form-control'
      })
    }


class UserAccessForm(forms.ModelForm):
  class Meta:
    model=UserAccess
    fields=()