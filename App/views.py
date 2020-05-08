from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from GMS.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import auth
import datetime
from django import forms
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from .models import GymInfromation
from django.contrib.auth.decorators import login_required


# Create your views here.
#def home(request):
   # information=GymInfromation.objects.all()
    #return render(request,'GYMS/home.html',{'messages':information})
def index(request):

    information=GymInfromation.objects.all()

    return render(request,'App/index.html',{'informations':information})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
    #return render(request,'/')
 


def contact(request):
    f = ContactForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            #purpose = f.cleaned_data['purpose']
            message = f.cleaned_data['message']
            recepient = str(f['email'].value())
            send_mail(name,message, recepient,[ EMAIL_HOST_USER], fail_silently = False)
            messages.add_message(request, messages.INFO, 'Thanks for submitting your feedback.')
            return redirect('/')
    else:
        f = ContactForm()
    return render(request, 'App/contact.html', {'form': f})