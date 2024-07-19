from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):

  user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, unique=False)  

  text=models.CharField(max_length=50, unique=False)
  complete = models.BooleanField(default = False)
  def __str__(self):
    return self.text