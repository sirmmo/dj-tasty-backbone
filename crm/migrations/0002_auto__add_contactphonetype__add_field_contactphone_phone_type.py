# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContactPhoneType'
        db.create_table('crm_contactphonetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('crm', ['ContactPhoneType'])

        # Adding field 'ContactPhone.phone_type'
        db.add_column('crm_contactphone', 'phone_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.ContactPhoneType'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'ContactPhoneType'
        db.delete_table('crm_contactphonetype')

        # Deleting field 'ContactPhone.phone_type'
        db.delete_column('crm_contactphone', 'phone_type_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crm.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crm.company': {
            'Meta': {'object_name': 'Company'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        'crm.companyaddress': {
            'Meta': {'object_name': 'CompanyAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Place']"}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'crm.companyrole': {
            'Meta': {'object_name': 'CompanyRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'crm.companysocial': {
            'Meta': {'object_name': 'CompanySocial'},
            'account': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Social']"})
        },
        'crm.companywebsite': {
            'Meta': {'object_name': 'CompanyWebsite'},
            'address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.CompanyRole']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'crm.contactemail': {
            'Meta': {'object_name': 'ContactEmail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.contactphone': {
            'Meta': {'object_name': 'ContactPhone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.ContactPhoneType']", 'null': 'True', 'blank': 'True'}),
            'time_available': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'crm.contactphonetype': {
            'Meta': {'object_name': 'ContactPhoneType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'crm.contactsocial': {
            'Meta': {'object_name': 'ContactSocial'},
            'account': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Social']"})
        },
        'crm.place': {
            'Meta': {'object_name': 'Place'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crm.social': {
            'Meta': {'object_name': 'Social'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'crm.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crm.Area']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['crm']
