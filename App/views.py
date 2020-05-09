from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from GMS.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import auth
import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import GymInfromation,UserInformation
from django.contrib.auth.decorators import login_required
from App.forms import UserForm, UserInformationForm, ContactForm

from django.contrib.auth import authenticate, login as dj_login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text 
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage  
from django.contrib.auth.models import User





# Create your views here.
def index(request):

    information=GymInfromation.objects.all()

    return render(request,'App/index.html',{'informations':information})
def login(request):
    #return render(request, 'GYM/login.html')
    #if request.user.is_authenticated():
        #return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(username=username, password=password)
        if user:
            if user.is_active:
                dj_login(request,user)
                print(username)
                print(password)
                return redirect('/')
                #return render('/',{'username':username})
            else:
                return HttpResponse("Your account was inactive.")
        else:
             
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:      
        return render(request, 'GYM/login.html') 
            
def signup(request):
    if request.method == 'POST':
        profile_form= UserInformationForm(request.POST)
        user_form = UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            current_site = get_current_site(request)  
            mail_subject = 'Activate your account.'  
            message = render_to_string('App/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),  
                'token': account_activation_token.make_token(user),  
            })  
            to_email = profile_form.cleaned_data.get('email')  
            email = EmailMessage(  

                mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
            return redirect('login')
            
        else:
            print(user_form.errors,profile_form.errors)

           # messages.success(request, 'Account created successfully') 
    else:
        profile_form = UserInformationForm()
        user_form=UserForm() 
    return render(request, 'App/signup.html', {'user_form':user_form,'profile_form':profile_form })

def activate(request, uidb64, token):
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(id=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
   # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
        return redirect('login')
    else:  
        return HttpResponse('Activation link is invalid!')


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