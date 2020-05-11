from django.shortcuts import render, HttpResponse, redirect
from GYM.models import Trainers,Schedule, Comment
from App.models import GymInfromation
from GYM.forms import RegistrationForm



# Create your views here.
def gymadmin(request):
    
    return render(request, 'gymadmin/index.html')

# schedule starting
def schedule(request):
    data=Schedule.objects.all()
    return render(request,'gymadmin/schedule.html',{'datas':data})
def insert(request):
    if request.method=='POST':
        type = request.POST.get('type')
        shift = request.POST.get('shift')
        time = request.POST.get('time')
        trainer = request.POST.get('trainer')
        user=Schedule()
        user.type=type
        user.shift=shift
        user.time=time
        user.trainer=trainer
        user.save()
        print('data is insert')
        return redirect('schedule')
def update(request,id):
     if request.method=='POST':
        data=Schedule.objects.get(pk=id)
        print(data.type)
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
def trainer(request):
    data=Trainers.objects.all()
    return render(request,'gymadmin/trainer.html',{'datas':data })

def Trainer_insert(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        trainer_type = request.POST.get('trainer_type')
        pic = request.POST.get('pic')
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
     if request.method=='POST':
        data=Trainers.objects.get(pk=id)
        data.name = request.POST.get('name')
        data.phone_number = request.POST.get('phone_number')
        data.age = request.POST.get('age')
        data.trainer_type =request.POST.get('trainer_type')
        data.pic = request.POST.get('pic')
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

#Index file
def index(request,id):
    if request.method=='GET':
        print(id)
        gym=GymInfromation.objects.get(pk=id)
        #Schedule.objects.all().prefetch_related().filter(gym__pk=id)
        data=Schedule.objects.all()
        obj=Trainers.objects.all()
        return  render(request, 'GYM/index.html',{'info':gym.name,'datas':data,'obj':obj})

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


         