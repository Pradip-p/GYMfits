from django.shortcuts import render, HttpResponse, redirect
from GYM.models import Trainers,Schedule, Comment, Registration
from App.models import GymInfromation,UserInformation
from django.contrib.auth.models import User
from GYM.forms import RegistrationForm, ScheduleForm,UserInformationForm
from django.contrib.auth import authenticate, login as dj_login

from django.conf import settings
from django.core.files.storage import FileSystemStorage



# Create your views here.
def gymadmin(request,id ): 
    obj=Schedule.objects.get(pk=id)
    #obj=GymInfromation.objects.get(pk=id)  
    print(obj.gym.name)
    #ob=GymInfromation.objects.all().prefetch_related(User).filter(user_id=1)
    #ob=Schedule.objects.all().prefetch_related('GymInfromation').filter(gym_id=1)
    #print(ob)
    
   # print(ob)
   # print(ob.gym_id)
    contex={
        'obj':obj,
        #'ob':ob
    }
    
    return render(request, 'gymadmin/index.html',contex)

# schedule starting
def schedule(request, id):
    print(id)
    data=Schedule.objects.all().prefetch_related().filter(gym__pk=id)
    print(data)
    #data=Schedule.objects.all()
    print(data)
    for i in data:
        type=i.type
        shift=i.shift
        time=i.time
        

       
    
    schedule_form=ScheduleForm()
    contex={
        'datas':data,
        'form':schedule_form
    }
    return render(request,'gymadmin/schedule.html',contex)
def insert(request):
    if request.method == 'POST':
        form= ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            print("data is subit")
    return redirect('schedule')

   # if request.method=='POST':
       # t=Trainers.objects.get(pk=1)
        #user=Schedule(type="GYM",shift="Morning",time="4:6PM", trainer=t)
        #user.save()
        #print("data is sumited")
        #type = request.POST.get('type')
        #shift = request.POST.get('shift')
        #time = request.POST.get('time')
        #t=Trainers.objects.create(trainer=trainer)
        #trainer = request.POST.get('trainer')
        #user=Schedule()
        #user.type=type
        #user.shift=shift
        #user.time=time
        #user.trainer=trainer
        #user.save()
        #print('data is insert')
        #return redirect('schedule')

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
    return render(request,'gymadmin/trainer.html',{'datas':data })



def Trainer_insert(request):
    if request.method=='POST' and request.FILES['pic']:
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        trainer_type = request.POST.get('trainer_type')
        pic = request.FILES.get('pic')
        fs = FileSystemStorage()
        filename = fs.save(pic.name, pic)
        uploaded_file_url = fs.url(filename)
        address = request.POST.get('address')
        about = request.POST.get('about')
        user=Trainers()
        user.name=name
        user.phone_number=phone_number
        user.age=age
        user.trainer_type=trainer_type
        user.pic=pic
        user.address=address
        user.about=about
        user.save()
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
                dj_login(request,user)
                #ob=GymInfromation.objects.all().prefetch_related("User")
                #print([list(pizza.User.filter(name=dell)) for pizza in ob])
                #ob=GymInfromation.objects.all().prefetch_related(User).filter(user_id=1)
                
                return redirect('/GYM/gymadmin')
                #return render(request,'A pp/index.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
             
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:      
        return render(request, 'gymadmin/login.html') 
    #return render(request,'gymadmin/login.html')
#Index file
def index(request,id):
    if request.method=='GET':
        gym=GymInfromation.objects.get(pk=id)
        data=Schedule.objects.all().prefetch_related().filter(gym__pk=id).first()
        obj=Schedule.objects.all().prefetch_related().filter(gym__pk=id)

        #print(data.gym_id)
        #obj=Trainers.objects.all()
        contex={
            'data':data,
            'gym':gym,
            'datas':obj
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

def registration(request):
    if request.method == 'POST':
        profile_form= UserInformationForm(request.POST)
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid():
            profile=profile_form.save(commit=False)
            profile.save()
            user=register_form.save()
            user.save() 
            return redirect('/GYM/gymadmin')
            
        else:
            print('can not register')
    else:
        register_form = RegistrationForm()
        profile_form = UserInformationForm()
    registration=Registration.objects.values_list("id")
    contex={
        'register_form':register_form,
        'registration':registration,
        'profile_form':profile_form

    }
    return render(request, 'gymadmin/registration.html', contex)


         