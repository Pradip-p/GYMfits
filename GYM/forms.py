from django.contrib.auth.models import User
from GYM.models import UserInformation,Registration
from django import forms
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        #fields='__all__'
        fields = ('username','password')

class UserInformationForm(forms.ModelForm):
    class Meta:
        model=UserInformation
        fields=('name','email','phone_number','address','gender','age','status','pan_number','user_type')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'