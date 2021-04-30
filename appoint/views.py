from django.shortcuts import render
from .models import Doctor,City

# Create your views here.

def search_doctors(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched=searched.capitalize()
        city=City.objects.get(name=searched)
        if(not city):
            print("no city")
        else:
            print("city  matched")
            
        doctors = Doctor.objects.filter(city=city.id)
        return render (request,'search_doctors.html',{'searched':searched,'doctors':doctors})
    else:
        return render (request,'search_doctors.html',{})

def home(request):
    return render(request,'home.html')

