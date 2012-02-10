# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Area'
        db.create_table('crm_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('crm', ['Area'])

        # Adding model 'UserProfile'
        db.create_table('crm_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Area'], null=True, blank=True)),
        ))
        db.send_create_signal('crm', ['UserProfile'])

        # Adding model 'Social'
        db.create_table('crm_social', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('crm', ['Social'])

        # Adding model 'Place'
        db.create_table('crm_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('crm', ['Place'])

        # Adding model 'Company'
        db.create_table('crm_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
        ))
        db.send_create_signal('crm', ['Company'])

        # Adding model 'CompanyAddress'
        db.create_table('crm_companyaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Company'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Place'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('crm', ['CompanyAddress'])

        # Adding model 'CompanyWebsite'
        db.create_table('crm_companywebsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Company'])),
            ('address', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('crm', ['CompanyWebsite'])

        # Adding model 'CompanySocial'
        db.create_table('crm_companysocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Company'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Social'])),
            ('account', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('crm', ['CompanySocial'])

        # Adding model 'CompanyRole'
        db.create_table('crm_companyrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('crm', ['CompanyRole'])

        # Adding model 'Contact'
        db.create_table('crm_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.CompanyRole'])),
        ))
        db.send_create_signal('crm', ['Contact'])

        # Adding model 'ContactEmail'
        db.create_table('crm_contactemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('crm', ['ContactEmail'])

        # Adding model 'ContactPhone'
        db.create_table('crm_contactphone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('time_available', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('crm', ['ContactPhone'])

        # Adding model 'ContactSocial'
        db.create_table('crm_contactsocial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Contact'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Social'])),
            ('account', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('crm', ['ContactSocial'])


    def backwards(self, orm):
        
        # Deleting model 'Area'
        db.delete_table('crm_area')

        # Deleting model 'UserProfile'
        db.delete_table('crm_userprofile')

        # Deleting model 'Social'
        db.delete_table('crm_social')

        # Deleting model 'Place'
        db.delete_table('crm_place')

        # Deleting model 'Company'
        db.delete_table('crm_company')

        # Deleting model 'CompanyAddress'
        db.delete_table('crm_companyaddress')

        # Deleting model 'CompanyWebsite'
        db.delete_table('crm_companywebsite')

        # Deleting model 'CompanySocial'
        db.delete_table('crm_companysocial')

        # Deleting model 'CompanyRole'
        db.delete_table('crm_companyrole')

        # Deleting model 'Contact'
        db.delete_table('crm_contact')

        # Deleting model 'ContactEmail'
        db.delete_table('crm_contactemail')

        # Deleting model 'ContactPhone'
        db.delete_table('crm_contactphone')

        # Deleting model 'ContactSocial'
        db.delete_table('crm_contactsocial')


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
            'time_available': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
