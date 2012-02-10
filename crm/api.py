from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields

from crm.models import *

global_auth = Authorization

class UserProfileResource(ModelResource):
	class Meta:
		queryset = UserProfile.objects.all()
		resource_name = "profile"
		authorization = global_auth()

class InteractionResource(ModelResource):
	class Meta:
		queryset = Interaction.objects.all()
		resource_name = "i"
		authorization = global_auth()

class RelationshipResource(ModelResource):
	class Meta:
		queryset = Relationship.objects.all()
		resource_name = "rel"
		authorization = global_auth()

class ContactRelationshipResource(ModelResource):
	contact_from = fields.ToOneField('crm.api.ContactResource', 'contact_from')
	contact_to = fields.ToOneField('crm.api.ContactResource', 'contact_to')
	relationship = fields.ToOneField('crm.api.RelationshipResource', 'relationship', full=True)
	
	class Meta:
		queryset = ContactRelationship.objects.all()
		resource_name = "cr"
		authorization = global_auth()

class CompanyResource(ModelResource):
	addresses = fields.ToManyField('crm.api.CompanyAddressResource', 'addresses', full=True, extras={'type':"List"})
	websites = fields.ToManyField('crm.api.CompanyWebsiteResource', 'websites', full=True, extras={'type':"List"})
	contacts = fields.ToManyField('crm.api.ContactResource', 'contacts', full=True, extras={'type':"List"})
	socials = fields.ToManyField('crm.api.ContactSocialResource', 'social', full=True, extras={'type':"List"})
	areas = fields.ToManyField('crm.api.CompanyAreaResource', 'areas', full=True, extras={'type':"List"})
	
	class Meta:
		queryset = Company.objects.all()
		resource_name = "company"
		authorization = global_auth()

class PlaceResource(ModelResource):
	class Meta:
		queryset = Place.objects.all()
		resource_name = "place"
		authorization = global_auth()

class CompanyAddressResource(ModelResource):
	place = fields.ToOneField('crm.api.PlaceResource', 'place', full=True, extras={ 'type': 'NestedModel', 'model': 'Place' },)
	class Meta:
		queryset = CompanyAddress.objects.all()
		resource_name = "company_address"
		authorization = global_auth()

class CompanyWebsiteResource(ModelResource):

	class Meta:
		queryset = CompanyWebsite.objects.all()
		resource_name = "company_website"
		authorization = global_auth()

class CompanySocialResource(ModelResource):

	class Meta:
		queryset = CompanySocial.objects.all()
		resource_name = "company_social"
		authorization = global_auth()

class CompanyRoleResource(ModelResource):

	class Meta:
		queryset = CompanyRole.objects.all()
		resource_name = "company_role"
		authorization = global_auth()

class CompanyAreaResource(ModelResource):

	class Meta:
		queryset = CompanyArea.objects.all()
		resource_name = "company_area"
		authorization = global_auth()


class ContactResource(ModelResource):
	emails = fields.ToManyField('crm.api.ContactEmailResource', 'emails', full=True)
	phones = fields.ToManyField('crm.api.ContactPhoneResource', 'phones', full=True)
	social = fields.ToManyField('crm.api.ContactSocialResource', 'social', full=True)

	class Meta:
		queryset = Contact.objects.all()
		resource_name = "contact"
		authorization = global_auth()

class ContactEmailResource(ModelResource):
	class Meta:
		queryset = ContactEmail.objects.all()
		resource_name = "contact_email"
		authorization = global_auth()

class ContactPhoneResource(ModelResource):
	class Meta:
		queryset = ContactPhone.objects.all()
		resource_name = "contact_phone"
		authorization = global_auth()

class ContactSocialResource(ModelResource):
	class Meta:
		queryset = ContactSocial.objects.all()
		resource_name = "contact_social"
		authorization = global_auth()

