from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    gender = models.CharField(30)
    email = models.CharField(max_length=50)

