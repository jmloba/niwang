from django import forms
from .models import Todo
from . import models

class TodoForm(forms.ModelForm):
  class Meta:
    model = models.Todo
    fields =[ 'text'  ]
    widgets={ 
      'text': forms.TextInput(
            attrs={'class':'form-contol', 'placeholder': 'todo entry','aria-label':'Todo',     }
    ) }
    