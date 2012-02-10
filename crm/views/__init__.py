import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from crm.models import *

try:
        import json
except:
        import simplejson as json
	
#------------------------------------------------------------------------------

def details(request):

	context = {
		'subject': unicode(request.user),
		'date': datetime.date.today(),
		'urn': "users/%s" % request.user.id
	}
	return render_to_response('resource_details.html', context, context_instance = RequestContext(request))

#------------------------------------------------------------------------------

def get_user_messages(request):
	return render_to_response('user_messages.html', context = {}, context_instance = RequestContext(request))

@login_required
def users(request):
        u = request.user
        users = [{"username": user.user.username, "fullname":user.user.get_full_name(), 'profile':user.get_user_profile()} for user in UserProfile.objects.filter(manager = UserProfile.objects.get(user = u).manager).exclude(user__is_active = False)]
        return HttpResponse(json.dumps(users))

