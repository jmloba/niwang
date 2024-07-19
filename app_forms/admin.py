
from django.contrib import admin
from .models import Student, Course, CrudUser, Movie, Category, Product

class StudentAdmin(admin.ModelAdmin):
  list_display=('id','name','email','course',)
  ordering=('name',)
  list_editable =('name','email','course',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class CourseAdmin(admin.ModelAdmin):
  list_display=('course',)
  ordering=('course',)
  # list_editable =('name',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()


class CrudUserAdmin(admin.ModelAdmin):
  list_display=('name','address','age')
  ordering=('name',)
  list_editable =('name','address','age')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class CrudUserAdmin(admin.ModelAdmin):
  list_display=('name','address','age')

class MovieAdmin(admin.ModelAdmin):
  list_display=('name','image')
  ordering=('name',)
  
  filter_horizontal=()
  list_filter =()
  fieldsets=()   


class CategoryAdmin(admin.ModelAdmin):
  list_display=('name',)
  ordering=('name',)
  
  filter_horizontal=()
  list_filter =()
  fieldsets=()   

class ProductAdmin(admin.ModelAdmin):
  list_display=('product_number','name', 'is_active')
  ordering=('product_number',)
  
  filter_horizontal=()
  list_filter =()
  fieldsets=()   


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(CrudUser, CrudUserAdmin)
admin.site.register(Movie, MovieAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)