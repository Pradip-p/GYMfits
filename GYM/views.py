from django.shortcuts import render, HttpResponse, redirect
from GYM.models import Trainers,Schedule, Comment
from App.models import GymInfromation
from GYM.forms import RegistrationForm



# Create your views here.
def index(request,id):
    if request.method=='GET':
        objects=GymInfromation.objects.all()
        for i in objects:
            if i.id==id:
                data=Schedule.objects.all()
                return  render(request, 'GYM/index.html',{'info':i.name,'datas':data})
    elif request.method=='POST':
        name=request.POST.get('name')
        print(name)
        email=request.POST.get('email')
        message=request.POST.get('message')
        user=Comment()
        user.name=name
        user.email=email
        user.message=message
        user.save()
        print("thank you for comment")
    return redirect('/')

		
		

	

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


         