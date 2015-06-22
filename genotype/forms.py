
from django import forms
from splitjson.widgets import SplitJSONWidget
from django.forms import ModelForm
from .models import *


class PinfForm(ModelForm):
    attrs = {'class': 'special', 'size': '40'}
    obs = forms.CharField(widget=SplitJSONWidget(attrs=attrs, debug=True))
    title = "Update"

    class Meta:
        model = Marker
        fields = ['obs']


class MarkerForm(PinfForm):
    title = "Update"

    class Meta(PinfForm.Meta):
        model = Marker
        fields = ['kea_id', 'ebrida_id', 'obs']


class PrimerObForm(PinfForm):
    title = "Update"

    class Meta(PinfForm.Meta):
        model = PrimerOb

