from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(DataSource)
admin.site.register(Species)
admin.site.register(Ontology)
admin.site.register(Term)

