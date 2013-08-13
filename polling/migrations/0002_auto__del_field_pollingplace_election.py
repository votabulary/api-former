# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PollingPlace.election'
        db.delete_column(u'polling_pollingplace', 'election_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PollingPlace.election'
        raise RuntimeError("Cannot reverse this migration. 'PollingPlace.election' and its values cannot be restored.")

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