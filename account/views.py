from django.contrib.auth.models import User, Permission,Group
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required#,user_passes_test,permission_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import password_change
from django.template import RequestContext

def account_login(request):
	errors= []
	account=None
	password=None
	if request.method == 'POST' :
		print request.POST['account']
		if not request.POST.get('account'):
			errors.append('Please Enter account')
		else:
			account = request.POST.get('account')
		if not request.POST.get('password'):
			errors.append('Please Enter password')
		else:
			password= request.POST.get('password')
		if account is not None and password is not None :
			user = authenticate(username=account,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					errors.append('disabled account')
			else :
					errors.append('wrong password')
	return render_to_response('login.html', {'errors': errors},context_instance=RequestContext(request))

@login_required
def account_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required
def account_password_change(request):
	errors = []
	if request.method == 'POST':
		username = request.user
		user_id = request.user.id
		old_password = request.POST['old_password']
		new_password1 = request.POST['new_password1']
		new_password2 = request.POST['new_password2']
		try:
			currentuser = UserProfile.objects.get(id=user_id)
			if currentuser.check_password(old_password):
				if  new_password1 == new_password2:
					#currentuser = UserProfile.objects.get(username__exact=username)
					currentuser.set_password(new_password1)
					currentuser.save()
					logout(request)
					return HttpResponseRedirect('/account/login.html')
				else:
					errors.append('Please input the same password')
			else:
				errors.append('Please correct the old password')
		except UserProfile.DoesNotExist:
			return HttpResponseRedirect('/account/login.html')
	return render_to_response('change_password.html',{'errors':errors},context_instance=RequestContext(request))

@login_required
def account_view_profile(request):
	user = request.user
	return render_to_response('view_profile.html',{'user':user},context_instance=RequestContext(request))