from GYM.models import Registration
from django import forms
from django.forms import ModelForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'