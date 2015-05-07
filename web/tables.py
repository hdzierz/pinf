# -*- coding: utf-8 -*-

#from django_tables2.utils import A  # alias for Accessor
#from django.db.models import Sum
from django_tables2_reports.tables import TableReport
import django_tables2 as tables
from api.models import *
from seafood.models import *
from genotype.models import *


class ObTable(TableReport):
    fields = []
    values = []
    sterm = '' 

    class Meta:
        attrs = {"class": "paleblue"}
        exclude = ("obkeywords", "search_index", "values", )


class SpeciesTable(TableReport):
    class Meta:
        attrs = {"class": "paleblue"}


class CategoryTable(TableReport):
    sterm = None
    class Meta:
        attrs = {"class": "paleblue"}
        exclude = ("obkeywords", "search_index",  )


class FishObTable(ObTable):

    class Meta(ObTable.Meta):
        model = FishOb


class PostHarvestSurvivalObTable(ObTable):
    class Meta(ObTable.Meta):
        model = PostHarvestSurvivalOb


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


class PrimerObTable(ObTable):
    class Meta(ObTable.Meta):
        model = PrimerOb


class MarkerObTable(ObTable):
    class Meta(ObTable.Meta):
        model = MarkerOb








