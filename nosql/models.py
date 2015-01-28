from django.db import models

from api.models import DataSource
from djangotoolbox.fields import DictField, EmbeddedModelField

# Create your models here.


class ObKVs(models.Model):
    name = models.CharField(max_length=255)
    values = DictField()

