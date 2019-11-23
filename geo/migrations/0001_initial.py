# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tblgeo'
        db.create_table(u'geo_tblgeo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cohession', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nc', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('d', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('r1', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nq', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('b', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('r2', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nr', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('qu', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'geo', ['tblgeo'])

        # Adding model 'tblendbearing'
        db.create_table(u'geo_tblendbearing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cohession', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nc', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('d', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('r1', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nq', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('b', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('nr', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('qu', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'geo', ['tblendbearing'])

        # Adding model 'tblskincapacity'
        db.create_table(u'geo_tblskincapacity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cohession', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('unit', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('friction', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('r1', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('adhession', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('d', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('off2', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('qs', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'geo', ['tblskincapacity'])


    def backwards(self, orm):
        # Deleting model 'tblgeo'
        db.delete_table(u'geo_tblgeo')

        # Deleting model 'tblendbearing'
        db.delete_table(u'geo_tblendbearing')

        # Deleting model 'tblskincapacity'
        db.delete_table(u'geo_tblskincapacity')


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
            'cohession': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'd': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'friction': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'off2': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'qs': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'r1': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'unit': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'})
        }
    }

    complete_apps = ['geo']