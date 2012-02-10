from django.http import HttpResponse
from crm.models import *

try:
	import json
except:
	import simplejson as json

def list(request):
	j = [{'name':str(c), 'id':c.id} for c in Company.objects.all()]
	return HttpResponse(json.dumps(j))

def detail(request, id):
	c = Company.objects.get(id=id)
	data = {
		'name':c.name,
		'abbreviation':c.abbreviation,
		'addresses':[{'address':a.address, 'postcoode':a.post_code, 'city':str(a.place)} for a in c.addresses.all()],
		'websites':[{'url':w.address} for w in c.websites.all()],
		'social':[{'account':str(s.medium), 'url':s.account} for s in c.social.all()],
		'contacts':[{'name':co.name, 'surname':co.surname, 'role':str(co.role), 'area':str(co.area), 'id':co.id} for co in c.contacts.filter(active=True)]
	}
	return HttpResponse(json.dumps(data))