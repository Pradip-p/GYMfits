from GYM.models import *
from App.models import UserInformation
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserInformationForm(forms.ModelForm):
    class Meta:
        model=UserInformation
        fields=('name','email','phone_number','address','gender','age','status')
class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields='__all__'
class TrainersForm(forms.ModelForm):
    class Meta:
        model=Trainers
        fields='__all__'
