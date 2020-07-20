from django.forms import ModelForm
from django import forms
from .models import Trip
import datetime
import random
import pytz

class TripForm(forms.ModelForm):
    CurrentLocation = forms.CharField(required=False, widget=forms.TextInput(attrs={'value': 'Current Location'}))
    Destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' ,'value': datetime.date.today}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time' ,'value': datetime.datetime.now(pytz.timezone('Asia/Jerusalem'))}))
    smoking = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onclick':'selected(3)'}))
    pets = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onclick':'selected(2)'}))
    music = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onclick':'selected(1)'}))
    passengers = forms.IntegerField(widget=forms.NumberInput(attrs={'value': 1}))

    class Meta:
        model = Trip
        fields = [  'CurrentLocation',
                    'Destination',
                    'date',
                    'time',
                    'passengers',
                    'music',
                    'pets',
                    'smoking'
                ]

class searchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'type':'search','placeholder':'Search'}))