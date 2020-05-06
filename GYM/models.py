from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import CASCADE

# Create your models here.
class UserInformation(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email=models.EmailField(blank=True, null=True,help_text='enter your email')
    address=models.CharField(max_length=20)
    gender=models.CharField( max_length=50,default='male',choices=(('female','female'),('male','male'),('other','other')))
    age=models.CharField(default=18, max_length=20)
    status=models.CharField(max_length=20,default='single',choices=(('single','single'),('married','married')))
    pan_number=models.CharField(max_length=100)
    user_type=models.CharField(max_length=20,choices=(('Member','member'),('GYM Owner','GYM Owner')))
    def __str__(self):

        return self.name

class Trainers(models.Model):
    name=models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    age=models.CharField(max_length=20)
    trainer_type=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='images', null=True, blank=True)
    address=models.CharField(max_length=20)
    about=models.TextField()



class Registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email=models.EmailField(blank=True, null=True,help_text='enter your email')
    address=models.CharField(max_length=20)
    gender=models.CharField( max_length=50,default='male',choices=(('female','female'),('male','male'),('other','other')))
    age=models.CharField(default=18, max_length=20)
    status=models.CharField(max_length=20,default='single',choices=(('single','single'),('married','married')))
    time=models.CharField(verbose_name='GYM Time',max_length=20,default='moring',choices=(('morning','morning'),('day','day'),('evening','evening')))
    
    def __str__(self):
        return self.first_name





#class GymInfromation(models.Model):
 #   name=models.CharField(max_length=20)  
  #  user=models.ForeignKey(on_delete=CASCADE,to=UserInformation)  
   # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #location=models.CharField(max_length=20)
    #pic=models.ImageField(upload_to='images\\', null=True)
    #pricing=models.CharField(max_length=20)
    #rating_count=models.CharField(max_length=20)
    #summary=models.TextField()
    

    #def __str__(self):
     #   return self.name

#class RatingInformation(models.Model):
#  user=models.ForeignKey(to=UserInformation, on_delete=CASCADE)
#Gname=models.ForeignKey(on_delete=CASCADE,to=GymInfromation)
##comments=models.TextField()


    