from django import forms
from .models import Photos

class PhotoForms(forms.ModelForm):
  class Meta:
    model =Photos
    fields =('image','name', 'description' )
