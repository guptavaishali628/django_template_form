from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=50)
    Cpassword=models.CharField(max_length=50)
