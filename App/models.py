from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

from django.contrib.auth.models import User
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


class GymInfromation(models.Model):
    name=models.CharField(max_length=20)  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    location=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='images', null=True)
    pricing=models.CharField(max_length=20)
    rating_count=models.CharField(max_length=20)
    summary=models.TextField()
    user=models.OneToOneField(User,on_delete=CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.name



    