from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def doc_developer(request):
	return render_to_response('doc_developer.html')

@login_required
def doc_user(request):
	return render_to_response('doc_user.html')