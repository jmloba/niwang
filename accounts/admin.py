from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
  list_display=('user','age','location')
  ordering=('user',)
  list_editable =('age','location')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(UserProfile,UserProfileAdmin)