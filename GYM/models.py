from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import CASCADE
from App.models import GymInfromation, UserInformation
from django.contrib.auth.models import User



# Create your models here.
class GymContent(models.Model):
    title=models.CharField(max_length=20)
    about=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images', null=True, blank=True)
    gym=models.ForeignKey(to=GymInfromation,on_delete=CASCADE)

class Trainers(models.Model):
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    age=models.CharField(max_length=20)
    trainer_type=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='images', null=True, blank=True)
    address=models.CharField(max_length=20)
    gym = models.ForeignKey(to=GymInfromation,on_delete=CASCADE, null=True, blank=True)
    about=models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    message=models.TextField()
    user=models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)
    gym=models.ForeignKey(to=GymInfromation, on_delete=CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Schedule(models.Model):
    type=models.CharField(max_length=20)
    shift=models.CharField( max_length=50,default='Moring',choices=(('morning','Moring'),('afternoon','Afternoon'),('evening','Evening')))
    time=models.CharField(max_length=20)
    #trainer=models.CharField(max_length=20)
    trainer=models.ForeignKey(on_delete=CASCADE,to=Trainers, null=True, blank=True)
    gym = models.ForeignKey(to=GymInfromation,on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return self.type 



class UserSchedule(models.Model):
    user=models.ForeignKey(to=User, on_delete=CASCADE,null=True, blank=True)
    schedule=models.ForeignKey(to=Schedule, on_delete=CASCADE,null=True, blank=True)
    

