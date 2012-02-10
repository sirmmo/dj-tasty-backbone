from django.forms import ModelForm

from crm.models import *
from task.models import *
class AreaForm(ModelForm):
	class Meta:
		model = Area

class UserProfileForm(ModelForm):
        class Meta:
                model = UserProfile

class PlaceForm(ModelForm):
	class Meta:
		model = Place

class CompanyForm(ModelForm):
	class Meta:
		model = Company

class ProjectForm(ModelForm):
	class Meta:
		model = Project

def aForm(request):
        if request.method == 'POST': # If the form has been submitted...
                form = AreaForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                #form.cleaned_data
                        return HttpResponse('Ok') # Redirect after POST
        else:
                form = AreaForm() # An unbound form

        return render_to_response('inner_form.html', {
                'form': form,
        })

def upForm(request):
        if request.method == 'POST': # If the form has been submitted...
                form = AreaForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                #form.cleaned_data
                        return HttpResponse('Ok') # Redirect after POST
        else:
                form = AreaForm() # An unbound form

        return render_to_response('inner_form.html', {
                'form': form,
        })

def pForm(request):
        if request.method == 'POST': # If the form has been submitted...
                form = AreaForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                #form.cleaned_data
                        return HttpResponse('Ok') # Redirect after POST
        else:
                form = AreaForm() # An unbound form

        return render_to_response('inner_form.html', {
                'form': form,
        })

def cForm(request):
        if request.method == 'POST': # If the form has been submitted...
                form = AreaForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                #form.cleaned_data
                        return HttpResponse('Ok') # Redirect after POST
        else:
                form = AreaForm() # An unbound form

        return render_to_response('inner_form.html', {
                'form': form,
        })

def prjForm(request):
        if request.method == 'POST': # If the form has been submitted...
                form = AreaForm(request.POST) # A form bound to the POST data
                if form.is_valid(): # All validation rules pass
                #form.cleaned_data
                        return HttpResponse('Ok') # Redirect after POST
        else:
                form = AreaForm() # An unbound form

        return render_to_response('inner_form.html', {
                'form': form,
        })
