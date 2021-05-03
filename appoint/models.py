from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    #email=models.EmailField('email',unique=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(default=timezone.now)

    
    # username=models.CharField('username',unique=True,max_length=50,default="",null=False,blank=False)
    # USERNAME_FIELD='username'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()
    # def __str__(self):
    #     return self.email

    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)   

    def __str__(self):
        return self.first_name+" "+self.last_name


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
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    mobNum = models.CharField(max_length=100)
    profilePicture = models.ImageField(upload_to='profile_pic')
    speciality = models.ForeignKey(Speciality,null=True,on_delete=models.CASCADE)
    city = models.ForeignKey(City,null=True,on_delete=models.CASCADE)
    availability = models.BooleanField()

    def __str__(self):
        return self.name
    

