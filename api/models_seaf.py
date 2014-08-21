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
    deleted = models.CharField(max_length=1)


class Crew(Category):
    crew_name = models.CharField(max_length=100)


class FishOb(Ob):
    val = None
    form_completed = models.BooleanField()
    trip = models.ForeignKey(Trip)
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

