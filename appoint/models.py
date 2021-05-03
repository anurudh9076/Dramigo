from django.db import models
#from django.contrib.auth.models import User
from accounts.models import CustomUser

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
    age = models.IntegerField()
    mobNum = models.CharField(max_length=100)
    profilePicture = models.ImageField(upload_to='image')
    speciality = models.ForeignKey(Speciality,null=True,on_delete=models.CASCADE)
    city = models.ForeignKey(City,null=True,on_delete=models.CASCADE)
    availability = models.BooleanField()
    author=models.ForeignKey(CustomUser,default=None,on_delete=models.CASCADE)

    #def __str__(self):
     #   return self.name
    

class placeOrder(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Running','Running'),
        ('Done','Done'),
    )    
    customer = models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.doctor.mobNum

