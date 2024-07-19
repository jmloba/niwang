from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=30, null=True, blank=True)
  age = models.IntegerField(default=0, null=True, blank=True)
  def __str__(self):
    return str(self.user.username)
