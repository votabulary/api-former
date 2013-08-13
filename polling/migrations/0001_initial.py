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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('state', self.gf('django.db.models.fields.CharField')(default='TX', max_length=2)),
        ))
        db.send_create_signal(u'polling', ['County'])

        # Adding model 'Voter'
        db.create_table(u'polling_voter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.County'])),
            ('precinct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Precinct'])),
            ('email_voting_reminders', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_voting_reminders', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'polling', ['Voter'])

        # Adding model 'Election'
        db.create_table(u'polling_election', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.County'])),
            ('early_voting_start_date', self.gf('django.db.models.fields.DateField')()),
            ('early_voting_end_date', self.gf('django.db.models.fields.DateField')()),
            ('voting_date', self.gf('django.db.models.fields.DateField')()),
            ('voting_rule', self.gf('django.db.models.fields.CharField')(default='VP', max_length=2)),
        ))
        db.send_create_signal(u'polling', ['Election'])

        # Adding model 'VoterElection'
        db.create_table(u'polling_voterelection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Voter'])),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Election'])),
            ('has_voted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'polling', ['VoterElection'])

        # Adding model 'Precinct'
        db.create_table(u'polling_precinct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.County'])),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'polling', ['Precinct'])

        # Adding model 'PollingPlace'
        db.create_table(u'polling_pollingplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Address'])),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Election'])),
        ))
        db.send_create_signal(u'polling', ['PollingPlace'])

        # Adding model 'ElectionPrecinctPollingPlace'
        db.create_table(u'polling_electionprecinctpollingplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('election', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Election'])),
            ('precinct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.Precinct'])),
            ('polling_place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polling.PollingPlace'])),
        ))
        db.send_create_signal(u'polling', ['ElectionPrecinctPollingPlace'])

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

        # Deleting model 'Voter'
        db.delete_table(u'polling_voter')

        # Deleting model 'Election'
        db.delete_table(u'polling_election')

        # Deleting model 'VoterElection'
        db.delete_table(u'polling_voterelection')

        # Deleting model 'Precinct'
        db.delete_table(u'polling_precinct')

        # Deleting model 'PollingPlace'
        db.delete_table(u'polling_pollingplace')

        # Deleting model 'ElectionPrecinctPollingPlace'
        db.delete_table(u'polling_electionprecinctpollingplace')

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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'TX'", 'max_length': '2'})
        },
        u'polling.election': {
            'Meta': {'object_name': 'Election'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.County']"}),
            'early_voting_end_date': ('django.db.models.fields.DateField', [], {}),
            'early_voting_start_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voting_date': ('django.db.models.fields.DateField', [], {}),
            'voting_rule': ('django.db.models.fields.CharField', [], {'default': "'VP'", 'max_length': '2'})
        },
        u'polling.electionprecinctpollingplace': {
            'Meta': {'object_name': 'ElectionPrecinctPollingPlace'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polling_place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.PollingPlace']"}),
            'precinct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Precinct']"})
        },
        u'polling.pollingplace': {
            'Meta': {'object_name': 'PollingPlace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Address']"}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'polling.precinct': {
            'Meta': {'object_name': 'Precinct'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.County']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'polling.voter': {
            'Meta': {'object_name': 'Voter'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.County']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'email_voting_reminders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile_voting_reminders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'precinct': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Precinct']"})
        },
        u'polling.voterelection': {
            'Meta': {'object_name': 'VoterElection'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Election']"}),
            'has_voted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polling.Voter']"})
        }
    }

    complete_apps = ['polling']