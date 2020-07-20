from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Trip
from .forms import TripForm, searchForm
import random
import math


@login_required
def homepage(request):
    username = request.user.username
    return render(request, 'trips/Home.html', {'user': username})


@login_required
def driverlist(request):
    trips = Trip.objects.all().order_by('-pk')
    # if request.method == 'POST':
    #     ids = ['string']
    #     form = searchForm(request.POST)
    #     search = request.POST['search']
    #     for i in User.objects.all():
    #         if(i.username == search):
    #             ids.append(i.get_id())
    #     for i in ids
    #         if i is not 'string'    
    #             trips = trips.objects.filter(driver.id)

    return render(request, 'trips/DriverList.html', {'trips': trips})


@login_required
def tripinfo(request, pk=0):
    trip = get_object_or_404(Trip, id=pk)
    return render(request, 'trips/TripInfo.html', {'trip':trip})


@login_required
def updateTrip(request, pk=0):
    trip = Trip.objects.get(id=pk)
    form = TripForm(instance=trip)
    
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('/TripInfo/' + pk )

    return render(request, 'trips/NewTrip.html', {'form':form})


@login_required
def deleteTrip(request, pk=0):
    trip = Trip.objects.get(id=pk)
    if request.method == 'GET':
        # return render(request, 'Delete/' + pk)
        return render(request, 'trips/Delete.html' , {'trip':trip} )

    if request.method == 'POST':
        trip.delete()
        return redirect('home')

    return redirect('/TripInfo/' + pk )



@login_required
def createTrip(request):
    form = TripForm()
    if request.method == 'POST':
        form = TripForm(request.POST)
        form.instance.driver = request.user
        number = random.uniform(5, 10)
        form.instance.rating = round(number, 1)

        number2= random.uniform(16, 70)
        form.instance.age = math.trunc(number2)

        if form.is_valid():
            form.save()
            return redirect('driverlist')

    return render(request, 'trips/NewTrip.html', {'form':form})
    # redirect!!!