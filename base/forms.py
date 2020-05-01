from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password1']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'  # you can put your own model forms here one by one


class AccessForm(ModelForm):
    class Meta:
        model = Access
        fields = '__all__'
        exclude = ['user', 'username', ]
