from django.db import models
#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#from django.core.exceptions import ObjectDoesNotExist
from django_countries.fields import CountryField
from django.db.models.base import *

from .logger import *
from .django_ext import *
from .models_base import *


class Trip(Category):
    user = models.CharField(max_length=10)
    method = models.CharField(max_length=255)
    trip_no = models.IntegerField()
    species = models.ForeignKey(Species)
    vessel = models.CharField(max_length=255)
    registration = models.IntegerField()
    country = CountryField()
    captain = models.CharField(max_length=100)
    first_sailing = models.DateField()
    last_arrival = models.DateField()
    deleted = models.CharField(1)


class Crew(Category):
    crew_name = models.CharField(max_length=100)


class FishOb(Ob):
    val = None

    class Meta(Ob.Meta):
        pass

