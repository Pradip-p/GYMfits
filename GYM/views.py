from django.shortcuts import render, HttpResponse, redirect
from GYM.models import *
from App.models import *
from django.contrib.auth.models import User
from GYM.forms import *
from django.contrib.auth import authenticate, login as dj_login
from django.conf import settings
from django.core.files.storage import FileSystemStorage



# Create your views here.
def gymadmin(request,id): 
    obj=Schedule.objects.get(pk=id)
    contex={
        'obj':obj,    
    }
    return render(request, 'gymadmin/index.html',contex)

# schedule starting
def schedule(request, id):
    data=Schedule.objects.all().prefetch_related().filter(gym__pk=id)
    trainers = Trainers.objects.all()
    schedule_form=ScheduleForm()
    request.session['gym_id']=id

    contex={
        'datas':data,
        'form':schedule_form,
        'trainers':trainers
    }
    return render(request,'gymadmin/schedule.html',contex)
def insert(request):
    if request.method=='POST':
        gym_id = request.session.get('gym_id')
        schedule_form=ScheduleForm(request.POST)
        if schedule_form.is_valid:
            schedule_form.save()
            print("data is sumited") 
        return redirect('/GYM/schedule/'+str(gym_id))

def update(request,id):
     if request.method=='POST':
        data=Schedule.objects.get(pk=id)
        data.type = request.POST.get('type')
        data.shift = request.POST.get('shift')
        data.time = request.POST.get('time')
        trainer_id =request.POST.get('trainer')
        trainer = Trainers.objects.filter(pk=trainer_id).first()
        data.trainer = trainer
        data.save()
        print('data is updated')
        return redirect('/GYM/schedule/'+str(id))
def delete(request,id):
    Schedule.objects.filter(id=id).delete()
    print('data is deleted')
    return redirect('/GYM/schedule/'+str(id))
#schedule End


#Trainer Starting
def trainer(request, id):
    data=Trainers.objects.all().prefetch_related().filter(gym__pk=id)
    #data=Trainers.objects.all()
    trainer_form=TrainersForm()
    gym_id = request.session.get('gym_id')
    contex={
        'datas':data,
        'form':trainer_form
    }
    return render(request,'gymadmin/trainer.html',contex)



def Trainer_insert(request):
    if request.method == 'POST':
        gym_id = request.session.get('gym_id')
        form= TrainersForm(request.POST)
        if form.is_valid():
            form.save()
            print('data is insert')
    return redirect('/GYM/trainer/'+str(gym_id))

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
        gym_id = request.session.get('gym_id')
        return redirect('/GYM/trainer/'+str(gym_id))
        #return redirect('trainer')

def trainer_delete(request,id):
    gym_id = request.session.get('gym_id')
    Trainers.objects.filter(id=id).delete()
    print('data is deleted')
    return redirect('/GYM/trainer/'+str(gym_id))
    #return redirect('trainer')
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
        gym_content=GymContent.objects.prefetch_related().filter(gym__pk=id).first()
        #user_id = request.session.get('user')
        #user=User.objects.get(pk=user_id)
        user_comment=Comment.objects.all().prefetch_related().filter(gym__pk=id)
        contex={
            #'user':user,
            'data':data,
            'gym':gym,
            'datas':obj,
            'ob':ob,
            'user_comment':user_comment,
            'gym_content':gym_content,
        
        }
        return  render(request, 'GYM/index.html',contex)
    elif request.method=='POST':
        message=request.POST.get('message')
        user_id = request.session.get('user')
        user = User.objects.filter(pk=user_id).first()
        gym=GymInfromation.objects.get(pk=id)
        comment=Comment(message=message,user=user,gym=gym)
        comment.save()
        print("thank you for comment")
    return redirect('/GYM/index/'+str(id))

def registration(request,id):
    if request.method=='GET':
        data=UserSchedule.objects.get(pk=24)
        contex={
            'datas':data
        }
        return render(request, 'gymadmin/registration.html', contex)
        #data=UserSchedule.objects.all().prefetch_related().filter(gym__pk=1)[0]
       # contex={
       # 'datas':data
        #} 
    

def enroll(request, schedule_id):
    user_id = request.session.get('user')
    schedule_id = schedule_id
    user = User.objects.filter(pk=user_id).first()
    schedule = Schedule.objects.filter(pk=schedule_id).first()
    us = UserSchedule(user=user,schedule=schedule)
    us.save()
    return redirect('/')

  