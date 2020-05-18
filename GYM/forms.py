from GYM.models import Registration,Schedule
from App.models import UserInformation
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserInformationForm(forms.ModelForm):
    class Meta:
        model=UserInformation
        fields=('name','email','phone_number','address','gender','age','status')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        
        fields='__all__'
class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields='__all__'