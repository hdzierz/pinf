from django.db import models
#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#from django.core.exceptions import ObjectDoesNotExist
from djangotoolbox.fields import DictField, EmbeddedModelField
from django_countries.fields import CountryField
from django.db.models.base import *
from jsonfield import JSONField

from api.logger import *
from api.django_ext import *
from api.models import *


# Create your models here.

class DataFile(Ob):
    values = JSONField()

