from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email= models.CharField(max_length=100)
    mobNum = models.CharField(max_length=100)
    profilePicture = models.ImageField(upload_to='profile_pic')
    speciality = models.ForeignKey(Speciality,null=True,on_delete=models.CASCADE)
    city = models.ForeignKey(City,null=True,on_delete=models.CASCADE)
    availability = models.BooleanField()

    def __str__(self):
        return self.name
    

