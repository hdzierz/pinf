from django.db import models
#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#from django.core.exceptions import ObjectDoesNotExist
from djangotoolbox.fields import DictField, EmbeddedModelField
from django_countries.fields import CountryField
from django.db.models.base import *
from jsonfield import JSONField

from .logger import *
from .django_ext import *
from .models_base import *


class Trip(Ob):
    orig_trip_id = models.IntegerField()
    user = models.CharField(max_length=10, null=True, blank=True, default=None)
    method = models.CharField(max_length=255, null=True, blank=True, default=None)
    trip_no = models.IntegerField()
    species = models.ForeignKey(Species)
    vessel = models.CharField(max_length=255, null=True, blank=True, default=None)
    registration = models.IntegerField(null=True, blank=True, default=None)
    country = CountryField(null=True, blank=True, default=None)
    captain = models.CharField(max_length=100, null=True, blank=True, default=None)
    first_sailing = models.DateTimeField(blank=True, null=True, default=None)
    last_arrival = models.DateTimeField(blank=True, null=True, default=None)
    deleted = models.CharField(max_length=1, null=True, blank=True, default='N')

    @staticmethod
    def GetByOrigId(oid):
        try:
            return Trip.objects.get(orig_trip_id=oid)
        except Exception:
            return None

    def __unicode__(self):
        return self.name


class City(Category):
    orig_city_id = models.IntegerField()

    @staticmethod
    def GetByOrigId(oid):
        try:
            city, created = City.objects.get_or_create(orig_city_id=oid)
            return city
        except Exception:
            return None

    def __unicode__(self):
        return self.name


class Crew(Category):
    deleted_flag = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name



class Tow(Ob):
    deleted_flag = models.BooleanField(default=False)
    city = models.ForeignKey(City)
    trip = models.ForeignKey(Trip)
    sample_count = models.IntegerField()
    treatments = models.ManyToManyField(Treatment)
    sampler = models.CharField(max_length=10)
    sample_method = models.ForeignKey(SampleMethod)
    sample_location = models.CharField(max_length=255)
    ph_instrument = models.CharField(max_length=255, null=True, default=None)
    instruments = models.ManyToManyField(Instrument)
    external_assessment_only = models.CharField(max_length=20, null=True, default=None)
    no_comment = models.CharField(max_length=255, null=True, default=None)
    comment = models.TextField(null=True, default=None)
    date_on_deck = models.DateTimeField(null=True, default=None)


class FishScore(Category):
    values = JSONField(max_length=100)
    group = models.CharField(max_length=100)
    
    def GetValue(group, name):
        try:
            return FishScore.objects.filter(Q(name=name) & Q(group=group))
        except:
            pass

    def __unicode__(self):
        return self.name


