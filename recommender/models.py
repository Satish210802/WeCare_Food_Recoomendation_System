from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     def __str__(self):
#         return f"{self.id}: {self.first_name} {self.last_name}"

class Food(models.Model):
    name = models.CharField(max_length=50)
    bf = models.IntegerField()
    lu = models.IntegerField()
    di = models.IntegerField()
    cal = models.IntegerField()
    fat = models.IntegerField()
    pro = models.IntegerField()
    sug = models.IntegerField()
    imagepath= models.CharField(default="",max_length=100)
    def __str__(self):
        return self.name
class UserList(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    mail_id1 = models.CharField(max_length=100)
    pass
