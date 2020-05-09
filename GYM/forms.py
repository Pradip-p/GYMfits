from GYM.models import Registration
from django import forms
from django.forms import ModelForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')