class FishOb(Ob):
    form_completed = models.BooleanField(default=False)
    trip = models.ForeignKey(Trip)
    city = models.ForeignKey(City)
    values = JSONField() 

    def __unicode__(self):
        return str(self.name)

    def GetName(self):
        return self.study.name + '.' + self.trip.name + '.' + str(self.name)

    def SaveKV(self, key, value):
        if key:
            if not type(self.values) == 'dict':
                self.values = {}
            self.values[key] = value

    def SaveKVs(self, lst):
        for key, value in list(lst.items()):
            self.SaveKV(key, value)

    def GetColumns(self):
        try:
            return list(self.values.keys())
        except:
            return ()

    #Townr
    #Sample Number
    #Species
    #Date Time
    #Iki Time
    #Location
    #Iki
    #Measurement Method
    #Length
    #Rigor
    #Texture
    #Weight
    #Scale Loss
    #Scale Removal
    #Twitch Present
    #Twitch Whole Body
    #Twitch Half Body
    #Twitch Fins
    #Twitch Gill/Jaw
    #Twitch Intensity
    #Left Muscle Temp
    #Right Muscle Temp
    #Core Temp
    #Left Dorsal Colour type
    #Left Dorsal Colour 1
    #Left Dorsal Colour 2
    #Left Dorsal Colour Intensity
    #Left Dorsal Iridescence Colour 1
    #Left Dorsal Iridescence Colour 2
    #Left Dorsal Iridescence Intensity
    #Left Ventral Colour type
    #Left Ventral Colour 1
    #Left Ventral Colour 2
    #Left Ventral Colour Intensity
    #Left Ventral Iridescence Colour 1
    #Left Ventral Iridescence Colour 2
    #Left Ventral Iridescence Intensity
    #Right Dorsal Colour type
    #Right Dorsal Colour 1
    #Right Dorsal Colour 2
    #Right Dorsal Colour Intensity
    #Right Dorsal Iridescence Colour 1
    #Right Dorsal Iridescence Colour 2
    #Right Dorsal Iridescence Intensity
    #Right Ventral Colour type
    #Right Ventral Colour 1
    #Right Ventral Colour 2
    #Right Ventral Colour Intensity
    #Right Ventral Iridescence Colour 1
    #Right Ventral Iridescence Colour 2
    #Right Ventral Iridescence Intensity
    #Left Pectoral Fin Tearing	
    #Left Pectoral Fin Bruising
    #Left Pelvic Fin Tearing
    #Left Pelvic Fin Bruising
    #Tail Fin Tearing
    #Tail Fin Bruising
    #Anal Fin Tearing
    #Anal Fin Bruising
    #Dorsal Fin Tearing
    #Dorsal Fin Bruising
    #Right Pectoral Fin Tearing
    #Right Pectoral Fin Bruising
    #Right Pelvic Fin Tearing
    #Right Pelvic Fin Bruising	
    #Left Eye Too Damaged
    #Left Eye Cornea Colour
    #Left Eye Pupil Colour
    #Left Eye Form
    #Left Eye Cold/Osmotic
    #Left Eye Bleeding
    #Left Eye Bubbles
    #Left Eye Bulging
    #Left Eye Primary Colour
    #Left Eye Secondary Colour
    #Right Eye Too Damaged
    #Right Eye Cornea Colour
    #Right Eye Pupil Colour
    #Right Eye Form
    #Right Eye Cold/Osmotic
    #Right Eye Bleeding
    #Right Eye Bubbles
    #Right Eye Bulging
    #Right Eye Primary Colour
    #Right Eye Secondary Colour
    #Left Gill Plate Scrapes
    #Left Gill Flaring
    #Left Gill Mucus
    #Left Gill Debris
    #Left Gill Colour
    #Right Gill Plate Scrapes
    #Right Gill Flaring
    #Right Gill Mucus
    #Right Gill Debris	Right Gill Colour
    #Sex
    #Gonad Condition
    #Gonad Weight
    #Liver Colour 1
    #Liver Colour 2
    #Liver Weight
    #Swim Bladder Ruptured
    #Swim Bladder Rupture Position
    #Swim Bladder Rupture Size	Kidney Ruptured
    #Parasite 1 Location
    #Parasite 1 Type
    #Parasite 2 Location
    #Parasite 2 Type
    #Parasite 3 Location
    #Parasite 3 Type
    #Parasite 4 Location
    #Parasite 4 Type
    #Heart Function
    #Atrium Intact
    #Heart Weight
    #Stomach Weight Full
    #Stomach Weight Empty
    #Spleen Weight
    #Stomach Contents
    #GI Contents
    #Otolith Sample
    #DNA Sample	Left Fat Line
    #Left Free Blood
    #Left Blood Spot A
    #Left Blood Spot B
    #Left Blood Spot C
    #Left Blood Spot D
    #Left Blood Spot E
    #Left Blood Spot F
    #Left Blood Spot G
    #Left Blood Spot H
    #Left Bruising A
    #Left Bruising B
    #Left Bruising C
    #Left Bruising D
    #Left Bruising E
    #Left Bruising F
    #Left Bruising G
    #Left Bruising H
    #Left Gaping V2
    #Left Gaping V1
    #Left Gaping D1
    #Left Gaping D2
    #Left Gaping D3
    #Left Gaping D3D2
    #Left Gaping D2D1
    #Left Gaping D1V1
    #Left Gaping V1V2
    #Right Fat Line
    #Right Free Blood
    #Right Blood Spot A
    #Right Blood Spot B
    #Right Blood Spot C
    #Right Blood Spot D
    #Right Blood Spot E
    #Right Blood Spot F
    #Right Blood Spot G
    #Right Blood Spot H
    #Right Bruising A
    #Right Bruising B
    #Right Bruising C
    #Right Bruising D
    #Right Bruising E
    #Right Bruising F
    #Right Bruising G
    #Right Bruising H
    #Right Gaping V2
    #Right Gaping V1
    #Right Gaping D1
    #Right Gaping D2
    #Right Gaping D3
    #Right Gaping D3D2
    #Right Gaping D2D1
    #Right Gaping D1V1
    #Right Gaping V1V2
    #Left Fillet Colour Even
    #Left Fillet Colour Patchy
    #Left Fillet Colour Striped
    #Left Fillet Primary Colour
    #Left Fillet Secondary Colour
    #Left Fillet Pinking
    #Left Fillet Texture
    #Left Fillet Sticky
    #Left Fillet Wet
    #Left Fillet Moist
    #Left Fillet Dry
    #Left Fillet Greasy
    #Left Fillet Torry 1
    #Left Fillet Torry 2
    #Left Fillet Torry 3
    #Left Fillet pH
    #Left Fillet Twitch
    #Left Fillet Twitch Location
    #Left Fillet Twitch Intensity
    #Left Fillet Iridescence
    #Right Fillet Colour Even
    #Right Fillet Colour Patchy
    #Right Fillet Colour Striped
    #Right Fillet Primary Colour
    #Right Fillet Secondary Colour
    #Right Fillet Pinking
    #Right Fillet Texture
    #Right Fillet Sticky
    #Right Fillet Wet
    #Right Fillet Moist
    #Right Fillet Dry
    #Right Fillet Greasy
    #Right Fillet Torry 1
    #Right Fillet Torry 2
    #Right Fillet Torry 3
    #Right Fillet pH
    #Right Fillet Twitch
    #Right Fillet Twitch Location
    #Right Fillet Twitch Intensity
    #Right Fillet Iridescence

    class Meta(Ob.Meta):
        pass


