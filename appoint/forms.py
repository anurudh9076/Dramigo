from django import forms
from django.forms import ModelForm
from .models import Doctor,User

class UserForm(ModelForm):
    class Meta:
        model = User
        #field = "__all__"
        fields = ('first_name', 'last_name', 'username','email','password')
        labels ={
            'first_name': '',
            'last_name': '',
            'username': '',
            'manager': '',
            'email': '',
            'password':'',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
            
        }
