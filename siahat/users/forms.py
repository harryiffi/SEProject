from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name' ,'email', 'password1', 'password2']


class userProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('ProfilePicture','Adress', 'Age', 'City', '_type')
