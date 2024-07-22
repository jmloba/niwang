from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Article(models.Model):
  
  title = models.CharField(max_length=100 , unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  body = models.TextField(max_length=2000)

  date = models.DateTimeField(auto_now_add=True)
  thumb= models.ImageField(default='default.jpg',null=True,blank=True,upload_to='images/')
  
  author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  def save(self,*args,**kwargs):
    self.slug = slugify(self.title)
    super().save(*args,*kwargs)
  def __str__(self):
    return self.title
  def snippet(self):
    return self.body[:300]
  
class UserAccess(models.Model):
  user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
  article_create = models.BooleanField(default=False)
  article_delete = models.BooleanField(default=False)
  programmer_access=models.BooleanField(default=False)
  admin_only=models.BooleanField(default=False)
  todo_access_all = models.BooleanField(default=False)
  todo_rights = models.BooleanField(default=False)
  send_email_trigger  = models.BooleanField(default=False)

  # location=models.CharField(max_length=30, null=True, blank=True)

  # age = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  

  def __str__(self):
    return self.user.username
  

  