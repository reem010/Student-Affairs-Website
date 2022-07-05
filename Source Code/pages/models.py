from django.db import models 
from datetime import datetime
from django.forms import modelform_factory

# Create your models here.
class Student(models.Model):
    x = [
        ('General','General'),('CS','CS'),('IS','IS'),
        ('AI','AI'),
        ('DS','DS'),
        ('IT','IT'),
    ]
    CHOICES=[
        ('male','male'),('female','female'),
    ]
    status=[
        ('active','active'),('inactive','inactive'),
    ]
    name =models.CharField(max_length = 50 )
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField(null=True)
    email = models.CharField(max_length=100,null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=1,null=True)
    phone = models.IntegerField(null=True)
    date=models.DateField(default=datetime.now,null=True)
    gender = models.CharField(max_length=7, choices=CHOICES, default='Female' ,null=True)
    status = models.CharField(max_length=10, choices=status ,default='active',null=True)
    department= models.CharField(max_length=50,blank=True,choices=x,null=True)

    def __str__(self):
        return self.name

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=14)
    def __str__(self):
        return self.username

class Register(models.Model):
    email =models.CharField(max_length=40)
    password =models.CharField(max_length=14)
    repassword =models.CharField(max_length=14)
    def __str__(self):
        return self.email


