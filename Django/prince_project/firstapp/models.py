from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_name = models.CharField(max_length=100)
    Emp_Email = models.EmailField()
    Emp_Mobile = models.IntegerField()
def __str__ (self):
    return self().Emp_name    

class User_Profile(models.Model):
    User_name = models.CharField(max_length=100)
    User_pass = models.CharField(max_length= 100 , default="")
    User_Email = models.EmailField()
    User_Mobile = models.IntegerField()
    User_Address = models.CharField(max_length=100)

class Blog(models.Model):
    btext = models.CharField(max_length=100)
    bdate = models.CharField(max_length=20)
    btime = models.CharField(max_length=20)
    bimage = models.ImageField(upload_to="image")
