# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'County'
        db.create_table(u'polling_county', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'polling', ['County'])

        # Adding model 'Election'
        db.create_table(u'polling_election', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.County'])),
            ('election_date', self.gf('django.db.models.fields.DateField')()),
            ('voting_rule', self.gf('django.db.models.fields.CharField')(default='VP', max_length=2)),
        ))
        db.send_create_signal(u'polling', ['Election'])

        # Adding model 'Precinct'
        db.create_table(u'polling_precinct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'polling', ['Precinct'])

        # Adding model 'PollingPlace'
        db.create_table(u'polling_pollingplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Address'])),
        ))
        db.send_create_signal(u'polling', ['PollingPlace'])

        # Adding model 'Address'
        db.create_table(u'polling_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address_line3', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address_line4', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(default='TX', max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('country', self.gf('django.db.models.fields.CharField')(default='US', max_length=2)),
        ))
        db.send_create_signal(u'polling', ['Address'])


    def backwards(self, orm):
        # Deleting model 'County'
        db.delete_table(u'polling_county')

        # Deleting model 'Election'
        db.delete_table(u'polling_election')

        # Deleting model 'Precinct'
        db.delete_table(u'polling_precinct')

        # Deleting model 'PollingPlace'
        db.delete_table(u'polling_pollingplace')

        # Deleting model 'Address'
        db.delete_table(u'polling_address')


    models = {
        u'polling.address': {
            'Meta': {'object_name': 'Address'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'address_line4': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'US'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'TX'", 'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        u'polling.county': {
            'Meta': {'object_name': 'County'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'polling.election': {
            'Meta': {'object_name': 'Election'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.County']"}),
            'election_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voting_rule': ('django.db.models.fields.CharField', [], {'default': "'VP'", 'max_length': '2'})
        },
        u'polling.pollingplace': {
            'Meta': {'object_name': 'PollingPlace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Address']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'polling.precinct': {
            'Meta': {'object_name': 'Precinct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polling']