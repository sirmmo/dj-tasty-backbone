from lib.soap import DjangoSoapApp, soapmethod, soap_types
from django.contrib.auth.decorators import login_required

from crm.models import *

class InteractionLoggingService(DjangoSoapApp):

	__tns__ = 'http://www.labs.it/soap/'

	@login_required
	@soapmethod(soap_types.String,soap_types.String,soap_types.String,soap_types.String,soap_types.String, soap_types.String, soap_types.String, soap_types.String, soap_types.String, _returns=soap_types.Boolean)
	def log_interaction(self, name_F, surname_F, means_F, name_T, surname_T, means_T, company, time, content=Null):
		i = Interaction()
		i.contact_from = Contact.objects.filter(name=name_F, surname=surname_F, company=company_F)[0]
		i.contact_to = Contact.objects.filter(name=name_T, surname=surname_T, company=company_T)[0]
		i.means = InteractionType.objects.get(name=means)
		i.time = time
		i.communication = content

		i.save()

		


ils = InteractionLoggingService() 