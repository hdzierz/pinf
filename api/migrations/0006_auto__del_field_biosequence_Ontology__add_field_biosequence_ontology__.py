# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BioSequence.Ontology'
        db.delete_column(u'api_biosequence', 'Ontology_id')

        # Adding field 'BioSequence.ontology'
        db.add_column(u'api_biosequence', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Protein.Ontology'
        db.delete_column(u'api_protein', 'Ontology_id')

        # Adding field 'Protein.ontology'
        db.add_column(u'api_protein', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'StudyGroup.Ontology'
        db.delete_column(u'api_studygroup', 'Ontology_id')

        # Adding field 'StudyGroup.ontology'
        db.add_column(u'api_studygroup', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'BioSample.Ontology'
        db.delete_column(u'api_biosample', 'Ontology_id')

        # Adding field 'BioSample.ontology'
        db.add_column(u'api_biosample', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Species.Ontology'
        db.delete_column(u'api_species', 'Ontology_id')

        # Adding field 'Species.ontology'
        db.add_column(u'api_species', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'DataSource.Ontology'
        db.delete_column(u'api_datasource', 'Ontology_id')

        # Adding field 'DataSource.ontology'
        db.add_column(u'api_datasource', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'StudyArea.Ontology'
        db.delete_column(u'api_studyarea', 'Ontology_id')

        # Adding field 'StudyArea.ontology'
        db.add_column(u'api_studyarea', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Labresource.Ontology'
        db.delete_column(u'api_labresource', 'Ontology_id')

        # Adding field 'Labresource.ontology'
        db.add_column(u'api_labresource', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Crew.Ontology'
        db.delete_column(u'api_crew', 'Ontology_id')

        # Adding field 'Crew.ontology'
        db.add_column(u'api_crew', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Study.Ontology'
        db.delete_column(u'api_study', 'Ontology_id')

        # Adding field 'Study.ontology'
        db.add_column(u'api_study', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Trip.Ontology'
        db.delete_column(u'api_trip', 'Ontology_id')

        # Adding field 'Trip.ontology'
        db.add_column(u'api_trip', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Unit.Ontology'
        db.delete_column(u'api_unit', 'Ontology_id')

        # Adding field 'Unit.ontology'
        db.add_column(u'api_unit', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'RawImport.Ontology'
        db.delete_column(u'api_rawimport', 'Ontology_id')

        # Adding field 'RawImport.ontology'
        db.add_column(u'api_rawimport', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Gene.Ontology'
        db.delete_column(u'api_gene', 'Ontology_id')

        # Adding field 'Gene.ontology'
        db.add_column(u'api_gene', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Diet.Ontology'
        db.delete_column(u'api_diet', 'Ontology_id')

        # Adding field 'Diet.ontology'
        db.add_column(u'api_diet', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Tissue.Ontology'
        db.delete_column(u'api_tissue', 'Ontology_id')

        # Adding field 'Tissue.ontology'
        db.add_column(u'api_tissue', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'BioSubject.Ontology'
        db.delete_column(u'api_biosubject', 'Ontology_id')

        # Adding field 'BioSubject.ontology'
        db.add_column(u'api_biosubject', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Genotype.Ontology'
        db.delete_column(u'api_genotype', 'Ontology_id')

        # Adding field 'Genotype.ontology'
        db.add_column(u'api_genotype', 'ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BioSequence.Ontology'
        db.add_column(u'api_biosequence', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'BioSequence.ontology'
        db.delete_column(u'api_biosequence', 'ontology_id')

        # Adding field 'Protein.Ontology'
        db.add_column(u'api_protein', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Protein.ontology'
        db.delete_column(u'api_protein', 'ontology_id')

        # Adding field 'StudyGroup.Ontology'
        db.add_column(u'api_studygroup', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'StudyGroup.ontology'
        db.delete_column(u'api_studygroup', 'ontology_id')

        # Adding field 'BioSample.Ontology'
        db.add_column(u'api_biosample', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'BioSample.ontology'
        db.delete_column(u'api_biosample', 'ontology_id')

        # Adding field 'Species.Ontology'
        db.add_column(u'api_species', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Species.ontology'
        db.delete_column(u'api_species', 'ontology_id')

        # Adding field 'DataSource.Ontology'
        db.add_column(u'api_datasource', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'DataSource.ontology'
        db.delete_column(u'api_datasource', 'ontology_id')

        # Adding field 'StudyArea.Ontology'
        db.add_column(u'api_studyarea', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'StudyArea.ontology'
        db.delete_column(u'api_studyarea', 'ontology_id')

        # Adding field 'Labresource.Ontology'
        db.add_column(u'api_labresource', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Labresource.ontology'
        db.delete_column(u'api_labresource', 'ontology_id')

        # Adding field 'Crew.Ontology'
        db.add_column(u'api_crew', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Crew.ontology'
        db.delete_column(u'api_crew', 'ontology_id')

        # Adding field 'Study.Ontology'
        db.add_column(u'api_study', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Study.ontology'
        db.delete_column(u'api_study', 'ontology_id')

        # Adding field 'Trip.Ontology'
        db.add_column(u'api_trip', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Trip.ontology'
        db.delete_column(u'api_trip', 'ontology_id')

        # Adding field 'Unit.Ontology'
        db.add_column(u'api_unit', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Unit.ontology'
        db.delete_column(u'api_unit', 'ontology_id')

        # Adding field 'RawImport.Ontology'
        db.add_column(u'api_rawimport', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'RawImport.ontology'
        db.delete_column(u'api_rawimport', 'ontology_id')

        # Adding field 'Gene.Ontology'
        db.add_column(u'api_gene', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Gene.ontology'
        db.delete_column(u'api_gene', 'ontology_id')

        # Adding field 'Diet.Ontology'
        db.add_column(u'api_diet', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Diet.ontology'
        db.delete_column(u'api_diet', 'ontology_id')

        # Adding field 'Tissue.Ontology'
        db.add_column(u'api_tissue', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Tissue.ontology'
        db.delete_column(u'api_tissue', 'ontology_id')

        # Adding field 'BioSubject.Ontology'
        db.add_column(u'api_biosubject', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'BioSubject.ontology'
        db.delete_column(u'api_biosubject', 'ontology_id')

        # Adding field 'Genotype.Ontology'
        db.add_column(u'api_genotype', 'Ontology',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['api.Ontology']),
                      keep_default=False)

        # Deleting field 'Genotype.ontology'
        db.delete_column(u'api_genotype', 'ontology_id')


    models = {
        u'api.biosample': {
            'Meta': {'object_name': 'BioSample'},
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tissue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Tissue']"}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.biosequence': {
            'Meta': {'object_name': 'BioSequence'},
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'do_ignore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.datasource': {
            'Meta': {'object_name': 'DataSource'},
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'physicalsourceuri': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'uploadsourceuri': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.diet': {
            'Meta': {'object_name': 'Diet'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.genotype': {
            'Meta': {'object_name': 'Genotype'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ob_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Ontology']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '10240'})
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
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.study': {
            'Meta': {'object_name': 'Study'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wiki': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.studygroup': {
            'Meta': {'object_name': 'StudyGroup'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Species']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.tissue': {
            'Meta': {'object_name': 'Tissue'},
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.trip': {
            'Meta': {'object_name': 'Trip'},
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
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
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
            'alias': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'createdby': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createddate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'lastupdatedby': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastupdateddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '255'}),
            'obid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obkeywords': ('django.db.models.fields.TextField', [], {}),
            'ontology': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['api.Ontology']"}),
            'statuscode': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'xreflsid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['api']