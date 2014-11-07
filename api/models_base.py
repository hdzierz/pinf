from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import *

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField

from .logger import *
from .django_ext import *
from api.algorithms import *

import datetime
from jsonfield import JSONField


# Create your models here.
class DataError(Exception):
    pass


class Ontology(models.Model):
    ontology = 'unkown'
    name = models.CharField(max_length=2048)
    displayurl = models.CharField(max_length=2048, default="", null=True)
    tablename = models.CharField(max_length=128)
    owner = models.CharField(max_length=128, null=True, default='core')
    description = models.CharField(max_length=2048, null=True, default='')
    classname = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class DataSource(models.Model):
    name = models.CharField(max_length=1024)
    typ = models.CharField(null=True, max_length=256, default="None")
    supplier = models.CharField(null=True, max_length=2048, default="None")
    physicalsourceuri = models.CharField(null=True, max_length=2048)
    supplieddate = models.DateField(auto_now_add=True)
    comment = models.TextField(null=True, default="none")
    numberoffiles = models.IntegerField(null=True, default=1)
    uploadsourceuri = models.CharField(max_length=2048, null=True, default="")
    search_index = VectorField()
    objects = SearchManager(
        fields=('name', 'typ'),
        auto_update_search_field=True
    )

    def GetName(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, default="unknown")
    alias = models.CharField(max_length=255, default="unknown")
    datasource = models.ForeignKey(DataSource, default=1)
    description = models.TextField(default="")
    obid = models.AutoField(primary_key=True)
    ontology = models.ForeignKey(Ontology, default=1)
    xreflsid = models.CharField(max_length=255)
    createddate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=255)
    lastupdateddate = models.DateTimeField(auto_now=True)
    lastupdatedby = models.CharField(max_length=50)
    obkeywords = models.TextField()
    statuscode = models.IntegerField(default=1)
    search_index = VectorField()
    objects = SearchManager(
        fields=('name', 'alias', 'description', 'obkeywords'),
        auto_update_search_field=False
    )

    def InitOntology(self):
        name = self.__class__.__name__
        tname = 'api_' + name.lower()

        obt = Ontology()
        obt.displayname = name
        obt.classname = name
        obt.tablename = tname
        obt.save()

    def GetName(self):
        return self.name

    def IsOntology(self):
        return True

    class Meta:
        abstract = True


def InitOntology(obj):
    if isinstance(obj, str):
        name = obj
    elif isinstance(obj, object):
        name = obj.__class__.__name__
    else:
        raise Exception('Setting the Ontology can only be done for objects or strings')

    tname = 'api_' + name.lower()

    Ontology.objects.get_or_create(
        name=name,
        classname=name,
        tablename=tname
    )


class Species(Category):
    common_name = models.CharField(max_length=255)


class StudyGroup(Category):
    species = models.ForeignKey(Species)


class StudyArea(Category):
    wiki = models.CharField(max_length=255)


class Study(Category):
    study_group = models.ForeignKey(StudyGroup)
    study_area = models.ForeignKey(StudyArea)
    #biosequence = models.ForeignKey(BioSubjectOb, db_column='biosequenceob')

    @staticmethod
    def get_or_create_from_name(
        name,
        species_name,
        study_group_name,
        study_area_name):

        species, screated = Species.objects.get_or_create(
            name=species_name
            )

        study_group, gcreated = StudyGroup.objects.get_or_create(
            name=study_group_name,
            species=species
            )

        study_area, acreated = StudyArea.objects.get_or_create(
            name=study_area_name
            )

        study, created = Study.objects.get_or_create(
            name=name,
            study_area=study_area,
            study_group=study_group
            )

        if(created):
            study.xreflsid = "Study.{0}.{1}.{2}".format(
                study.study_area.name,
                study.study_group.name,
                study.name
                )
            study.save()
            Logger.Message("Study: Created new study %s." % name)

        return study

    def InitRawImport(self, clean=False):
        i = datetime.datetime.now()
        i_str = i.strftime('%Y-%m-%d')
        imp, created = RawImport.objects.get_or_create(
            study=self,
            createddate=i
            )

        if(created):
            imp.xreflsid = "RawImport." + self.xreflsid + "." + i_str
            imp.save()

            Logger.Message(
                "RawImports: Created new import entry for " + self.name
                )

        if(clean):
            imp.Clean()
        return imp

    def __unicode__(self):
        return self.name


class Diet(Category):
    pass


class Ob(models.Model):
    name = models.CharField(max_length=255)
    daughters = []
    ontology = models.ForeignKey(Ontology, default=1)
    datasource = models.ForeignKey(DataSource, null=True)
    study = models.ForeignKey(Study, null=True)
    xreflsid = models.CharField(max_length=2048)
    createddate = models.DateField(auto_now_add=True)
    createdby = models.CharField(max_length=255)
    lastupdateddate = models.DateField(auto_now=True)
    lastupdatedby = models.CharField(max_length=50)
    obkeywords = models.TextField()
    statuscode = models.IntegerField(default=1)
    group = models.CharField(max_length=1024, default="NA")
    recordeddate = models.DateField(auto_now_add=True)

    search_index = VectorField()
    objects = SearchManager(
        fields=('obkeywords'),
        auto_update_search_field=True
    )

    def IsOntology(self):
        return True

    def GetName(self):
        return self.study.name + '.' + self.name

    class Meta:
        abstract = True


class Unit(Category):
    pass


