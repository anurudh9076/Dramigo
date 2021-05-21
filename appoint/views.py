from django.shortcuts import render,redirect
from .models import Doctor,City,Speciality,Appointment,Slots
from .filters import DoctorFilter
from .forms import UserForm,User,DoctorForm,AppointmentForm
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.
def appoint(request):
    #doctor=Doctor.objects.get(id=doctor_id)
    if request.method=='POST':
        slot=Slots.objects.get(id=int(request.POST['slot']))
        date=request.POST['date']
        doctor_id=request.POST['doctor_id']

        doctor_id=int(doctor_id)
        doctor =Doctor.objects.get(id=doctor_id)
        print(doctor_id)
        appointment=Appointment.objects.create(slot=slot,date=date,doctor=doctor,status='pending')
        appointment.save()
        print("appointment created")
        return render (request,'make_appointment.html')

    return redirect('/')

def make_appointment(request,doctor_id):
    dated=False
    if(request.method=='POST'):
        dated=True
        date=request.POST['date']
        doctor=Doctor.objects.get(id=doctor_id)
        slots=doctor.slots.all()
        pre_appointment=Appointment.objects.filter(doctor=doctor.id,date=date)
        pre_slosts = []
        slots=list(slots)
        for ap in pre_appointment:
            slots.remove(ap.slot)
            #pre_slosts=pre_slosts.append(ap.slot)                
        
        # for slot in all_slots :
        #     if slot not in pre_slosts:
        #         slots=slots.append(slot)

        return render(request,'make_appointment.html',{'slots':slots,'dated':dated,'date':date,'doctor':doctor})
    else:
        return render(request,'make_appointment.html',{'dated':dated})



def doctor_profile(request):
    user=request.user
    if not user.is_doctor:
        redirect('home')
    doctor=Doctor.objects.get(user=user.id)
    form = DoctorForm(request.POST or None,request.FILES or None,instance=doctor)
    form1=  UserForm(instance=user)
    if form.is_valid():
        form.save()
        messages.info(request,'Details Updated Successfully')
        return redirect('doctor-profile')

    return render (request,'doctor_profile.html',{'form':form,'user':user,'form1':form1})

    



def login(request,des):
    if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      print(username)
      print(password)
      if(des == 'patient'):
          user = auth.authenticate(username=username,password=password)
          if (user is not None) and (user.is_patient == True):
              auth.login(request,user)
              return redirect('/')
          else:
              messages.info(request,'Credentials not matched')
              return redirect('login',des)
      elif(des == 'doctor'):
          user = auth.authenticate(username=username,password=password)
          if (user is not None) and (user.is_doctor == True):
              auth.login(request,user)
              return redirect('/')
          else:
              messages.info(request,'Credentials not matched')
              return redirect('login',des)  
      
      else:
          messages.info(request,'Credentials not matched')
          return redirect('login',des)
    else:
      return render(request,'login.html')
   


def register(request,des):
    submitted =False
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']    
        
        if password1==password2 :
         if User.objects.filter(username=username).exists():
            messages.info(request,'Username is taken')
            return redirect('register',des)
         elif User.objects.filter(email=email).exists():
            messages.info(request,'email is taken')
            return redirect('register',des)
         else:  
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            user=User.objects.get(username=request.POST['username'])
            if(des =='doctor'):
                user.is_doctor=True
                user.save()
                doctor=Doctor.objects.create(user=user)
                doctor.save()

            elif(des == 'patient'):
                print('hi_pat')
                user.is_patient=True
                user.save()
            messages.info(request,'Successfully Registered')
            return redirect('login',des)
        else:
            messages.info(request,'password is not matching')
            return redirect('register',des)
           
        
        return redirect('login',des)
    else: 
        form= UserForm
        if 'submitted' in request.GET:
            submitted =True        
        return render(request,'register.html',{'form':form,'submitted':submitted})

def logout(request):
   auth.logout(request)
   return redirect('/')


        
def search_doctors(request):
    
    if request.method == "POST":
        if(request.POST['city'] == "select a city" and request.POST['speciality']=='select a speciality'):
            return render (request,'search_doctors.html',{'searched':False})
        elif(request.POST['speciality']=='select a speciality'):
            city=City.objects.get(name=request.POST['city'])
            doctors = Doctor.objects.filter(city=city.id)
        elif(request.POST['city'] == 'select a city'):
            speciality= Speciality.objects.get(name=request.POST['speciality'])
            doctors = Doctor.objects.filter(city=speciality.id)
        else:
            city=City.objects.get(name=request.POST['city'])
            speciality= Speciality.objects.get(name=request.POST['speciality'])
            doctors = Doctor.objects.filter(city=city.id,speciality=speciality.id)

        return render (request,'search_doctors.html',{'doctors':doctors,'searched':True})
    else:
        return render (request,'search_doctors.html',{})

def home(request):
    cities =City.objects.all()
    sps = Speciality.objects.all()
    return render(request,'home.html',{'cities':cities,'sps':sps})

