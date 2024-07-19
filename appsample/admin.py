from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Todo



class TodoAdmin(admin.ModelAdmin):

  list_display=('user','text',)
  # list_editable =('text',)
  ordering=('-user',)

  filter_horizontal=()
  list_filter =()
  fieldsets=()


admin.site.register(Todo,TodoAdmin )  
