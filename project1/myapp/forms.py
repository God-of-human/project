from django import forms

class NameFrom(forms.form):
    your_name = forms.CharField(label='Your name', max_length=100)