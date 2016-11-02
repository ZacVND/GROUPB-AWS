from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)