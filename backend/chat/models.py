import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=100, unique=True) # 사용자 이름 = email
  password = models.CharField(max_length=128) # 사용자 패스워드
  nickname = models.CharField(max_length=128)
  ranking = models.IntegerField(default=0)
  score = models.IntegerField(default=0)
  gender = models.CharField(max_length=128)
  age = models.IntegerField(default=0)
  friends = models.ManyToManyField('self', blank=True)
  
class Friend(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  nickname = models.CharField(max_length=255)

  def __str__(self):
      return self.name