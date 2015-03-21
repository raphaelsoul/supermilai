import json
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required

@login_required
@permission_required('listcheck.change_listplan',login_url='/403.html')
def temp_mark(request):
	if request.method == 'POST':
		requested_sku = request.POST['sku_id']
		requested_action = request.POST['action']
		try:
			if requested_action == 'mark_as_done':
				requested_item = Item.objects.get(id=requested_sku)
				requested_item.hasTemp = True
				requested_item.save()
				current_status = 'done'
			elif requested_action == 'mark_as_undone':
				requested_item = Item.objects.get(id=requested_sku)
				requested_item.hasTemp = False
				requested_item.save()
				current_status = 'undone'
			else:
				return HttpResponseRedirect('/')
		except Item.DoesNotExist:
			return HttpResponse('500')
		finally:
			return HttpResponse(current_status)
	else:
		return HttpResponseRedirect('/404.html')

@login_required
@permission_required('listcheck.change_listplan',login_url='/403.html')
def description_mark(request):
	if request.method == 'POST':
		requested_sku = request.POST['sku_id']
		requested_action = request.POST['action']
		try:
			if requested_action == 'des_mark_as_done':
				requested_item = Item.objects.get(id=requested_sku)
				requested_item.hasDescription = True
				requested_item.save()
				current_status = 'done'
			elif requested_action == 'des_mark_as_undone':
				requested_item = Item.objects.get(id=requested_sku)
				requested_item.hasDescription = False
				requested_item.save()
				current_status = 'undone'
			else:
				return HttpResponseRedirect('/')
		except Item.DoesNotExist:
			current_status = '500'
		finally:
			return HttpResponse(current_status)
	else:
		return HttpResponseRedirect('/404.html')

@login_required
@permission_required('listcheck.change_listplan',login_url='/403.html')
def lot_size_mark(request):
	if request.method == 'POST':
		#print request.POST
		action = request.POST.get('action')
		sku_ids = request.POST.getlist('sku_ids[]',[])
		#print sku_ids
		print action#marktemp
		if action == 'marktemp':
			for sku_id in sku_ids:
				sku_to_mark = Item.objects.get(pk=sku_id)
				sku_to_mark.hasTemp = True
				sku_to_mark.save()
			return HttpResponse('done')
		if action == 'markdes':
			for sku_id in sku_ids:
				sku_to_mark = Item.objects.get(pk=sku_id)
				sku_to_mark.hasDescription = True
				sku_to_mark.save()
			return HttpResponse('done')