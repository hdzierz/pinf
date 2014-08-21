# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Obtype'
        db.create_table(u'api_obtype', (
            ('obtypeid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('displayname', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('displayurl', self.gf('django.db.models.fields.CharField')(default='', max_length=2048)),
            ('tablename', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('namedinstances', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isvirtual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isdynamic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('obtypedescription', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'api', ['Obtype'])

        # Adding model 'Species'
        db.create_table(u'api_species', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Species'])

        # Adding model 'StudyGroup'
        db.create_table(u'api_studygroup', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Species'])),
        ))
        db.send_create_signal(u'api', ['StudyGroup'])

        # Adding model 'StudyArea'
        db.create_table(u'api_studyarea', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('wiki', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['StudyArea'])

        # Adding model 'Study'
        db.create_table(u'api_study', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('study_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.StudyGroup'])),
            ('study_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.StudyArea'])),
        ))
        db.send_create_signal(u'api', ['Study'])

        # Adding model 'DataSource'
        db.create_table(u'api_datasource', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('datasourcename', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('datasourcetype', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('datasupplier', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('physicalsourceuri', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('datasupplieddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('datasourcecomment', self.gf('django.db.models.fields.TextField')(default='none')),
            ('numberoffiles', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('datasourcecontent', self.gf('django.db.models.fields.TextField')(default='')),
            ('dynamiccontentmethod', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
            ('uploadsourceuri', self.gf('django.db.models.fields.CharField')(default='', max_length=2048)),
        ))
        db.send_create_signal(u'api', ['DataSource'])

        # Adding model 'Diet'
        db.create_table(u'api_diet', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Diet'])

        # Adding model 'Unit'
        db.create_table(u'api_unit', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Unit'])

        # Adding model 'Fact'
        db.create_table(u'api_fact', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('ob_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('att_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('att_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Fact'])

        # Adding model 'Gene'
        db.create_table(u'api_gene', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Gene'])

        # Adding model 'Protein'
        db.create_table(u'api_protein', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Protein'])

        # Adding model 'BioSubject'
        db.create_table(u'api_biosubject', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Species'])),
            ('subjectname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subjectspeciesname', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('subjecttaxon', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('strain', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, null=True)),
            ('subjectdescription', self.gf('django.db.models.fields.TextField')(default='')),
            ('dob', self.gf('django.db.models.fields.DateField')(default=None, null=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(default=None, max_length=1, null=True)),
            ('cohort', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True)),
            ('changed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, null=True)),
            ('do_ignore', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('centre', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True)),
        ))
        db.send_create_signal(u'api', ['BioSubject'])

        # Adding model 'RawImport'
        db.create_table(u'api_rawimport', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['RawImport'])

        # Adding model 'RawImportOb'
        db.create_table(u'api_rawimportob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('grp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('imp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.RawImport'])),
            ('att_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('att_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['RawImportOb'])

        # Adding model 'Labresource'
        db.create_table(u'api_labresource', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('resourcename', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('resourcetype', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('resourcesequence', self.gf('django.db.models.fields.TextField')()),
            ('resourceseqlength', self.gf('django.db.models.fields.IntegerField')()),
            ('resourcedate', self.gf('django.db.models.fields.DateField')()),
            ('resourcedescription', self.gf('django.db.models.fields.TextField')()),
            ('supplier', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'api', ['Labresource'])

        # Adding model 'Tissue'
        db.create_table(u'api_tissue', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Tissue'])

        # Adding model 'BioSample'
        db.create_table(u'api_biosample', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'])),
            ('typ', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('tissue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Tissue'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['BioSample'])

        # Adding model 'BioSequence'
        db.create_table(u'api_biosequence', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('sequencename', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('sequencetype', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('seqstring', self.gf('django.db.models.fields.TextField')()),
            ('sequencedescription', self.gf('django.db.models.fields.TextField')()),
            ('sequencetopology', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('seqlength', self.gf('django.db.models.fields.IntegerField')()),
            ('sequenceurl', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('seqcomment', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('gi', self.gf('django.db.models.fields.IntegerField')()),
            ('fnindex_accession', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('fnindex_id', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal(u'api', ['BioSequence'])

        # Adding model 'MouseIntakeOb'
        db.create_table(u'api_mouseintakeob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Unit'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('diet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Diet'], null=True)),
            ('intake', self.gf('django.db.models.fields.FloatField')(default=None, null=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'api', ['MouseIntakeOb'])

        # Adding model 'MouseWeightOb'
        db.create_table(u'api_mouseweightob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Unit'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('diet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Diet'], null=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(default=None, null=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'api', ['MouseWeightOb'])

        # Adding model 'MouseHistologyOb'
        db.create_table(u'api_mousehistologyob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Unit'])),
            ('biosample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSample'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('week', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('diet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Diet'], null=True)),
            ('inflam_type', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('sub_type', self.gf('django.db.models.fields.CharField')(default='=unknown', max_length=255)),
            ('score', self.gf('django.db.models.fields.FloatField')(default=None, null=True)),
            ('adj_score', self.gf('django.db.models.fields.FloatField')(default=None, null=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(default='', max_length=1024)),
        ))
        db.send_create_signal(u'api', ['MouseHistologyOb'])

        # Adding model 'MouseHistologyV2Ob'
        db.create_table(u'api_mousehistologyv2ob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('biosample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSample'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('scorer', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=20)),
            ('diet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Diet'], null=True)),
            ('crypt_hyperplasia', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('aberrant_crypts', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('crypt_injury', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('crypt_loss', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('goblet_cell_loss', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('crypt_abscess', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('lymphoid_aggregates', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('submucosal_thickening', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('hyperchromatic', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('surface_loss', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('monocytes_and_macrophages', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('neutrophils', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('plasma_cells_and_lymphocytes', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('muscular_layer', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('omental_fat', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('all_unit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='all_unit', null=True, to=orm['api.Unit'])),
            ('comments', self.gf('django.db.models.fields.CharField')(default='', max_length=1024)),
        ))
        db.send_create_signal(u'api', ['MouseHistologyV2Ob'])

        # Adding model 'EpigeneticsOb'
        db.create_table(u'api_epigeneticsob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Unit'])),
            ('biosample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSample'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('island', self.gf('django.db.models.fields.CharField')(default='CpG_unkown', max_length=255)),
            ('methylation', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('assay', self.gf('django.db.models.fields.CharField')(default='-9999', max_length=255)),
            ('diet', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('lid', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('week', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'api', ['EpigeneticsOb'])

        # Adding model 'ProteinGelSpotOb'
        db.create_table(u'api_proteingelspotob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('biosample', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSample'])),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('fold_change', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('num_uniq_pep', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('spot_no', self.gf('django.db.models.fields.CharField')(default='unkown', max_length=155)),
            ('acc_num', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('gene_mgi', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('prot_ident', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('theo_pl', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('sequest_p', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('spot', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('seq_cov', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('theo_al', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('M_Gel', self.gf('django.db.models.fields.CharField')(default='-9999', max_length=255)),
            ('descriptor', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('week', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(default='', max_length=1024)),
        ))
        db.send_create_signal(u'api', ['ProteinGelSpotOb'])

        # Adding model 'QuestionnaireOb'
        db.create_table(u'api_questionnaireob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'], null=True, blank=True)),
            ('att_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('att_value', self.gf('django.db.models.fields.CharField')(default=None, max_length=4096, null=True)),
            ('att_code', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True)),
            ('grp', self.gf('django.db.models.fields.CharField')(default='', max_length=1024)),
        ))
        db.send_create_signal(u'api', ['QuestionnaireOb'])

        # Adding model 'Genotype'
        db.create_table(u'api_genotype', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('typ', self.gf('django.db.models.fields.CharField')(default='SNP', max_length=255)),
        ))
        db.send_create_signal(u'api', ['Genotype'])

        # Adding model 'GenotypeOb'
        db.create_table(u'api_genotypeob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('biosubject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.BioSubject'])),
            ('genotype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Genotype'])),
            ('observationdate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('genotypeobserved', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True)),
            ('genotypeobserved_comment', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, null=True)),
            ('finalgenotype', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True)),
            ('finalgenotype_comment', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, null=True)),
        ))
        db.send_create_signal(u'api', ['GenotypeOb'])

        # Adding model 'Fish'
        db.create_table(u'api_fish', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'api', ['Fish'])

        # Adding model 'FishOb'
        db.create_table(u'api_fishob', (
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
        ))
        db.send_create_signal(u'api', ['FishOb'])


    def backwards(self, orm):
        # Deleting model 'Obtype'
        db.delete_table(u'api_obtype')

        # Deleting model 'Species'
        db.delete_table(u'api_species')

        # Deleting model 'StudyGroup'
        db.delete_table(u'api_studygroup')

        # Deleting model 'StudyArea'
        db.delete_table(u'api_studyarea')

        # Deleting model 'Study'
        db.delete_table(u'api_study')

        # Deleting model 'DataSource'
        db.delete_table(u'api_datasource')

        # Deleting model 'Diet'
        db.delete_table(u'api_diet')

        # Deleting model 'Unit'
        db.delete_table(u'api_unit')

        # Deleting model 'Fact'
        db.delete_table(u'api_fact')

        # Deleting model 'Gene'
        db.delete_table(u'api_gene')

        # Deleting model 'Protein'
        db.delete_table(u'api_protein')

        # Deleting model 'BioSubject'
        db.delete_table(u'api_biosubject')

        # Deleting model 'RawImport'
        db.delete_table(u'api_rawimport')

        # Deleting model 'RawImportOb'
        db.delete_table(u'api_rawimportob')

        # Deleting model 'Labresource'
        db.delete_table(u'api_labresource')

        # Deleting model 'Tissue'
        db.delete_table(u'api_tissue')

        # Deleting model 'BioSample'
        db.delete_table(u'api_biosample')

        # Deleting model 'BioSequence'
        db.delete_table(u'api_biosequence')

        # Deleting model 'MouseIntakeOb'
        db.delete_table(u'api_mouseintakeob')

        # Deleting model 'MouseWeightOb'
        db.delete_table(u'api_mouseweightob')

        # Deleting model 'MouseHistologyOb'
        db.delete_table(u'api_mousehistologyob')

        # Deleting model 'MouseHistologyV2Ob'
        db.delete_table(u'api_mousehistologyv2ob')

        # Deleting model 'EpigeneticsOb'
        db.delete_table(u'api_epigeneticsob')

        # Deleting model 'ProteinGelSpotOb'
        db.delete_table(u'api_proteingelspotob')

        # Deleting model 'QuestionnaireOb'
        db.delete_table(u'api_questionnaireob')

        # Deleting model 'Genotype'
        db.delete_table(u'api_genotype')

        # Deleting model 'GenotypeOb'
        db.delete_table(u'api_genotypeob')

        # Deleting model 'Fish'
        db.delete_table(u'api_fish')

        # Deleting model 'FishOb'
        db.delete_table(u'api_fishob')


    models = {
        u'api.biosample': {
            'Meta': {'object_name': 'BioSample'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tissue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Tissue']"}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.biosequence': {
            'Meta': {'object_name': 'BioSequence'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'fnindex_accession': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'fnindex_id': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'gi': ('django.db.models.fields.IntegerField', [], {}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'seqcomment': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'seqlength': ('django.db.models.fields.IntegerField', [], {}),
            'seqstring': ('django.db.models.fields.TextField', [], {}),
            'sequencedescription': ('django.db.models.fields.TextField', [], {}),
            'sequencename': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'sequencetopology': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'sequencetype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sequenceurl': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.biosubject': {
            'Meta': {'object_name': 'BioSubject'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'centre': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'changed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cohort': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'do_ignore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'sex': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1', 'null': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'strain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True'}),
            'subjectdescription': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'subjectname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subjectspeciesname': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'subjecttaxon': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasourcecomment': ('django.db.models.fields.TextField', [], {'default': "'none'"}),
            'datasourcecontent': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'datasourcename': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'datasourcetype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'datasupplieddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasupplier': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'dynamiccontentmethod': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'numberoffiles': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'physicalsourceuri': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'uploadsourceuri': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.diet': {
            'Meta': {'object_name': 'Diet'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.epigeneticsob': {
            'Meta': {'object_name': 'EpigeneticsOb'},
            'assay': ('django.db.models.fields.CharField', [], {'default': "'-9999'", 'max_length': '255'}),
            'biosample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSample']"}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'diet': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'island': ('django.db.models.fields.CharField', [], {'default': "'CpG_unkown'", 'max_length': '255'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'methylation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.fact': {
            'Meta': {'object_name': 'Fact'},
            'att_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'att_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ob_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.fish': {
            'Meta': {'object_name': 'Fish'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.fishob': {
            'Meta': {'object_name': 'FishOb'},
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.forminputlookupfact': {
            'Meta': {'object_name': 'FormInputLookupFact', 'db_table': "'form_input_lookup_fact'", 'managed': 'False'},
            'form_lookup_ob': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.FormInputLookupOb']"}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.forminputlookupob': {
            'Meta': {'object_name': 'FormInputLookupOb', 'db_table': "'form_input_lookup_ob'", 'managed': 'False'},
            'form': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'inpt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'api.gene': {
            'Meta': {'object_name': 'Gene'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.genotype': {
            'Meta': {'object_name': 'Genotype'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'typ': ('django.db.models.fields.CharField', [], {'default': "'SNP'", 'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.genotypeob': {
            'Meta': {'object_name': 'GenotypeOb'},
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']"}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'finalgenotype': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'finalgenotype_comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'null': 'True'}),
            'genotype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Genotype']"}),
            'genotypeobserved': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'genotypeobserved_comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'observationdate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.genotypeoblg': {
            'Meta': {'object_name': 'GenotypeObLg', 'db_table': "'api_genotypeob_lg'", 'managed': 'False'},
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']"}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']"}),
            'genotype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Genotype']"}),
            'genotypeobserved': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']"})
        },
        u'api.labresource': {
            'Meta': {'object_name': 'Labresource'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'resourcedate': ('django.db.models.fields.DateField', [], {}),
            'resourcedescription': ('django.db.models.fields.TextField', [], {}),
            'resourcename': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'resourceseqlength': ('django.db.models.fields.IntegerField', [], {}),
            'resourcesequence': ('django.db.models.fields.TextField', [], {}),
            'resourcetype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'supplier': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.mousehistologyob': {
            'Meta': {'object_name': 'MouseHistologyOb'},
            'adj_score': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'biosample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSample']"}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'diet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Diet']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'inflam_type': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'score': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'sub_type': ('django.db.models.fields.CharField', [], {'default': "'=unknown'", 'max_length': '255'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'week': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.mousehistologyv2ob': {
            'Meta': {'object_name': 'MouseHistologyV2Ob'},
            'aberrant_crypts': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'all_unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'all_unit'", 'null': 'True', 'to': u"orm['api.Unit']"}),
            'biosample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSample']"}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crypt_abscess': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'crypt_hyperplasia': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'crypt_injury': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'crypt_loss': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'diet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Diet']", 'null': 'True'}),
            'goblet_cell_loss': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'hyperchromatic': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lymphoid_aggregates': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'monocytes_and_macrophages': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'muscular_layer': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'neutrophils': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'omental_fat': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'plasma_cells_and_lymphocytes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'scorer': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '20'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'submucosal_thickening': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'surface_loss': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.mouseintakeob': {
            'Meta': {'object_name': 'MouseIntakeOb'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'diet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Diet']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'intake': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.mouseweightob': {
            'Meta': {'object_name': 'MouseWeightOb'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'diet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Diet']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.obtype': {
            'Meta': {'object_name': 'Obtype'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'displayname': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'displayurl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'isdynamic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvirtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'namedinstances': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obtypedescription': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'obtypeid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tablename': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.protein': {
            'Meta': {'object_name': 'Protein'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.proteingelspotob': {
            'M_Gel': ('django.db.models.fields.CharField', [], {'default': "'-9999'", 'max_length': '255'}),
            'Meta': {'object_name': 'ProteinGelSpotOb'},
            'acc_num': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'biosample': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSample']"}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'file_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'fold_change': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'gene_mgi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'num_uniq_pep': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'prot_ident': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'seq_cov': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'sequest_p': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'spot': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'spot_no': ('django.db.models.fields.CharField', [], {'default': "'unkown'", 'max_length': '155'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'theo_al': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'theo_pl': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.questionnaireob': {
            'Meta': {'object_name': 'QuestionnaireOb'},
            'att_code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'att_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'att_value': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4096', 'null': 'True'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']", 'null': 'True', 'blank': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'grp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.rawimport': {
            'Meta': {'object_name': 'RawImport'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']"}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.rawimportob': {
            'Meta': {'object_name': 'RawImportOb'},
            'att_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'att_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'grp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'imp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.RawImport']"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.species': {
            'Meta': {'object_name': 'Species'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.study': {
            'Meta': {'object_name': 'Study'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyArea']"}),
            'study_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyGroup']"}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studyarea': {
            'Meta': {'object_name': 'StudyArea'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wiki': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.tissue': {
            'Meta': {'object_name': 'Tissue'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.unit': {
            'Meta': {'object_name': 'Unit'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Obtype']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']