class ObKV(models.Model):
    parent = None
    datasource = models.ForeignKey(DataSource)
    key = models.CharField(max_length=255)
    value = JSONField()

    def __unicode__(self):
        return self.key + ":" + str(self.value)

    class Meta:
        abstract = True


def SaveKV(ob, cls, key, value):
    kv = eval(ob.daughters[0])
    enc = json.JSONEncoder()
    #kv = cls()
    kv.parent = ob
    kv.key = key
    kv.value = enc.encode(value)
    kv.save()
    return kv


def SaveKVs(ob, cls, lst):
    for key, value in list(lst.items()):
        SaveKV(ob, cls, key, value)
    return True


def GetKV(ob, cls, key):
    try:
        dec = json.JSONDecoder()
        kv = cls.objects.get(
            parent=ob,
            key=key
            )
        if(kv):
            return dec.decode(kv.value)
        else:
            return None
    except:
        return None


def decode(item):
    dec = json.JSONDecoder()
    item['value'] = dec.decode(item['value'])


def GetKVs(ob, cls):
    try:
        kvs = list(cls.objects.filter(
            parent=ob
            ).values())
        if(kvs):
            return for_each(kvs, decode)
        else:
            return None
    except:
        return None


class Gene(Category):
    pass


class Protein(Category):
    pass


class BioSubject(Category):
    species = models.ForeignKey(Species)
    subjectname = models.CharField(max_length=255)
    subjectspeciesname = models.CharField(max_length=1024)
    subjecttaxon = models.IntegerField(default=None, null=True)
    strain = models.CharField(max_length=1024, default=None, null=True)
    subjectdescription = models.TextField(default="")
    dob = models.DateField(default=None, null=True)
    sex = models.CharField(max_length=1, default=None, null=True)
    cohort = models.CharField(max_length=10, default=None, null=True)
    changed = models.BooleanField(default=False)
    comment = models.CharField(max_length=1024, default=None, null=True)
    do_ignore = models.BooleanField(default=False)
    centre = models.CharField(max_length=255, default=None, null=True)

    def GetName(self):
        return self.subjectname


class RawImport(Category):
    study = models.ForeignKey(Study)

    def Clean(self):
        RawImportOb.objects.filter(imp=self).delete()


class RawImportOb(Ob):
    debug = False
    grp = models.IntegerField(default=0)
    imp = models.ForeignKey(RawImport)
    att_key = models.CharField(max_length=255)
    att_value = models.CharField(max_length=255)

    @staticmethod
    def SaveOb(imp, key, value, grp=-9999):
        if(RawImportOb.debug):
            Logger.Error(value)
        riob = RawImportOb()
        riob.att_key = key
        riob.imp = imp
        riob.grp = grp
        riob.att_value = value
        riob.save()

    @staticmethod
    def GetOb(imp, key, grp=-9999):
        ob = RawImportOb.objects.get(imp=imp, att_key=key, grp=grp)
        if(ob):
            return ob.att_value
        else:
            Logger.Warning(
                "Ob.GetFact: Key does not exist: {0}/{1}".format(
                    ob.xreflsid,
                    key
                    )
                )
            return None

    @staticmethod
    def GetObs(imp):
        grps = RawImportOb.objects.filter(
            imp=imp).order_by("grp").distinct("grp")
        res = []
        for grp in grps:
            ris = RawImportOb.objects.filter(imp=imp, grp=grp.grp)

            v = {}
            for r in ris:
                v[r.att_key] = r.att_value
            res.append(v)
        return res


class Labresource(Category):
    typ = models.CharField(max_length=256)
    sequence = models.TextField()
    seqlength = models.IntegerField()
    date = models.DateField()
    supplier = models.CharField(max_length=1024)

    def GetName(self):
        return self.name


class Tissue(Category):
    pass


class BioSample(Category):
    biosubject = models.ForeignKey(BioSubject)
    typ = models.CharField(max_length=256)
    tissue = models.ForeignKey(Tissue)
    date = models.DateField()
    count = models.IntegerField(default=1)


class Treatment(Category):
    no = models.IntegerField(default=0)


class SampleMethod(Category):
    pass


class Instrument(Category):
    pass


class BioSequence(Category):
    typ = models.CharField(max_length=256)
    string = models.TextField()
    topology = models.CharField(max_length=32)
    length = models.IntegerField()
    url = models.CharField(max_length=2048)
    comment = models.CharField(max_length=2048)
    gi = models.IntegerField()
    fnindex_accession = models.CharField(max_length=2048)
    fnindex_id = models.CharField(max_length=2048)

    def GetName(self):
        return self.name


class FormInputLookupOb(models.Model):
    obid = models.AutoField(primary_key=True)
    form = models.CharField(max_length=255)
    inpt = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'form_input_lookup_ob'


class FormInputLookupFact(models.Model):
    obid = models.AutoField(primary_key=True)
    form_lookup_ob = models.ForeignKey(FormInputLookupOb)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'form_input_lookup_fact'


# SIGNALS
@receiver(pre_save)
def set_ontology(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    try:
        instance.IsOntology()
    except Exception:
        return

    try:
        obt = Ontology.objects.get(classname=class_name)
        instance.ontology = obt
        instance.xreflsid = class_name + "." + instance.GetName()
        instance.obkeywords = class_name + " " + instance.GetName()

    except ObjectDoesNotExist:
        msg = "ERROR in signal set_ontology. Uknown class: %s." % class_name
        Logger.Warning(msg)
        raise DataError(msg)

