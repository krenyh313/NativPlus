from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder':'Password Confirmation'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

