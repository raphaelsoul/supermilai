from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required#,user_passes_test,
from models import UserProfile
from django.contrib.auth.models import Permission,Group
#from django.core.exceptions import PermissionDenied
#from decorators import custom_permission_required

@login_required
@permission_required('account.stop_userprofile')
def set_active_status(request):
	if request.method == 'POST':
		requested_db_id = request.POST.get('db_id')
		account_to_stop = UserProfile.objects.get(pk=requested_db_id)
		if account_to_stop.is_active == True:
			account_to_stop.is_active = False
			account_to_stop.is_staff = False
			account_to_stop.save()
			msg = 'set_false'
		else:
			account_to_stop.is_active = True
			account_to_stop.is_staff = True
			account_to_stop.save()
			msg = 'set_true'
		return HttpResponse(msg)
	else:
		return HttpResponseRedirect('/404.html')

@login_required
@permission_required('account.change_other_userprofile')
def set_group(request):
	if request.method == 'POST':
		group_id = request.POST.get('group_id')
		user_id = request.POST.get('user_id')
		user = UserProfile.objects.get(pk=user_id)
		group = Group.objects.get(pk=group_id)
		current_groups = user.groups.all()
		#clear the old relationship#
		for g in current_groups:
			user.groups.remove(g)
		#build new relationship#
		user.groups.add(group)
		user.save()
		return HttpResponse('done')
	else:
		return HttpResponseRedirect('/404.html')