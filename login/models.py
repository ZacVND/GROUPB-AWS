from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.
class User(models.Model):
    # objects = UserManager()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Citation(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)