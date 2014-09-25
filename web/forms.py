from django import forms

# api includes
from api.models import *


FMT_CHOICES = (('json', 'json',),
    ('yaml', 'yaml',),
    ('csv', 'csv',),
    ('html', 'html',))

RPT_CHOICES = (
    ('ibdgenotypeextract', 'ibd_genotype_extract',),
    ('ibdgenotypevariance1', 'ibd_genotype_variance',),
    )


class ReportBaseForm(forms.Form):

    fmt = forms.ChoiceField(choices=FMT_CHOICES)
    limit = forms.CharField()


class IBDGenotypeExtractForm(forms.Form):
    pass
    #fmt = forms.ChoiceField(choices=FMT_CHOICES)
    #limit = forms.CharField()
    #cohort = forms.ChoiceField(
        #choices=[(o.key, o.value)
        #for o in FormInputLookupFact.objects.filter(
            #form_lookup_ob_id=15398793)]
            #)
    #study = forms.ChoiceField(
        #choices=[(o.value, o.key)
        #for o in FormInputLookupFact.objects.filter(
            #form_lookup_ob_id=15398795)]
            #)


class IBDGenotypeVarianceForm(forms.Form):
    pass
    #fmt = forms.ChoiceField(choices=FMT_CHOICES)
    #limit = forms.CharField()
    #study = forms.ChoiceField(
        #choices=[(o.value, o.key)
        #for o in FormInputLookupFact.objects.filter(
            #form_lookup_ob_id=15398795)]
            #)