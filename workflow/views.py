from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from django.template import RequestContext
from logistik.models import Item
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from account.models import UserProfile

@login_required
@permission_required('listcheck.view_plan',login_url='/403.html')
def all_tasks(request,page_num):
	items_to_tasks = Item.objects.filter(manager=None)
	paginator = Paginator(items_to_tasks, 20)
	try:
		items_to_tasks = paginator.page(page_num)
	except PageNotAnInteger:
		items_to_tasks = paginator.page(1)
	except EmptyPage:
		items_to_tasks = paginator.page(paginator.num_pages)
	return render_to_response('all_tasks.html',{'items_to_tasks':items_to_tasks},context_instance=RequestContext(request))

@login_required
#@permission_required('listcheck.pass_plan',login_url='/403.html')
def handle_tasks_asign(request):
	if request.method == 'POST':
		chosen_tasks = request.POST.getlist('task',[])
		user = request.user
		for item_id in chosen_tasks:
			chosen_item = Item.objects.get(pk=item_id)
			chosen_item.manager = user
			chosen_item.save()
		return HttpResponseRedirect('/workflow/my_tasks.html')
		#return HttpResponse('done')
	else:
		return HttpResponseRedirect('/404.html')

@login_required
@permission_required('listcheck.view_plan',login_url='/403.html')
def my_tasks(request):
	user_id = request.user.id
	user = UserProfile.objects.get(pk=user_id)
	my_tasks = user.item_set.all()
	return render_to_response('my_tasks.html',{'items':my_tasks},context_instance=RequestContext(request))