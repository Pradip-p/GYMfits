from GYM.models import Registration,Schedule
from django import forms
from django.forms import ModelForm



class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'
class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields='__all__'