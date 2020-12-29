from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('security_c', views.security_c, name='security_c'),
    
   
    
    
    

]