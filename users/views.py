from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm, UserLoginForm

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        _username = request.POST['username']
        for i in User.objects.all():
            if(i.username == _username):
                return render(request, 'users/register.html', {'form': form, 'FORM_ERROR_user': "Username exists"})
        _password = request.POST['password1']
        _password2 = request.POST['password2']
        if(_password != _password2):
            return render(request, 'users/register.html', {'form': form, 'FORM_ERROR_pass': "Password doesn't match"})
        if form.is_valid():
            form.save()
            user = authenticate(request, username=_username, password=_password)
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'users/register.html', {'form': form})

def LogUserIn(request):
    form = UserLoginForm()
    if request.method == 'GET':
        return render(request, 'users/index.html', {'form': form})
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            error = "Wrong username / password"

    return render(request, 'users/index.html', {'form': form , 'LOGIN_ERROR': error})