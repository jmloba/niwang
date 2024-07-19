import pathlib

import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
  course = models.CharField(max_length=100, null=False, blank=False)
  def __str__(self) :
    return str(self.course)
  
class Student(models.Model):
  name = models.CharField(max_length=100,)
  email = models.EmailField(max_length=50, )
  course = models.CharField(max_length=50 )
  def __str__(self) :
    return str(self.name)


class CrudUser(models.Model):
  name = models.CharField(max_length=100,blank = True)
  address = models.CharField(max_length=50, blank=True)
  age = models.IntegerField(blank=True , null = True )
  def __str__(self) :
    return str(self.name)
  
class Movie(models.Model) :
  name = models.CharField(max_length=200) 
  image = models.ImageField(upload_to='caleb_images')



class Category(models.Model) :
  name = models.CharField(max_length=50, blank = False)


  
class Product (models.Model) :
  product_number=models.CharField(max_length=50, unique=True, blank=False, null=False)
  name = models.CharField("Product Name ",max_length=50,default="no-name")
  is_active= models.BooleanField(default=True)
  



