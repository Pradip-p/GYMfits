from django import forms
from django.contrib.auth.models import User
from App.models import UserInformation


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   # purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))



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
