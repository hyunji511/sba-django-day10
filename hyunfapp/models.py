from django.db import models
class Users(models.Model):
    username = models.CharField(max_length=30, verbose_name="name")
    password = models.CharField(max_length=30, verbose_name="password")

# Create your models here.
