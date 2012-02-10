from django.http import HttpResponse
from crm.models import *

try:
	import json
except:
	import simplejson as json

def list(request, company_id=None):
	if company_id:
		qq = Contact.objects.filter(company__id=company_id)
	else:
		qq = Contact.objects.all()

	j = [{
		'name':c.name, 
		'surname':c.surname,
		'company':{
			'name':str(c.company),
			'id':c.company.id
		},
		'role':str(c.role),
		'id':c.id
		} for c in qq]
	return HttpResponse(json.dumps(j))

def detail(request, id):
	qq = Contact.objects.get(id=id)
	data = {
		'name':qq.name,
		'surname':qq.surname,
		'role':str(qq.role),
		'area':str(qq.area),
		'emails':[e.address for e in qq.emails.all()],
		'phones':[{'type':str(p.phone_type), 'number':p.number} for p in qq.phones.all()],
		'social':[{'type':str(p.medium ), 'number':p.account } for p in qq.social.all()],
		'relationships':{
			'from':[{}for r in qq.relates_to.all()],
			'to':[{}for r in qq.related_to.all()],
		}
	}
	return HttpResponse(json.dumps(data))

def vcard(request, id):
	import vobject
	qq = Contact.objects.get(id=id)
	card = vobject.vCard()
	card.add('n')
	card.n.value=vobject.vcard.Name(family=qq.surname, given=qq.name)
	card.add('fn')
	card.fn.value="%s %s" % (qq.name, qq.surname,)
	ei = 0
	for e in qq.emails.all():
		card.add('email')
		card.email_list[ei].value=e.address
		card.email_list[ei].type_param ='INTERNET'
	pi = 0
	for p in qq.phones.all():
		card.add('tel')	
		card.tel_list[pi].type_param=str(p.phone_type)
		card.tel_list[pi].value=p.number
		pi = pi + 1
	card.add('org')
	card.org.value = [str(qq.company)]
	card.add('title')
	card.title.value = str(qq.role)

	return HttpResponse(card.serialize())#, content_type = "text/vcard")