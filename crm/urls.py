from django.conf import settings
from django.conf.urls.defaults import *

from api_urls import v1_api

urlpatterns = patterns('crm',


	url(r'company$', 'views.companies.list', name = "list_companies"),
	url(r'company/(?P<id>\d+)$', 'views.companies.detail', name = "company_details"),
	url(r'company/(?P<company_id>\d+)/contacts$', 'views.contacts.list', name = "contacts_company_list"),

	url(r'contact$', 'views.contacts.list', name = "contacts_list"),
	url(r'contact/(?P<id>\d+)$', 'views.contacts.detail', name = "contact_details"),
	url(r'contact/(?P<id>\d+).vcard$', 'views.contacts.vcard', name = "contact_vcard"),
	url(r'contact/(?P<id>\d+).vcf$', 'views.contacts.vcard', name = "contact_vcf"),
	url(r'api/', include(v1_api.urls)),
		


#		url(r'interaction.wsdl$', 'views.soap.ils', name = "interaction_logging_service"),
	

#	url(r'user$', 'views.users', name = "list_users"),
#	url(r'user/(?P<username>\w+)$', 'views.user.details', name = "user_info"),

#	url(r'form/user$', 'forms.upForm', name = "user_form"),
#	url(r'form/area$', 'forms.aForm', name = "area_form"),
#	url(r'form/place$', 'forms.pForm', name = "place_form"),
#	url(r'form/company$', 'forms.cForm', name = "company_form"),
)
