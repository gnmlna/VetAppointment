from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

from myapp.forms import PatientForm  
from .models import Patient 

# Create your views here.

@unauthenticated_user
def registerPage(request):
  
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html',context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            
    context = {}
    return render(request, 'login.html',context)


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'user.html',context)


def logoutUser(request):
    logout(request )
    return redirect('login')

# index
@login_required(login_url='login')
@admin_only
def home(request):

    patient = Patient.objects.all()
    context = {'patient':patient }
    return render(request, 'home.html',context)

@login_required(login_url='login')
def appointmentPage(request):
    context = {}
    return render(request, 'appointment.html',context)

def addRecord(request):
    a=request.POST['name']
    b=request.POST['phone']
    c=request.POST['email']
    d=request.POST['date']
    e=request.POST['time']
    f=request.POST['address']
    patient = Patient(name=a,phone=b,email=c,date=d,time=e,address=f)
    patient.save()
    return redirect("/")

def delete(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect("/")

def update(request,id):
    patient = Patient.objects.get(id=id)
    return render(request,'update.html',{'patient':patient})

def updateRecord(request,id):
    a=request.POST['name']
    b=request.POST['phone']
    c=request.POST['email']
    d=request.POST['date']
    e=request.POST['time']
    f=request.POST['address']
    patient = Patient.objects.get(id=id)
    patient.name=a
    patient.phone=b
    patient.email=c
    patient.date=d
    patient.time=e
    patient.address=f
    patient.save()
    return redirect("/")

def show(request):  
    patients = Patient.objects.all()  
    return render(request,"show.html",{'patients':patients})