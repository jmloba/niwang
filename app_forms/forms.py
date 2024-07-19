from django import forms
from .models import Student, Course,  Movie , Category, Product

class CourseForm(forms.Form):
    course = forms.CharField(label="Course", max_length=100)

class CreateStudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields= ('name','course')

class CategoryForm (forms.ModelForm)  :      
    class Meta:
        model = Category
        fields= ('name',)

        
class ProductForm(forms.ModelForm) :       
    class Meta:
        model = Product
        fields= ('product_number','name','is_active',)



class CreateStudentForm2 (forms.ModelForm):
    class Meta:
        model = Student
        fields= ['name','email','course']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'name-id',}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'email-id'}),
            'course': forms.TextInput(attrs={'class':'form-control', 'id':'course-id'}),}
        
class UploadForm(forms.ModelForm) :
    name = forms.TextInput()       
    image= forms.ImageField()
    class Meta:
        model = Movie
        fields =['name','image']

