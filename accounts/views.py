from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import CustomUser
#from . import forms
# Create your views here.
def register(request):
     if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            pwd=request.POST['password1']
            cnfrm_pwd=request.POST['password2']
            type_of_user=request.POST['Type']
            if username=='' or first_name=='' or email=='':
                  messages.info(request,'Please Fill All The Details')
                  #return redirect('register')
                  
            if pwd==cnfrm_pwd:
                  if CustomUser.objects.filter(username=username).exists():
                        messages.info(request,'username taken')
                        return redirect('register')    
                  elif CustomUser.objects.filter(email=email).exists():
                        messages.info(request,'email exists already')
                        return redirect('register')
                  else:
                         if type_of_user=='doctor' :
                            user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pwd,is_customer=False)
                            user.save()
                         else:
                            user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pwd,is_customer=True)
                            user.save()   

            else:
                  messages.info(request,"password didn't matched")   
                  return redirect('register')              
            return redirect('login')     
            
            
     else:      
             return render(request,'register.html')

def login(request):
    if request.method=='POST':
           username=request.POST['username']
           pwd=request.POST['password1']
           user=auth.authenticate(username=username,password=pwd)

           if user is not None: 
                if user.is_customer==False:
                       return redirect('register')
                auth.login(request,user)
                return redirect('/')
           else  :
                messages.info(request,'Invalid Details')
                return redirect('login')
    else:
           return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')    