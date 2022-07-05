from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from .models import *
from django.forms import modelform_factory
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request,'projectfront/home.html')

def add(request):
    a = request.POST.get('name',False)
    b = request.POST.get('id')
    c = request.POST.get('level')
    d = request.POST.get('email')
    e = request.POST.get('gpa')
    f = request.POST.get('phone')
    g = request.POST.get('date')
    h = request.POST.get('gender')
    i = request.POST.get('status')
    j = request.POST.get('department')
    addform = Student(name=a,id=b,level=c,email=d,gpa=e,phone=f,date=g,gender=h,status=i,department=j)
    addform.save()
    context={
        'form1':addform,
        }
    return render (request,'projectfront/addstudent.html',context)

def StudentUpdate(request):
    return render (request,'projectfront/StudentUpdate.html')

def departmentt(request):
    return render (request,'projectfront/depart.html')

def allstudents(request):
    context={
    'student':Student.objects.all(),
    }
    return render (request,'projectfront/allstudents.html',context)

def changestat(request,id):
    student= Student.objects.get(id=id)
    if student.status=="active" or student.status=="active" :
        Student.objects.filter(id=id).update(status="inactive")
    else:
        Student.objects.filter(id=id).update(status="active")
    return redirect('allstudents')

def department(request,id):
    student_id = Student.objects.get(id=id)
    if request.method =='POST':
        student_save = UpdateForm( request.POST , request.FILES, instance=student_id)
        # self.UpdateForm["name"].disabled = True
        if student_save.is_valid():
            student_save.save()
            return redirect('search')        
    else:
        student_save =UpdateForm(instance=student_id)
    context={
        'form': student_save,
    }
    return render (request, 'projectfront/depart.html' , context)

def login(request):
    a = request.POST.get('username',False)
    b = request.POST.get('password',False)
    loginform=Login(username=a,password=b)
    loginform.save()
    context = {"form1": loginform,}
    return render (request,'projectfront/login.html',context)

def register(request):
    a = request.POST.get('email',False)
    b = request.POST.get('password',False)
    c = request.POST.get('repassword',False)
    loginform2=Register(email=a,password=b,repassword=c)
    loginform2.save()
    context = {"form1": loginform2,}
    return render (request,'projectfront/register.html',context)

def outer(request):
    return render (request,'projectfront/outerpage.html')


def search(request):
    context={
    'student':Student.objects.all(),
    }
    return render (request,'projectfront/search.html',context)

def update(request,id):
    student_id = Student.objects.get(id=id)
    if request.method =='POST':
        student_save = StudentForm( request.POST , request.FILES, instance=student_id)
        if student_save.is_valid():
            student_save.save()
            return redirect('allstudents')        
    else:
        student_save =StudentForm(instance=student_id)
    context={
        'form': student_save,
        
    }
    return render(request,'projectfront/StudentUpdate.html',context)

def delete(request,id):
    context={
        
    }
    student_delete=get_object_or_404(Student , id = id)
    if request.method=='POST':
        student_delete.delete()
        return redirect('allstudents')
    
    return render(request,'projectfront/delete.html', context)


