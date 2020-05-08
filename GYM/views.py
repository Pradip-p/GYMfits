from django.shortcuts import render, HttpResponse, redirect
from GYM.models import Trainers
from App.models import GymInfromation
from GYM.forms import RegistrationForm



# Create your views here.
def index(request,id):
    objects=GymInfromation.objects.all()
    for i in objects:
        if i.id==id:
            return  render(request, 'GYM/index.html',{'info':i.name})


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


         