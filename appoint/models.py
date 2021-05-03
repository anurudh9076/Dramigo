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
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True,blank=True)
    mobNum = models.CharField(max_length=100,blank=True)
    profilePicture = models.ImageField(upload_to='profile_pic/',blank=True,null=True)
    speciality = models.ForeignKey(Speciality,null=True,on_delete=models.CASCADE,blank=True)
    city = models.ForeignKey(City,null=True,on_delete=models.CASCADE,blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + " " +self.user.last_name
    

