#CRM

from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User, Group


import datetime

import settings
encoding = settings.ENCODING

class UserProfile(models.Model):	
	user = models.ForeignKey(User, unique = True, db_index = True)
	contact = models.ForeignKey('Contact', null=True, blank=True, related_name="user")

	sees_crm = models.BooleanField(default=False)

	def get_absolute_url(self):
		return ('user_info', (), {
			'username' : self.user.username
		})
	get_absolute_url = permalink(get_absolute_url)

	def __unicode__(self):
		return self.user.get_full_name() or self.user.username

	def get_user_profile(self):
		return ""

class InteractionType(models.Model):
	name=models.CharField(max_length=250)
	def __unicode__(self):
		return self.name

class Interaction(models.Model):
	contact_from = models.ForeignKey('Contact', related_name="contacted")
	contact_to = models.ForeignKey('Contact', related_name="contacted_by")
	means = models.ForeignKey(InteractionType)
	communication = models.TextField(null=True, blank = True)
	time = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "%s -%s-> %s @ %s" % (self.contact_from ,self.means, self.contact_to ,self.time)

class Relationship(models.Model):
	name=models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class ContactRelationship(models.Model):
	contact_from = models.ForeignKey('Contact', related_name = 'relates_to')
	contact_to = models.ForeignKey('Contact', related_name = 'related_to')
	relationship = models.ForeignKey(Relationship)

	def __unicode__(self):
		return "%s -%s-> %s" % (self.contact_from, self.relationship, self.contact_to)

class Social(models.Model):
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name

class Place(models.Model):
	city = models.CharField(max_length=100, verbose_name=_("place"))
	country = models.CharField(max_length=20, verbose_name=_("country"))
        
	def __unicode__(self):
		return "%s, %s" % (self.city, self.country)

class Company(models.Model):
	name = models.CharField(unique=True, max_length=256, verbose_name=_("name"))
	abbreviation = models.CharField(unique=True, max_length=8, verbose_name=_("abbreviation"))
	def __unicode__(self):
            return self.name
        
class CompanyAddress(models.Model):
	company = models.ForeignKey(Company, related_name="addresses")
	address = models.CharField(blank=True, max_length=50, verbose_name=_("address"))
	post_code = models.CharField(blank=True, max_length=50)
	place = models.ForeignKey(Place, verbose_name=_("place"))
	description = models.TextField(blank=True, verbose_name=_("description"))

class CompanyWebsite(models.Model):
	company=models.ForeignKey(Company, related_name="websites")
	address = models.URLField()
	def __unicode__(self):
            return self.address

class CompanySocial(models.Model):
	company = models.ForeignKey(Company, related_name="social")
	medium = models.ForeignKey(Social)
	account = models.URLField()

class CompanyRole(models.Model):
	name = models.CharField(max_length=150)
	def __unicode__(self):
		return self.name


class CompanyArea(models.Model):
	company = models.ForeignKey(Company, related_name="areas")
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name


class Contact(models.Model):
	company = models.ForeignKey(Company, related_name="contacts")
	name = models.CharField(max_length=256)
	surname = models.CharField(max_length = 256)
	active = models.BooleanField(default=True)
	role = models.ForeignKey(CompanyRole) 
	area = models.ForeignKey(CompanyArea, null=True, blank=True)

	def __unicode__(self):
		return "%s %s (%s)" % (self.name, self.surname, self.company)

class ContactEmail(models.Model):
	contact = models.ForeignKey(Contact, related_name="emails")
	address = models.CharField(max_length=256)

class ContactPhoneType(models.Model):
	name = models.CharField(max_length=256)
	def __unicode__(self):
		return self.name

class ContactPhone(models.Model):
	contact = models.ForeignKey(Contact, related_name="phones")
	number = models.CharField(max_length=20)
	phone_type = models.ForeignKey(ContactPhoneType, null=True, blank=True)
	time_available = models.CharField(max_length=20)

class ContactSocial(models.Model):
	contact = models.ForeignKey(Contact, related_name="social")
	medium = models.ForeignKey(Social)
	account = models.URLField()
	

