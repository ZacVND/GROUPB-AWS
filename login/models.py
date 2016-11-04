from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=15)

    def name(self):
        return self.username

    class Meta:
        db_table = "users"


class Citation(models.Model):
    content = models.CharField(max_length=200, default="Null Content")

    class Meta:
        db_table = "citation"
