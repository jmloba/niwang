from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Article, UserAccess


class ArticleUserAdmin(admin.ModelAdmin):
  list_display=('author','title','slug','body','date',)
  list_editable =('body',)
  ordering=('title',)

  filter_horizontal=()
  list_filter =()
  fieldsets=()

class UserAccessAdmin(admin.ModelAdmin) : 
  list_display=('user','article_create','article_delete','programmer_access','admin_only','todo_access_all','todo_rights',)

  list_editable =('article_create','article_delete','programmer_access','admin_only','todo_access_all','todo_rights',)
  ordering=('user',)

  filter_horizontal=()
  list_filter =()
  fieldsets=()


admin.site.register(Article,ArticleUserAdmin )  

admin.site.register(UserAccess,UserAccessAdmin )  