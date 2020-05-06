from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class GymInfromation(models.Model):
    name=models.CharField(max_length=20)  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    location=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='images', null=True)
    pricing=models.CharField(max_length=20)
    rating_count=models.CharField(max_length=20)
    summary=models.TextField()
    
    def __str__(self):
        return self.name



    