# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'tblskincapacity.cohession'
        db.delete_column(u'geo_tblskincapacity', 'cohession')

        # Deleting field 'tblskincapacity.r1'
        db.delete_column(u'geo_tblskincapacity', 'r1')

        # Adding field 'tblskincapacity.frictionangle'
        db.add_column(u'geo_tblskincapacity', 'frictionangle',
                      self.gf('django.db.models.fields.DecimalField')(default='4.4', max_digits=15, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'tblskincapacity.cohession'
        db.add_column(u'geo_tblskincapacity', 'cohession',
                      self.gf('django.db.models.fields.DecimalField')(default='43.3', max_digits=15, decimal_places=2),
                      keep_default=False)

        # Adding field 'tblskincapacity.r1'
        db.add_column(u'geo_tblskincapacity', 'r1',
                      self.gf('django.db.models.fields.DecimalField')(default='3.4', max_digits=15, decimal_places=2),
                      keep_default=False)

        # Deleting field 'tblskincapacity.frictionangle'
        db.delete_column(u'geo_tblskincapacity', 'frictionangle')


    models = {
        u'geo.tblendbearing': {
            'Meta': {'object_name': 'tblendbearing'},
            'b': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'cohession': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'd': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nc': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'nq': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'nr': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'qu': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'r1': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
        u'geo.tblgeo': {
            'Meta': {'object_name': 'tblgeo'},
            'b': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'cohession': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'd': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nc': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'nq': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'nr': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'qu': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'r1': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'r2': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
        u'geo.tblskincapacity': {
            'Meta': {'object_name': 'tblskincapacity'},
            'adhession': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'd': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'friction': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'frictionangle': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'off2': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'qs': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        }
    }

    complete_apps = ['geo']