from django.shortcuts import render, HttpResponse, redirect
from GYM.models import Trainers,Schedule, Comment, Registration
from App.models import GymInfromation,UserInformation
from django.contrib.auth.models import User
from GYM.forms import ScheduleForm,UserInformationForm,TrainersForm
from django.contrib.auth import authenticate, login as dj_login

from django.conf import settings
from django.core.files.storage import FileSystemStorage



# Create your views here.
def gymadmin(request,id): 
    print(id)
    obj=Schedule.objects.get(pk=id)
    contex={
        'obj':obj,    
    }
    return render(request, 'gymadmin/index.html',contex)

# schedule starting
def schedule(request, id):
    data=Schedule.objects.all().prefetch_related().filter(gym__pk=id)
    schedule_form=ScheduleForm()
    contex={
        'datas':data,
        'form':schedule_form
    }
    return render(request,'gymadmin/schedule.html',contex)
def insert(request):
    if request.method=='POST':
        schedule_form=ScheduleForm(request.POST)
        if schedule_form.is_valid:
            schedule_form.save()
            print("data is sumited") 
        print('data is insert')
        return redirect('schedule')

def update(request,id):
     if request.method=='POST':
        data=Schedule.objects.get(pk=id)
        data.type = request.POST.get('type')
        data.shift = request.POST.get('shift')
        data.time = request.POST.get('time')
        data.trainer =request.POST.get('trainer')
        data.save()
        print('data is updated')
        return redirect('schedule')
def delete(request,id):
    Schedule.objects.filter(id=id).delete()
    print('data is deleted')
    return redirect('schedule')
#schedule End


#Trainer Starting
def trainer(request, id):
    data=Trainers.objects.all().prefetch_related().filter(gym__pk=id)
    #data=Trainers.objects.all()
    schedule_form=ScheduleForm()
    contex={
        'datas':data,
        'form':schedule_form

    }
    return render(request,'gymadmin/trainer.html',contex)



def Trainer_insert(request):
    if request.method == 'POST':
        form= TrainersForm(request.POST)
        if form.is_valid():
            form.save()
            print("data is submit")
            print('data is insert')
    return redirect('trainer')

def trainer_update(request,id):
     if request.method=='POST'and request.FILES['pic']:
        data=Trainers.objects.get(pk=id)
        data.name = request.POST.get('name')
        data.phone_number = request.POST.get('phone_number')
        data.age = request.POST.get('age')
        data.trainer_type =request.POST.get('trainer_type')
        a=data.pic = request.FILES.get('pic')
        fs = FileSystemStorage()
        filename = fs.save(a.name, a)
        uploaded_file_url = fs.url(filename)
        data.address = request.POST.get('address')
        data.about = request.POST.get('about')
        data.save()
        print('data is updated')
        return redirect('trainer')

def trainer_delete(request,id):
    Trainers.objects.filter(id=id).delete()
    print('data is deleted')
    return redirect('trainer')
#Trainer End
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(username=username, password=password)
        if user:
            if user.is_staff:
                print(user.id)
                dj_login(request,user)   
                data=GymInfromation.objects.all().prefetch_related().get(user_id=user.id)  
                a=data.id
                print(type(a))
                print(a)
                print(data.name)       
                return redirect('/GYM/gymadmin/a')
            else:
                return HttpResponse("Your account was inactive.")
        else:
             
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")

    else:      
        return render(request, 'gymadmin/login.html') 
    
#Index file
def index(request,id):
    if request.method=='GET':
        gym=GymInfromation.objects.get(pk=id)
        data=Schedule.objects.all().prefetch_related().filter(gym__pk=id).first()
        obj=Schedule.objects.all().prefetch_related().filter(gym__pk=id)
        ob=Trainers.objects.all().prefetch_related().filter(gym__pk=id)
        contex={
            'data':data ,
            'gym':gym,
            'datas':obj,
            'ob':ob
        }
        return  render(request, 'GYM/index.html',contex)
    elif request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        user=Comment()
        user.name=name
        user.email=email
        user.message=message
        user.save()
        print("thank you for comment")
    return redirect('/')

def registration(request,id):
    if request.method=='GET':
        data=Registration.objects.all().prefetch_related().get(user_id=id)
        contex={
        'datas':data
        } 
    elif request.method=="POST":
        print("user is sumbmitted")
    return render(request, 'gymadmin/registration.html',contex)


         