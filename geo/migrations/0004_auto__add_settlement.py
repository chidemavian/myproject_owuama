# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'settlement'
        db.create_table(u'geo_settlement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compression', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('void', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('unit', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('thick', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('off2', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('off1', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('d', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('pressure', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'geo', ['settlement'])


    def backwards(self, orm):
        # Deleting model 'settlement'
        db.delete_table(u'geo_settlement')


    models = {
        u'geo.settlement': {
            'Meta': {'object_name': 'settlement'},
            'compression': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'd': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'off1': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'off2': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'pressure': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'thick': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'void': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        },
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
            'qs': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        }
    }

    complete_apps = ['geo']