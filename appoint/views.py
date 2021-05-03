from django.shortcuts import render
from .models import Doctor,City,Speciality
from .filters import DoctorFilter
from .forms import DoctorForm
# Create your views here.

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


def createDoctor(request):
    form=DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
        print("printing",request.POST)

    context = {'form':form}

    return render(request,'appoint_form.html',context)    

