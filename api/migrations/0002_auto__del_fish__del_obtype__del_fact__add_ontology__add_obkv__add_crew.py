# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Fish'
        db.delete_table(u'api_fish')

        # Deleting model 'Obtype'
        db.delete_table(u'api_obtype')

        # Deleting model 'Fact'
        db.delete_table(u'api_fact')

        # Adding model 'Ontology'
        db.create_table(u'api_ontology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('displayname', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('displayurl', self.gf('django.db.models.fields.CharField')(default='', max_length=2048)),
            ('tablename', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('namedinstances', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isvirtual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isdynamic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('Ontologydescription', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'api', ['Ontology'])

        # Adding model 'ObKV'
        db.create_table(u'api_obkv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ob_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('att_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('att_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['ObKV'])

        # Adding model 'Crew'
        db.create_table(u'api_crew', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Ontology', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('crew_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'api', ['Crew'])

        # Adding model 'Trip'
        db.create_table(u'api_trip', (
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Ontology', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('trip_no', self.gf('django.db.models.fields.IntegerField')()),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Species'])),
            ('vessel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('registration', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('captain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('first_sailing', self.gf('django.db.models.fields.DateField')()),
            ('last_arrival', self.gf('django.db.models.fields.DateField')()),
            ('deleted', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'api', ['Trip'])

        # Deleting field 'FishOb.obtype'
        db.delete_column(u'api_fishob', 'obtype_id')

        # Adding field 'FishOb.ontology'
        db.add_column(u'api_fishob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'FishOb.recordeddate'
        db.add_column(u'api_fishob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'FishOb.form_completed'
        db.add_column(u'api_fishob', 'form_completed',
                      self.gf('django.db.models.fields.BooleanField')(default='Y'),
                      keep_default=False)

        # Adding field 'FishOb.trip'
        db.add_column(u'api_fishob', 'trip',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['api.Trip']),
                      keep_default=False)

        # Deleting field 'MouseHistologyOb.obtype'
        db.delete_column(u'api_mousehistologyob', 'obtype_id')

        # Adding field 'MouseHistologyOb.ontology'
        db.add_column(u'api_mousehistologyob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'MouseHistologyOb.recordeddate'
        db.add_column(u'api_mousehistologyob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'BioSequence.obtype'
        db.delete_column(u'api_biosequence', 'obtype_id')

        # Adding field 'BioSequence.Ontology'
        db.add_column(u'api_biosequence', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'BioSequence.createddate'
        db.alter_column(u'api_biosequence', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'BioSequence.lastupdateddate'
        db.alter_column(u'api_biosequence', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))
        # Deleting field 'Protein.obtype'
        db.delete_column(u'api_protein', 'obtype_id')

        # Adding field 'Protein.Ontology'
        db.add_column(u'api_protein', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Protein.lastupdateddate'
        db.alter_column(u'api_protein', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Protein.createddate'
        db.alter_column(u'api_protein', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'StudyGroup.obtype'
        db.delete_column(u'api_studygroup', 'obtype_id')

        # Adding field 'StudyGroup.Ontology'
        db.add_column(u'api_studygroup', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'StudyGroup.lastupdateddate'
        db.alter_column(u'api_studygroup', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'StudyGroup.createddate'
        db.alter_column(u'api_studygroup', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'BioSample.obtype'
        db.delete_column(u'api_biosample', 'obtype_id')

        # Adding field 'BioSample.Ontology'
        db.add_column(u'api_biosample', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'BioSample.lastupdateddate'
        db.alter_column(u'api_biosample', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'BioSample.createddate'
        db.alter_column(u'api_biosample', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'GenotypeOb.obtype'
        db.delete_column(u'api_genotypeob', 'obtype_id')

        # Adding field 'GenotypeOb.ontology'
        db.add_column(u'api_genotypeob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'GenotypeOb.recordeddate'
        db.add_column(u'api_genotypeob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'QuestionnaireOb.obtype'
        db.delete_column(u'api_questionnaireob', 'obtype_id')

        # Adding field 'QuestionnaireOb.ontology'
        db.add_column(u'api_questionnaireob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'QuestionnaireOb.recordeddate'
        db.add_column(u'api_questionnaireob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'Species.obtype'
        db.delete_column(u'api_species', 'obtype_id')

        # Adding field 'Species.Ontology'
        db.add_column(u'api_species', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Species.lastupdateddate'
        db.alter_column(u'api_species', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Species.createddate'
        db.alter_column(u'api_species', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'DataSource.obtype'
        db.delete_column(u'api_datasource', 'obtype_id')

        # Adding field 'DataSource.Ontology'
        db.add_column(u'api_datasource', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'DataSource.lastupdateddate'
        db.alter_column(u'api_datasource', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'DataSource.createddate'
        db.alter_column(u'api_datasource', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'MouseIntakeOb.obtype'
        db.delete_column(u'api_mouseintakeob', 'obtype_id')

        # Adding field 'MouseIntakeOb.ontology'
        db.add_column(u'api_mouseintakeob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'MouseIntakeOb.recordeddate'
        db.add_column(u'api_mouseintakeob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'StudyArea.obtype'
        db.delete_column(u'api_studyarea', 'obtype_id')

        # Adding field 'StudyArea.Ontology'
        db.add_column(u'api_studyarea', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'StudyArea.lastupdateddate'
        db.alter_column(u'api_studyarea', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'StudyArea.createddate'
        db.alter_column(u'api_studyarea', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Labresource.obtype'
        db.delete_column(u'api_labresource', 'obtype_id')

        # Adding field 'Labresource.Ontology'
        db.add_column(u'api_labresource', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Labresource.lastupdateddate'
        db.alter_column(u'api_labresource', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Labresource.createddate'
        db.alter_column(u'api_labresource', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Study.obtype'
        db.delete_column(u'api_study', 'obtype_id')

        # Adding field 'Study.Ontology'
        db.add_column(u'api_study', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Study.lastupdateddate'
        db.alter_column(u'api_study', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Study.createddate'
        db.alter_column(u'api_study', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Unit.obtype'
        db.delete_column(u'api_unit', 'obtype_id')

        # Adding field 'Unit.Ontology'
        db.add_column(u'api_unit', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Unit.lastupdateddate'
        db.alter_column(u'api_unit', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Unit.createddate'
        db.alter_column(u'api_unit', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'RawImport.obtype'
        db.delete_column(u'api_rawimport', 'obtype_id')

        # Adding field 'RawImport.Ontology'
        db.add_column(u'api_rawimport', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'RawImport.lastupdateddate'
        db.alter_column(u'api_rawimport', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'RawImport.createddate'
        db.alter_column(u'api_rawimport', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'EpigeneticsOb.obtype'
        db.delete_column(u'api_epigeneticsob', 'obtype_id')

        # Adding field 'EpigeneticsOb.ontology'
        db.add_column(u'api_epigeneticsob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'EpigeneticsOb.recordeddate'
        db.add_column(u'api_epigeneticsob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'ProteinGelSpotOb.obtype'
        db.delete_column(u'api_proteingelspotob', 'obtype_id')

        # Adding field 'ProteinGelSpotOb.ontology'
        db.add_column(u'api_proteingelspotob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'ProteinGelSpotOb.recordeddate'
        db.add_column(u'api_proteingelspotob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'MouseWeightOb.obtype'
        db.delete_column(u'api_mouseweightob', 'obtype_id')

        # Adding field 'MouseWeightOb.ontology'
        db.add_column(u'api_mouseweightob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'MouseWeightOb.recordeddate'
        db.add_column(u'api_mouseweightob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'RawImportOb.obtype'
        db.delete_column(u'api_rawimportob', 'obtype_id')

        # Adding field 'RawImportOb.ontology'
        db.add_column(u'api_rawimportob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'RawImportOb.recordeddate'
        db.add_column(u'api_rawimportob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'MouseHistologyV2Ob.obtype'
        db.delete_column(u'api_mousehistologyv2ob', 'obtype_id')

        # Adding field 'MouseHistologyV2Ob.ontology'
        db.add_column(u'api_mousehistologyv2ob', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Adding field 'MouseHistologyV2Ob.recordeddate'
        db.add_column(u'api_mousehistologyv2ob', 'recordeddate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'Gene.obtype'
        db.delete_column(u'api_gene', 'obtype_id')

        # Adding field 'Gene.Ontology'
        db.add_column(u'api_gene', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Gene.lastupdateddate'
        db.alter_column(u'api_gene', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Gene.createddate'
        db.alter_column(u'api_gene', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Diet.obtype'
        db.delete_column(u'api_diet', 'obtype_id')

        # Adding field 'Diet.Ontology'
        db.add_column(u'api_diet', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Diet.lastupdateddate'
        db.alter_column(u'api_diet', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Diet.createddate'
        db.alter_column(u'api_diet', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'Tissue.obtype'
        db.delete_column(u'api_tissue', 'obtype_id')

        # Adding field 'Tissue.Ontology'
        db.add_column(u'api_tissue', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Tissue.lastupdateddate'
        db.alter_column(u'api_tissue', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Tissue.createddate'
        db.alter_column(u'api_tissue', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Deleting field 'BioSubject.obtype'
        db.delete_column(u'api_biosubject', 'obtype_id')

        # Adding field 'BioSubject.Ontology'
        db.add_column(u'api_biosubject', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'BioSubject.createddate'
        db.alter_column(u'api_biosubject', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'BioSubject.lastupdateddate'
        db.alter_column(u'api_biosubject', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))
        # Deleting field 'Genotype.obtype'
        db.delete_column(u'api_genotype', 'obtype_id')

        # Adding field 'Genotype.Ontology'
        db.add_column(u'api_genotype', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


        # Changing field 'Genotype.lastupdateddate'
        db.alter_column(u'api_genotype', 'lastupdateddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Genotype.createddate'
        db.alter_column(u'api_genotype', 'createddate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Adding model 'Fish'
        db.create_table(u'api_fish', (
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('name', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Fish'])

        # Adding model 'Obtype'
        db.create_table(u'api_obtype', (
            ('obtypedescription', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('displayname', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('obtypeid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isdynamic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('displayurl', self.gf('django.db.models.fields.CharField')(default='', max_length=2048)),
            ('classname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('isop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('isvirtual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tablename', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('namedinstances', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['Obtype'])

        # Adding model 'Fact'
        db.create_table(u'api_fact', (
            ('group', self.gf('django.db.models.fields.CharField')(default='NA', max_length=1024)),
            ('att_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('att_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('obtype', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype'])),
            ('lastupdatedby', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('study', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Study'], null=True)),
            ('obid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('xreflsid', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('datasource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.DataSource'], null=True)),
            ('createdby', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('statuscode', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('ob_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('obkeywords', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'api', ['Fact'])

        # Deleting model 'Ontology'
        db.delete_table(u'api_ontology')

        # Deleting model 'ObKV'
        db.delete_table(u'api_obkv')

        # Deleting model 'Crew'
        db.delete_table(u'api_crew')

        # Deleting model 'Trip'
        db.delete_table(u'api_trip')

        # Adding field 'FishOb.obtype'
        db.add_column(u'api_fishob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'FishOb.ontology'
        db.delete_column(u'api_fishob', 'ontology_id')

        # Deleting field 'FishOb.recordeddate'
        db.delete_column(u'api_fishob', 'recordeddate')

        # Deleting field 'FishOb.form_completed'
        db.delete_column(u'api_fishob', 'form_completed')

        # Deleting field 'FishOb.trip'
        db.delete_column(u'api_fishob', 'trip_id')

        # Adding field 'MouseHistologyOb.obtype'
        db.add_column(u'api_mousehistologyob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'MouseHistologyOb.ontology'
        db.delete_column(u'api_mousehistologyob', 'ontology_id')

        # Deleting field 'MouseHistologyOb.recordeddate'
        db.delete_column(u'api_mousehistologyob', 'recordeddate')

        # Adding field 'BioSequence.obtype'
        db.add_column(u'api_biosequence', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'BioSequence.Ontology'
        db.delete_column(u'api_biosequence', 'Ontology_id')


        # Changing field 'BioSequence.createddate'
        db.alter_column(u'api_biosequence', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'BioSequence.lastupdateddate'
        db.alter_column(u'api_biosequence', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))
        # Adding field 'Protein.obtype'
        db.add_column(u'api_protein', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Protein.Ontology'
        db.delete_column(u'api_protein', 'Ontology_id')


        # Changing field 'Protein.lastupdateddate'
        db.alter_column(u'api_protein', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Protein.createddate'
        db.alter_column(u'api_protein', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'StudyGroup.obtype'
        db.add_column(u'api_studygroup', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'StudyGroup.Ontology'
        db.delete_column(u'api_studygroup', 'Ontology_id')


        # Changing field 'StudyGroup.lastupdateddate'
        db.alter_column(u'api_studygroup', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'StudyGroup.createddate'
        db.alter_column(u'api_studygroup', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'BioSample.obtype'
        db.add_column(u'api_biosample', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'BioSample.Ontology'
        db.delete_column(u'api_biosample', 'Ontology_id')


        # Changing field 'BioSample.lastupdateddate'
        db.alter_column(u'api_biosample', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'BioSample.createddate'
        db.alter_column(u'api_biosample', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'GenotypeOb.obtype'
        db.add_column(u'api_genotypeob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'GenotypeOb.ontology'
        db.delete_column(u'api_genotypeob', 'ontology_id')

        # Deleting field 'GenotypeOb.recordeddate'
        db.delete_column(u'api_genotypeob', 'recordeddate')

        # Adding field 'QuestionnaireOb.obtype'
        db.add_column(u'api_questionnaireob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'QuestionnaireOb.ontology'
        db.delete_column(u'api_questionnaireob', 'ontology_id')

        # Deleting field 'QuestionnaireOb.recordeddate'
        db.delete_column(u'api_questionnaireob', 'recordeddate')

        # Adding field 'Species.obtype'
        db.add_column(u'api_species', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Species.Ontology'
        db.delete_column(u'api_species', 'Ontology_id')


        # Changing field 'Species.lastupdateddate'
        db.alter_column(u'api_species', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Species.createddate'
        db.alter_column(u'api_species', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'DataSource.obtype'
        db.add_column(u'api_datasource', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'DataSource.Ontology'
        db.delete_column(u'api_datasource', 'Ontology_id')


        # Changing field 'DataSource.lastupdateddate'
        db.alter_column(u'api_datasource', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'DataSource.createddate'
        db.alter_column(u'api_datasource', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'MouseIntakeOb.obtype'
        db.add_column(u'api_mouseintakeob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'MouseIntakeOb.ontology'
        db.delete_column(u'api_mouseintakeob', 'ontology_id')

        # Deleting field 'MouseIntakeOb.recordeddate'
        db.delete_column(u'api_mouseintakeob', 'recordeddate')

        # Adding field 'StudyArea.obtype'
        db.add_column(u'api_studyarea', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'StudyArea.Ontology'
        db.delete_column(u'api_studyarea', 'Ontology_id')


        # Changing field 'StudyArea.lastupdateddate'
        db.alter_column(u'api_studyarea', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'StudyArea.createddate'
        db.alter_column(u'api_studyarea', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'Labresource.obtype'
        db.add_column(u'api_labresource', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Labresource.Ontology'
        db.delete_column(u'api_labresource', 'Ontology_id')


        # Changing field 'Labresource.lastupdateddate'
        db.alter_column(u'api_labresource', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Labresource.createddate'
        db.alter_column(u'api_labresource', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'Study.obtype'
        db.add_column(u'api_study', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Study.Ontology'
        db.delete_column(u'api_study', 'Ontology_id')


        # Changing field 'Study.lastupdateddate'
        db.alter_column(u'api_study', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Study.createddate'
        db.alter_column(u'api_study', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'Unit.obtype'
        db.add_column(u'api_unit', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Unit.Ontology'
        db.delete_column(u'api_unit', 'Ontology_id')


        # Changing field 'Unit.lastupdateddate'
        db.alter_column(u'api_unit', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Unit.createddate'
        db.alter_column(u'api_unit', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'RawImport.obtype'
        db.add_column(u'api_rawimport', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'RawImport.Ontology'
        db.delete_column(u'api_rawimport', 'Ontology_id')


        # Changing field 'RawImport.lastupdateddate'
        db.alter_column(u'api_rawimport', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'RawImport.createddate'
        db.alter_column(u'api_rawimport', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'EpigeneticsOb.obtype'
        db.add_column(u'api_epigeneticsob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'EpigeneticsOb.ontology'
        db.delete_column(u'api_epigeneticsob', 'ontology_id')

        # Deleting field 'EpigeneticsOb.recordeddate'
        db.delete_column(u'api_epigeneticsob', 'recordeddate')

        # Adding field 'ProteinGelSpotOb.obtype'
        db.add_column(u'api_proteingelspotob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'ProteinGelSpotOb.ontology'
        db.delete_column(u'api_proteingelspotob', 'ontology_id')

        # Deleting field 'ProteinGelSpotOb.recordeddate'
        db.delete_column(u'api_proteingelspotob', 'recordeddate')

        # Adding field 'MouseWeightOb.obtype'
        db.add_column(u'api_mouseweightob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'MouseWeightOb.ontology'
        db.delete_column(u'api_mouseweightob', 'ontology_id')

        # Deleting field 'MouseWeightOb.recordeddate'
        db.delete_column(u'api_mouseweightob', 'recordeddate')

        # Adding field 'RawImportOb.obtype'
        db.add_column(u'api_rawimportob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'RawImportOb.ontology'
        db.delete_column(u'api_rawimportob', 'ontology_id')

        # Deleting field 'RawImportOb.recordeddate'
        db.delete_column(u'api_rawimportob', 'recordeddate')

        # Adding field 'MouseHistologyV2Ob.obtype'
        db.add_column(u'api_mousehistologyv2ob', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'MouseHistologyV2Ob.ontology'
        db.delete_column(u'api_mousehistologyv2ob', 'ontology_id')

        # Deleting field 'MouseHistologyV2Ob.recordeddate'
        db.delete_column(u'api_mousehistologyv2ob', 'recordeddate')

        # Adding field 'Gene.obtype'
        db.add_column(u'api_gene', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Gene.Ontology'
        db.delete_column(u'api_gene', 'Ontology_id')


        # Changing field 'Gene.lastupdateddate'
        db.alter_column(u'api_gene', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Gene.createddate'
        db.alter_column(u'api_gene', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'Diet.obtype'
        db.add_column(u'api_diet', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Diet.Ontology'
        db.delete_column(u'api_diet', 'Ontology_id')


        # Changing field 'Diet.lastupdateddate'
        db.alter_column(u'api_diet', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Diet.createddate'
        db.alter_column(u'api_diet', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'Tissue.obtype'
        db.add_column(u'api_tissue', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Tissue.Ontology'
        db.delete_column(u'api_tissue', 'Ontology_id')


        # Changing field 'Tissue.lastupdateddate'
        db.alter_column(u'api_tissue', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Tissue.createddate'
        db.alter_column(u'api_tissue', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))
        # Adding field 'BioSubject.obtype'
        db.add_column(u'api_biosubject', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'BioSubject.Ontology'
        db.delete_column(u'api_biosubject', 'Ontology_id')


        # Changing field 'BioSubject.createddate'
        db.alter_column(u'api_biosubject', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'BioSubject.lastupdateddate'
        db.alter_column(u'api_biosubject', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))
        # Adding field 'Genotype.obtype'
        db.add_column(u'api_genotype', 'obtype',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Obtype']),
                      keep_default=False)

        # Deleting field 'Genotype.Ontology'
        db.delete_column(u'api_genotype', 'Ontology_id')


        # Changing field 'Genotype.lastupdateddate'
        db.alter_column(u'api_genotype', 'lastupdateddate', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Genotype.createddate'
        db.alter_column(u'api_genotype', 'createddate', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'api.biosample': {
            'Meta': {'object_name': 'BioSample'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tissue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Tissue']"}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.biosequence': {
            'Meta': {'object_name': 'BioSequence'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'fnindex_accession': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'fnindex_id': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'gi': ('django.db.models.fields.IntegerField', [], {}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'centre': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'changed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cohort': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'do_ignore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
        u'api.crew': {
            'Meta': {'object_name': 'Crew'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crew_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasourcecomment': ('django.db.models.fields.TextField', [], {'default': "'none'"}),
            'datasourcecontent': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'datasourcename': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'datasourcetype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'datasupplieddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasupplier': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'dynamiccontentmethod': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'numberoffiles': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'physicalsourceuri': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'uploadsourceuri': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.diet': {
            'Meta': {'object_name': 'Diet'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.fishob': {
            'Meta': {'object_name': 'FishOb'},
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'form_completed': ('django.db.models.fields.BooleanField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Trip']"}),
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
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.genotype': {
            'Meta': {'object_name': 'Genotype'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
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
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
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
            'omental_fat': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'plasma_cells_and_lymphocytes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.obkv': {
            'Meta': {'object_name': 'ObKV'},
            'att_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'att_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ob_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'api.ontology': {
            'Meta': {'object_name': 'Ontology'},
            'Ontologydescription': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'displayname': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'displayurl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isdynamic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isvirtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'namedinstances': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tablename': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.protein': {
            'Meta': {'object_name': 'Protein'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'prot_ident': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.rawimport': {
            'Meta': {'object_name': 'RawImport'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.species': {
            'Meta': {'object_name': 'Species'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.study': {
            'Meta': {'object_name': 'Study'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyArea']"}),
            'study_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyGroup']"}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studyarea': {
            'Meta': {'object_name': 'StudyArea'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wiki': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.tissue': {
            'Meta': {'object_name': 'Tissue'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.trip': {
            'Meta': {'object_name': 'Trip'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'captain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'first_sailing': ('django.db.models.fields.DateField', [], {}),
            'last_arrival': ('django.db.models.fields.DateField', [], {}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'registration': ('django.db.models.fields.IntegerField', [], {}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'trip_no': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vessel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.unit': {
            'Meta': {'object_name': 'Unit'},
            'Ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']