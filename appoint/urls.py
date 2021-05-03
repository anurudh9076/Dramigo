from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home,name='home'),
    path('search_doctors',views.search_doctors,name='search-doctors'),
    path('create_doctor',views.createDoctor,name='createdoctor')
]

