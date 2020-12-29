from django.shortcuts import render , HttpResponse ,redirect
from home.models import Contacts
from django.contrib import messages


# Create your views here.

def index(request):
    
    return render(request,'index.html')
    
    #return HttpResponse('<em> This is Homepage </em>')

def about(request):
    
    return render(request,'about.html')
    #return HttpResponse('<em> This is about </em>')

def contacts(request):
    if request.method == "POST":
       name = request.POST.get('name')
       address = request.POST.get('address')
       number = request.POST.get('number')
       email = request.POST.get('email')
       details = request.POST.get('details')
    
       contacts = Contacts(name=name,number=number,email=email)
       contacts.save()
       
       messages.success(request, 'Your Request has been recorded')
                  
    return render(request,'contacts.html')
   



    #return HttpResponse('<em> This is contacts </em>')

def services(request):
    return render(request,'services.html')
    #return HttpResponse('<em> This is services </em>')

def security_c(request):
    return render(request,'security_c.html')

def details1(request):
     return render(request,'details1.html')

def login(request):
    return render(request,'login.html')

def security_s(request):
    return render(request,'security_s.html')

def net_p(request):
    return render(request,'net_p.html')

def web_p(request):
    return render(request,'web_p.html')
