from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import *

from .logger import *
from .django_ext import *

import datetime


# Create your models here.
class DataError(Exception):
    pass


class Ontology(models.Model):
    ontology = 'unkown'
    displayname = models.CharField(max_length=2048)
    uri = models.CharField(max_length=2048)
    displayurl = models.CharField(max_length=2048, default="")
    tablename = models.CharField(max_length=128)
    namedinstances = models.BooleanField(default=False)
    isop = models.BooleanField(default=False)
    isvirtual = models.BooleanField(default=False)
    isdynamic = models.BooleanField(default=False)
    owner = models.CharField(max_length=128)
    Ontologydescription = models.CharField(max_length=2048)
    classname = models.CharField(max_length=128)


class Category(models.Model):
    ontology = 'unkown'
    name = models.CharField(max_length=255, default="unknown")
    alias = models.CharField(max_length=255, default="unknown")
    description = models.TextField(default="")
    obid = models.AutoField(primary_key=True)
    Ontology = models.ForeignKey(Ontology, default=1)
    xreflsid = models.CharField(max_length=255)
    createddate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField(max_length=255)
    lastupdateddate = models.DateTimeField(auto_now=True)
    lastupdatedby = models.CharField(max_length=50)
    obkeywords = models.TextField()
    statuscode = models.IntegerField(default=1)

    def GetName(self):
        return self.name

    def IsCategory(self):
        return True

    class Meta:
        abstract = True


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


class DataSource(Category):
    datasourcename = models.CharField(max_length=1024)
    datasourcetype = models.CharField(max_length=256)
    datasupplier = models.CharField(max_length=2048)
    physicalsourceuri = models.CharField(max_length=2048)
    datasupplieddate = models.DateField(auto_now_add=True)
    datasourcecomment = models.TextField(default="none")
    numberoffiles = models.IntegerField(default=1)
    datasourcecontent = models.TextField(default="")
    dynamiccontentmethod = models.CharField(max_length=256, default="")
    uploadsourceuri = models.CharField(max_length=2048, default="")

    def GetName(self):
        return self.datasourcename


class Diet(Category):
    pass


class Ob(models.Model):
    debug = False
    ontology = 'Ob'
    obid = models.AutoField(primary_key=True)
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
    recordeddate = models.DateField()

    def IsOb(self):
        return True

    def GetName(self):
        ans = []
        frame = inspect.currentframe().f_back
        tmp = dict(list(frame.f_globals.items()) + list(frame.f_locals.items()))
        for k, var in list(tmp.items()):
            if isinstance(var, self.__class__):
                if hash(self) == hash(var):
                    ans.append(k)
        if(len(ans) >= 1):
            return ans[0]
        else:
            return "unkown"

    class Meta:
        abstract = True


class Unit(Category):
    pass


class ObKV(models.Model):
    ob = models.ForeignKey(Ob)
    att_key = models.CharField(max_length=255)
    att_value = models.CharField(max_length=255)


def SaveKV(ob, key, value):
    fact, created = ObKV.objects.get_or_create(
        att_key=key,
        ob=ob
        )
    if(created):
        Logger.Warning(
            "Ob.SaveFact: Created new fact for %s/%s" % ob.xreflsid, key
            )
    fact.value = value
    fact.save()
    return fact


def GetKV(ob, key):
    fact = ObKV.objects.get(ob=ob, att_key=key)
    if(fact):
        return fact.att_value
    else:
        Logger.Warning(
            "Ob.GetFact: Key does not exist: {0}/{1}".format(
                ob.xreflsid,
                key)
            )
        return None


def GetKVs(ob):
    kvs = ObKV.objects.filter(ob=ob)
    if(kvs):
        return kvs
    else:
        return None


def SetKVs(ob, values):
    for item in values:
        SaveKv(ob, item)


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
    datasource = models.ForeignKey(DataSource, null=True, blank=True)

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

    resourcename = models.CharField(max_length=1024)
    resourcetype = models.CharField(max_length=256)
    resourcesequence = models.TextField()
    resourceseqlength = models.IntegerField()
    resourcedate = models.DateField()
    resourcedescription = models.TextField()
    supplier = models.CharField(max_length=1024)

    def GetName(self):
        return self.resourcename


class Tissue(Category):
    pass


class BioSample(Category):
    biosubject = models.ForeignKey(BioSubject)
    typ = models.CharField(max_length=256)
    tissue = models.ForeignKey(Tissue)
    date = models.DateField()
    count = models.IntegerField(default=1)


class BioSequence(Category):
    sequencename = models.CharField(max_length=1024)
    sequencetype = models.CharField(max_length=256)
    seqstring = models.TextField()
    sequencedescription = models.TextField()
    sequencetopology = models.CharField(max_length=32)
    seqlength = models.IntegerField()
    sequenceurl = models.CharField(max_length=2048)
    seqcomment = models.CharField(max_length=2048)
    gi = models.IntegerField()
    fnindex_accession = models.CharField(max_length=2048)
    fnindex_id = models.CharField(max_length=2048)

    def GetName(self):
        return self.sequencename


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
        instance.isOb()
    except Exception:
        return
    try:
        obt = Ontology.objects.get(classname=class_name)
        instance.Ontology = obt
        if not(instance.xreflsid):
            instance.xreflsid = class_name + "." + instance.name

    except ObjectDoesNotExist:
        msg = "ERROR in signal set_ontology. Uknown class: %s." % class_name
        Logger.Warning(msg)
        raise DataError(msg)


@receiver(pre_save)
def set_category(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    try:
        instance.IsCategory()
    except Exception:
        return
    try:
        obt = Ontology.objects.get(classname=class_name)
        instance.Ontology = obt
        if not(instance.xreflsid):
            instance.xreflsid = class_name + "." + instance.name

    except ObjectDoesNotExist:
        msg = "ERROR in signal set_category. Uknown class: %s." % class_name
        Logger.Warning(msg)
        raise DataError(msg)


@receiver(pre_save)
def set_xreflsid_ob(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    try:
        instance.isOb()
    except Exception:
        Logger.Warning("OB: No IsOb function in " + class_name)
        return

    if not(instance.xreflsid):
        instance.xreflsid = class_name + "." + instance.GetName()


@receiver(pre_save)
def set_xreflsid_category(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    try:
        instance.IsCategory()
    except Exception:
        Logger.Warning("ONTO: No IsOnto function in " + class_name)
        return

    if not(instance.xreflsid):
        n = instance.GetName()
        instance.xreflsid = class_name + "." + n
