from django.shortcuts import render, HttpResponse, redirect
from GYM.models import UserInformation, Trainers
from App.models import GymInfromation
from GYM.forms import UserForm, UserInformationForm,RegistrationForm
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
def index(request,id):
    objects=GymInfromation.objects.all()
    for i in objects:
        if i.id==id:
            return  render(request, 'GYM/index.html',{'info':i.name})

    #objects=GymInfromation.objects.get(id=10)

    #objects1=GymInfromation.objects.all()
    
    #contex={
       # 'obj':objects,
   # }

    #return  render(request, 'GYM/index.html',{'info':objects})

def registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user=register_form.save()
            user.save() 
            return redirect('/')
            
        else:
            print('can not register')
    else:
        register_form = RegistrationForm()
    return render(request, 'GYM/registration.html', {'register_form':register_form })


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
                return redirect('/admin')
                #return redirect('profile')
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
            message = render_to_string('GYM/acc_active_email.html', {  
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
    return render(request, 'GYM/signup.html', {'user_form':user_form,'profile_form':profile_form })

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



def gymadmin(request):
    obj=UserInformation.objects.all()
    return render(request, 'gymadmin/index.html',{ 'info':obj })         