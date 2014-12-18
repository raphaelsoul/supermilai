from django.contrib.auth.models import User, Permission,Group
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required#,user_passes_test,permission_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import password_change
from models import UserProfile
from django.template import RequestContext
from django.contrib.contenttypes.models import ContentType

@login_required
def user_list(request):
	users = UserProfile.objects.all()
	groups = Group.objects.all()
	return render_to_response(
		'user_list.html',
		{'users':users,'groups':groups},
		context_instance=RequestContext(request)
		)

@login_required
@permission_required('account.change_userprofile',login_url='/403.html')
def user_modify(request,id):
	user_to_modify = UserProfile.objects.get(pk=id)
	if request.method == 'POST':
		truename = request.POST['truename']
		email = request.POST['email']
		qq = request.POST['qq']
		user_to_modify = UserProfile.objects.get(pk=id)
		user_to_modify.truename = truename
		user_to_modify.email = email
		user_to_modify.qq = qq
		user_to_modify.save()
		return HttpResponseRedirect('/account/manage/user_list.html')
	else:
		if request.user == user_to_modify:
			user = user_to_modify
			groups = Group.objects.all()
			return render_to_response('user_form.html',{'user':user,'groups':groups},context_instance=RequestContext(request))
		else:
			#@permission_required('account.change_other_userprofile')
			if request.user.has_perm('account.change_other_userprofile'):
				user = user_to_modify
				groups = Group.objects.all()
				return render_to_response('user_form.html',{'user':user,'groups':groups},context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/404.html')

@login_required
@permission_required('account.add_userprofile',login_url='/403.html')
def user_add(request):
	errors= []
	if request.method == 'POST':
		username = request.POST['username']
		truename = request.POST['truename']
		email = request.POST['email']
		qq = request.POST['qq']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		print truename,email,qq,password1,password2
		if request.POST['is_active'] == 'true':
			is_active = True
		elif request.POST['is_active'] == 'false':
			is_active = False

		if username == '':
			errors.append('username failed')
		if password1 != password2:
			errors.append('different password!')
		if password1 == password2 and username != '':
			user=UserProfile.objects.create_user(username,email,password1)
			user.is_active=is_active
			user.qq = qq
			user.truename = truename
			user.save()
			return HttpResponseRedirect('/account/manage/user_list.html')

	disable = 'whatever what value it is, will not matters the template'
	return render_to_response(
		'user_add.html',
		{'disable':disable,'errors':errors},
		context_instance=RequestContext(request)
		)

@login_required
@permission_required('account.delete_userprofile',login_url='/403.html')
def user_remove(request,id):
	user_to_delete = UserProfile.objects.get(pk=id)
	user_to_delete.delete()
	return HttpResponseRedirect('/account/manage/user_list.html')

@login_required
def group_list(request):
	groups = Group.objects.all()
	#perms = groups[0].permission_set.all()
	return render_to_response('group_list.html',{'groups':groups},context_instance=RequestContext(request))#context_instance=RequestContext(request)

@login_required
#@permission_required('auth.change_group',login_url='/403.html')
def group_modify(request,id):
	if request.method == 'POST':
		group_id = request.POST.get('group_id')
		chosen_perms =  request.POST.getlist('perms',[])
		group_name = request.POST.get('groupname')
		print chosen_perms,group_name,group_id

		group_to_modify = Group.objects.get(pk=group_id)
		group_to_modify.name = group_name
		group_to_modify.permissions.clear()
		for chosen_perm_id in chosen_perms:
			permission_to_add = Permission.objects.get(pk=chosen_perm_id)
			print permission_to_add
		group_to_modify.permissions.add(permission_to_add)
		group_to_modify.save()
		return HttpResponseRedirect('/account/manage/group_list.html')

	else:
		group_to_modify = Group.objects.get(id=id)
		permissions = Permission.objects.all()
		return render_to_response('group_form.html',{'permissions':permissions,'group_to_modify':group_to_modify},context_instance=RequestContext(request))

@login_required
@permission_required('account.add_group',login_url='/403.html')
def group_add(request):
	if request.method == 'POST':
		groupname = request.POST['groupname']
		perms = request.POST.getlist('perms',[])
		group = Group(name=groupname)
		group.save()
		for perm in perms:
			perm_to_link = Permission.objects.get(codename=perm)
			group.permissions.add(perm_to_link)
		return HttpResponseRedirect('/account/manage/group_list.html')
	else:
		permissions = Permission.objects.all()
		return render_to_response('group_add.html',{'permissions':permissions},context_instance=RequestContext(request))

@login_required
@permission_required('account.delete_group',login_url='/403.html')
def group_remove(request,id):
	group_to_remove = Group.objects.get(pk=id)
	if group_to_remove.name == '':
		return HttpResponse(group_to_remove.name + 'cannot be removed')
	else:
		group_to_remove.delete()
	return HttpResponseRedirect('/account/manage/group_list.html')

@login_required
def permission_list(request):
	all_perms = Permission.objects.all()
	return render_to_response('perm_list.html',{'all_perms':all_perms},context_instance=RequestContext(request))

@login_required
@permission_required('permission.add_permission',login_url='/403.html')
def permission_add(request):
	if request.method == "POST":
		name = request.POST['name']
		contenttype = request.POST['contenttype']
		codename = request.POST['codename']
		print name,contenttype,codename
		permission_to_save = Permission(
			name=name,
			content_type_id=contenttype,
			codename=codename,
			)
		permission_to_save.save()
		return HttpResponseRedirect('/account/manage/permission_list.html')
	else:
		content_types = ContentType.objects.all()
		return render_to_response('perm_add.html',{'content_types':content_types},context_instance=RequestContext(request))

@login_required
def permission_modify(request,id):
	perm_to_modify = Permission.objects.get(pk=id)
	if request.method == "POST":
		name = request.POST['name']
		contenttype = request.POST['contenttype']
		codename = request.POST['codename']
		print name,contenttype,codename
		perm_to_modify.name = name
		perm_to_modify.content_type_id = content_type_id
		perm_to_modify.codename = codename
		perm_to_modify.save()
		return HttpResponseRedirect('/account/manage/permission_list.html')
	else:
		content_types = ContentType.objects.all()
		return render_to_response('perm_form.html',{'content_types':content_types,'perm_to_modify':perm_to_modify},context_instance=RequestContext(request))