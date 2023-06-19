from django.forms import ModelForm
from .models import Event, UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    secret_key = forms.CharField(max_length=100, required=True)
    public_key = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'secret_key', 'public_key')


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        # exclude = ['user']

class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['user']

class ProfileUpdateForm(forms.ModelForm):
    secret_key = forms.CharField(max_length=100)
    public_key = forms.CharField(max_length=100)

    class Meta:
        model = UserProfile
        fields = ('secret_key', 'public_key')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
