import datetime

#from crm.models import *

#from django.contrib.auth.models import *

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import smart_str

try:
        import json
except:
        import simplejson as json
        
#def details(request, username):
#	user = get_object_or_404(User, username = username)
#	context = {
#		'username': user.username,
#                'fullname': user.get_full_name(),
#                'projects': [{
#                        "project": proj.project.name,
#                        "leader": proj.leader,
#                        'url':proj.project.get_absolute_url()
#                } for proj in UserProject.objects.filter(user = user)]
#	}
#	return HttpResponse(json.dumps(context))
