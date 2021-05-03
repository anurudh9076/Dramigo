

from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home,name='home'),
    path('search_doctors',views.search_doctors,name='search-doctors'),
    path('register/<des>',views.register,name='register'),
    path('login/<des>',views.login,name='login'),
    path('logout',views.logout,name='logout'),
     path('doctor_profile',views.doctor_profile,name='doctor-profile'),
   
]

