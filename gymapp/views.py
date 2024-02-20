from django.shortcuts import render,HttpResponse,redirect
from.models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import *

def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def account(request):
    return render(request,"account.html")
def classes(request):
    return render(request,"classes.html")
def contact(request):

    if request.method=='POST':
       nm=request.POST.get('name')
       eml=request.POST.get('email')
       sub=request.POST.get('subject')
       msg=request.POST.get('message')
       print(" ",nm,eml,sub,msg)
       
       user = Contact(name=nm, email=eml, subject=sub, message=msg)
       user.save()

    return render(request,"contact.html")

def Loginuser(request):
    if request.method=='POST':
        
        eml = request.POST.get('usr')
        pwd = request.POST.get('pwd')

        user = authenticate(request, username=eml, password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'login.html',{})



def Signup(request):
    frm = UserCreationForm()
    if request.method=='POST':
        frm=UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect ('login')
    return render(request,"signup.html",{'fm':frm})


def photo(request):
    return render(request,"photo.html")

def logoutUser(request): 
     logout(request) 
     return redirect('login')

def service(request): 
    #  services=Service.objects.all() 
    # services=service.objects.all()
    services=Service.objects.all().order_by('-service_title') [1:3]
    if request.method=="GET": 
         st=request.GET.get('servicename') 
         if st!=None: 
             
    
              services=Service.objects.filter(service_title__icontains=st) 
    data={ 
          "ser":services 
     } 
      
    return render(request,"service.html",data)