def calc_external_twitch(ob):
    twitch_intensity = GetKV(ob, 'Twitch Intensity')
    
    targets = ['Twitch Whole Body', 'Twitch Half Body', 'Twitch Fins', 'Twitch Gill/Jaw']

    res = 0

    for target in targets:
        try:
            yn = GetKV(ob, target)
            if(yn.lower() == 'yes'):
                vfbo = FishScore.objects.get(Q(group='External Twitch') & Q(name=target))
                vfb = vfbo.values[twitch_intensity.lower()]
                res += vfb
        except:
            pass

    return res


def calc_fin_score(ob):
    targets_tearing = [
        'Left Pectoral Fin Tearing', 
        'Left Pelvic Fin Tearing', 
        'Tail Fin Tearing',
        'Anal Fin Tearing',
        'Dorsal Fin Tearing',
        'Right Pectoral Fin Tearing',
        'Right Pelvic Fin Tearing',
    ]

    targets_bruising = [
        'Left Pectoral Fin Bruising',
        'Left Pelvic Fin Bruising',
        'Tail Fin Bruising',
        'Anal Fin Bruising',
        'Dorsal Fin Bruising',
        'Right Pectoral Fin Bruising',
        'Right Pelvic Fin Bruising',
    ]

    res = 0

    for target in targets_tearing:
        try:
            score = FishScore.objects.get(Q(group='Fin score') & Q(name='damage severity tearing'))
            score_category = GetKV(ob, target)
            
            score = score.values[score_category.lower()]
            res += score
        except:
            pass

    for target in targets_bruising:
        try:
            score = FishScore.objects.get(Q(group='Fin score') & Q(name='damage severity bruising'))
            score_category = GetKV(ob, target)
            score = score.values[score_category.lower()]
            res += score
        except:
            pass

    return res


def calc_lhs_eye_score(ob):
    scores = FishScore.objects.filter(group='LHS eye score')
    res = 0

    for score in scores:
        val = GetKV(ob, score.name)
        sc = score.values[val.lower()]
        res += sc
        
    return res


def calc_rhs_eye_score(ob):
    scores = FishScore.objects.filter(group='RHS eye score')
    res = 0

    for score in scores:
        try:
            val = GetKV(ob, score.name)
            sc = score.values[val.lower()]
            res += sc
        except:
            pass

    return res


