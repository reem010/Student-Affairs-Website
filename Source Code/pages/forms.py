from django.forms import ModelForm
from django import forms
from.models import Login, Register, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=[
            'name',
            'id',
            'email',
            'phone',
            'level',
            'gpa',
            'status',
            'department',
            'gender',
            'date',    
        ]    
class UpdateForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=[
            'name',
            'id',
            'gpa',
            'level',
            'status',
            'department' ,
            
        ]   

