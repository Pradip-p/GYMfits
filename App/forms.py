from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
   # purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))

