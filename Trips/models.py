from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    CurrentLocation = models.CharField(max_length=60)
    Destination     = models.CharField(max_length=60)
    date            = models.DateField()
    time            = models.TimeField()
    passengers      = models.IntegerField()
    smoking         = models.BooleanField()
    pets            = models.BooleanField()
    music           = models.BooleanField()
    rating          = models.FloatField(default=0)
    age             = models.IntegerField(default=0)
    driver          = models.ForeignKey(User ,null=True, on_delete=models.SET_NULL)
    objects         = models.Manager()

    def __str__(self):
        return self.driver.username