def calc_lhs_fillet_score(ob):
    scores = FishScore.objects.get(Q(group='LHS Fillet score') & Q(name='yes no'))
    targets = [
                'Left Blood Spot A',
                'Left Blood Spot B',
                'Left Blood Spot C',
                'Left Blood Spot D',
                'Left Blood Spot E',
                'Left Blood Spot F',
                'Left Blood Spot G',
                'Left Blood Spot H',
        ]

    res = 0

    for bloodspot in targets:
        try:
            val = GetKV(ob, bloodspot.name)
            sc = scores.values[val]
            res += sc
        except:
            pass


    scores = FishScore.objects.get(Q(group='LHS Fillet score') & Q(name='intensity'))
    targets = [
        'Left Gaping V2',
        'Left Gaping V1',
        'Left Gaping D1',
        'Left Gaping D2',
        'Left Gaping D3',
        'Left Gaping D3D2',
        'Left Gaping D2D1',
        'Left Gaping D1V1',
        'Left Gaping V1V2',

    ]   

    for gaping in targets:
        val = GetKV(ob, gaping)
        sc = scores.values[val.lower()]
        res += sc

    return res

def calc_rhs_fillet_score(ob):
    scores = FishScore.objects.get(Q(group='RHS Fillet score') & Q(name='yes no'))
    targets = [
                'Right Blood Spot A',
                'Right Blood Spot B',
                'Right Blood Spot C',
                'Right Blood Spot D',
                'Right Blood Spot E',
                'Right Blood Spot F',
                'Right Blood Spot G',
                'Right Blood Spot H',
        ]

    res = 0

    scores = FishScore.objects.get(Q(group='RHS Fillet score') & Q(name='intensity'))

    for bloodspot in targets:
        try:
            val = GetKV(ob, bloodspot)
            sc = scores.values[val.lower()]
            res += sc
        except:
            pass

    targets = [
        'Right Gaping V2',
        'Right Gaping V1',
        'Right Gaping D1',
        'Right Gaping D2',
        'Right Gaping D3',
        'Right Gaping D3D2',
        'Right Gaping D2D1',
        'Right Gaping D1V1',
        'Right Gaping V1V2',

    ]

    for gaping in targets:
        val = GetKV(ob, gaping)
        sc = scores.values[val.lower()]
        res += sc

    return res


def calc_lhs_torry_avg(ob):
    targets = [
        'Left Fillet Torry 1',
        'Left Fillet Torry 2',
        'Left Fillet Torry 3',
    ]

    res = 0
    for target in target:
        val = GetKV(ob, target)
        if val:
            res += val/len(targets)

    return res


def calc_rhs_torry_avg(ob):
    targets = [
        'Right Fillet Torry 1',
        'Right Fillet Torry 2',
        'Right Fillet Torry 3',
    ]

    res = 0
    for target in target:
        val = GetKV(ob, target)
        if val:
            res += val/len(targets)

    return res


def calc_lhs_internal_twitch(ob):
    fillet_twitch_intensity = GetKV(ob, 'Left Fillet Twitch Intensity')
    fillet_twitch_location = GetKV(ob, 'Left Fillet Twitch Location')

    res = 0

    if(fillet_twitch_intensity and fillet_twitch_location):
        scores = FishScore.objects.get(Q(name=fillet_twitch_location) & Q(group='LHS Internal Twitch'))
        res += scores.values[fillet_twitch_intensity]

    return res


def calc_rhs_internal_twitch(ob):
    fillet_twitch_intensity = GetKV(ob, 'Right Fillet Twitch Intensity')
    fillet_twitch_location = GetKV(ob, 'Right Fillet Twitch Location')

    res = 0

    if(fillet_twitch_intensity and fillet_twitch_location):
        scores = FishScore.objects.get(Q(name=fillet_twitch_location) & Q(group='RHS Internal Twitch'))
        res += scores.values[fillet_twitch_intensity]

    return res

    
# SIGNALS
@receiver(pre_save)
def set_calc_fields(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    try:
        instance.IsOb()
    except Exception:
        return

    try:
        res = {}
        res['External Twitch'] = calc_external_twitch(instance)
        res['Fin Score'] = calc_fin_score(instance)
        
        
        
    except ObjectDoesNotExist:
        msg = "ERROR in signal set_ontology. Uknown class: %s." % class_name
        Logger.Warning(msg)
        raise DataError(msg)


