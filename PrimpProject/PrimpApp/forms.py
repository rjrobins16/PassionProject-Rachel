from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User


class NewUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class SignInForm(ModelForm):

     password = forms.CharField(widget=forms.PasswordInput)
     class Meta:
             model = User
             fields = ['username', 'password']
