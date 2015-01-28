from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(DataSource)
admin.site.register(Species)

admin.site.register(Trip)
admin.site.register(Tow)
admin.site.register(City)
admin.site.register(Crew)
admin.site.register(FishOb)
#admin.site.register(FishObKV)

admin.site.register(PrimerType)
admin.site.register(PrimerTail)
admin.site.register(PrimerOb)
admin.site.register(MarkerOb)

