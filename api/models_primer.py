# -*- coding: utf-8 -*-

from django.db import models
#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import *
from djangotoolbox.fields import DictField, EmbeddedModelField

from .logger import *
from .django_ext import *
from .models_base import *


class Primer(Category):
    def __unicode__(self):
        return self.name 


class PrimerType(Category):
    def __unicode__(self):
        return self.name


class PrimerTail(Category):
    def __unicode__(self):
        return self.name


class PrimerOb(Ob):
    primer = models.ForeignKey(Primer)
    primer_type = models.ForeignKey(PrimerType, null=True, blank=True)
    sequence = models.CharField(max_length=255)
    tail = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name


class MarkerOb(Ob):
    kea_id = models.CharField(max_length=255, db_index=True)
    ebrida_id = models.CharField(max_length=255, db_index=True)
    genotype_id = models.IntegerField(default=0, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    values = JSONField() 

    def __unicode__(self):
        return str(self.kea_id)

    def GetName(self):
        return self.study.name + '.' + str(self.kea_id) + "." + self.ebrida_id



# SIGNALS
@receiver(pre_save, sender=PrimerOb)
def set_obkeyword(sender, instance, **kwargs):
    obkw = instance.obkeywords
    if(instance.primer and instance.primer_type):
	obkw += ' ' + instance.primer.name + ' ' + instance.primer_type.name + ' ' + instance.sequence
	instance.obkeywords = obkw


