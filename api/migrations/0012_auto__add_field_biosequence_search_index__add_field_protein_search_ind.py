# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BioSequence.search_index'
        db.add_column(u'api_biosequence', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Protein.search_index'
        db.add_column(u'api_protein', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'StudyGroup.search_index'
        db.add_column(u'api_studygroup', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'BioSample.search_index'
        db.add_column(u'api_biosample', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Species.search_index'
        db.add_column(u'api_species', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'City.search_index'
        db.add_column(u'api_city', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'StudyArea.search_index'
        db.add_column(u'api_studyarea', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Labresource.search_index'
        db.add_column(u'api_labresource', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Crew.search_index'
        db.add_column(u'api_crew', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Study.search_index'
        db.add_column(u'api_study', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Unit.search_index'
        db.add_column(u'api_unit', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'RawImport.search_index'
        db.add_column(u'api_rawimport', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Gene.search_index'
        db.add_column(u'api_gene', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Diet.search_index'
        db.add_column(u'api_diet', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Tissue.search_index'
        db.add_column(u'api_tissue', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'BioSubject.search_index'
        db.add_column(u'api_biosubject', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Genotype.search_index'
        db.add_column(u'api_genotype', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BioSequence.search_index'
        db.delete_column(u'api_biosequence', 'search_index')

        # Deleting field 'Protein.search_index'
        db.delete_column(u'api_protein', 'search_index')

        # Deleting field 'StudyGroup.search_index'
        db.delete_column(u'api_studygroup', 'search_index')

        # Deleting field 'BioSample.search_index'
        db.delete_column(u'api_biosample', 'search_index')

        # Deleting field 'Species.search_index'
        db.delete_column(u'api_species', 'search_index')

        # Deleting field 'City.search_index'
        db.delete_column(u'api_city', 'search_index')

        # Deleting field 'StudyArea.search_index'
        db.delete_column(u'api_studyarea', 'search_index')

        # Deleting field 'Labresource.search_index'
        db.delete_column(u'api_labresource', 'search_index')

        # Deleting field 'Crew.search_index'
        db.delete_column(u'api_crew', 'search_index')

        # Deleting field 'Study.search_index'
        db.delete_column(u'api_study', 'search_index')

        # Deleting field 'Unit.search_index'
        db.delete_column(u'api_unit', 'search_index')

        # Deleting field 'RawImport.search_index'
        db.delete_column(u'api_rawimport', 'search_index')

        # Deleting field 'Gene.search_index'
        db.delete_column(u'api_gene', 'search_index')

        # Deleting field 'Diet.search_index'
        db.delete_column(u'api_diet', 'search_index')

        # Deleting field 'Tissue.search_index'
        db.delete_column(u'api_tissue', 'search_index')

        # Deleting field 'BioSubject.search_index'
        db.delete_column(u'api_biosubject', 'search_index')

        # Deleting field 'Genotype.search_index'
        db.delete_column(u'api_genotype', 'search_index')


    models = {
        u'api.biosample': {
            'Meta': {'object_name': 'BioSample'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'biosubject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.BioSubject']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tissue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Tissue']"}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.biosequence': {
            'Meta': {'object_name': 'BioSequence'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'fnindex_accession': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'fnindex_id': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'gi': ('django.db.models.fields.IntegerField', [], {}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'string': ('django.db.models.fields.TextField', [], {}),
            'topology': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
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
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'do_ignore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
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
        u'api.city': {
            'Meta': {'object_name': 'City'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'orig_city_id': ('django.db.models.fields.IntegerField', [], {}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.crew': {
            'Meta': {'object_name': 'Crew'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'deleted_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "'none'", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'numberoffiles': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'physicalsourceuri': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'supplieddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '2048', 'null': 'True'}),
            'typ': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '256', 'null': 'True'}),
            'uploadsourceuri': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048', 'null': 'True'})
        },
        u'api.diet': {
            'Meta': {'object_name': 'Diet'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'island': ('django.db.models.fields.CharField', [], {'default': "'CpG_unkown'", 'max_length': '255'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'methylation': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'week': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.fishob': {
            'Meta': {'object_name': 'FishOb'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.City']"}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'form_completed': ('django.db.models.fields.BooleanField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'obkv': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.ObKV']"}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.genotype': {
            'Meta': {'object_name': 'Genotype'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'observationdate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'seqlength': ('django.db.models.fields.IntegerField', [], {}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'supplier': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inflam_type': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lymphoid_aggregates': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'monocytes_and_macrophages': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'muscular_layer': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'neutrophils': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'omental_fat': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'plasma_cells_and_lymphocytes': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intake': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Unit']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.obkv': {
            'Meta': {'object_name': 'ObKV'},
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('jsonfield.fields.JSONField', [], {})
        },
        u'api.ontology': {
            'Meta': {'object_name': 'Ontology'},
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048', 'null': 'True'}),
            'displayurl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'owner': ('django.db.models.fields.CharField', [], {'default': "'core'", 'max_length': '128', 'null': 'True'}),
            'tablename': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'api.protein': {
            'Meta': {'object_name': 'Protein'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'num_uniq_pep': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'prot_ident': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.rawimport': {
            'Meta': {'object_name': 'RawImport'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.RawImport']"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.species': {
            'Meta': {'object_name': 'Species'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.study': {
            'Meta': {'object_name': 'Study'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study_area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyArea']"}),
            'study_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.StudyGroup']"}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studyarea': {
            'Meta': {'object_name': 'StudyArea'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wiki': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.tissue': {
            'Meta': {'object_name': 'Tissue'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.trip': {
            'Meta': {'object_name': 'Trip'},
            'captain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'default': 'None', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.DataSource']", 'null': 'True'}),
            'deleted': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'first_sailing': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'NA'", 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_arrival': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'orig_trip_id': ('django.db.models.fields.IntegerField', [], {}),
            'recordeddate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'registration': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Study']", 'null': 'True'}),
            'trip_no': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'vessel': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        u'api.unit': {
            'Meta': {'object_name': 'Unit'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasource': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']