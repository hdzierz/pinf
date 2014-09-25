# -*- coding: utf-8 -*-

#from django_tables2.utils import A  # alias for Accessor
#from django.db.models import Sum
from django_tables2_reports.tables import TableReport
import django_tables2 as tables
from api.models import *


class ObTable(TableReport):
    class Meta:
        attrs = {"class": "paleblue"}


class CategoryTable(TableReport):
    class Meta:
        attrs = {"class": "paleblue"}


class FishObTable(ObTable):
    data = tables.Column(empty_values=())

    def render_data(self, record):
        rds = record.fishobkv_set.filter(key='Right Bruising F')
        return rds[0].value

    class Meta(ObTable.Meta):
        model = FishOb


class TripTable(CategoryTable):
    class Meta(CategoryTable.Meta):
        model = Trip


class CityTable(CategoryTable):
    class Meta(CategoryTable.Meta):
        model = City


class CrewTable(CategoryTable):
    class Meta(CategoryTable.Meta):
        model = Crew


class TowTable(CategoryTable):
    class Meta(CategoryTable.Meta):
        model = Tow













