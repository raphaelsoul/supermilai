from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import django

@login_required
#@somedecorate
def index(request):
	return render_to_response('home_page.html', context_instance=RequestContext(request))


def django_version(request):
	return HttpResponse('Django Version = ' + str(django.VERSION))
