import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from django.contrib.auth.models import User
from  .models import Trip

class searchFilter(django_filters.FilterSet):
	class Meta:
		model = Trip
		fields = ['driver']
