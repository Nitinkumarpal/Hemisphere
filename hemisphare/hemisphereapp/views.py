from .models import Contact

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login,logout, authenticate
def base(request):
    
    return render(request,'base.html')




def home(request):
    
    return render(request,'home.html')

def home(request):
    if request.method =='GET':

        return render(request ,'home.html')

    if request.method == 'POST':

        Name=request.POST.get('Name')       
        Mobile=request.POST.get('Mobile')       
        Email=request.POST.get('Email')
        Message=request.POST.get('Message')
        
    
        user=Contact(Name=Name,Mobile=Mobile,Email=Email,Message=Message,
        )
        # messages.success(request,"The user "+ request.POST['firstname']+"is Saved Succesfully..!")
        user.save()
        return render(request,'home.html')
    
    return render(request,'home.html')
