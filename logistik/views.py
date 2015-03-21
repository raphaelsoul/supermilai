from models import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, Permission,Group
from django.template import RequestContext

def clean_date(date):
	if date == '' or date == None:
		return None
	else:
		return date

@login_required
@permission_required('logistik.view_container',login_url='/403.html')
def overview(request):
	containers = Container.objects.all()[0:10]
	skus = Item.objects.all()[0:10]
	containers_num = Container.objects.all().count()
	skus_num = Item.objects.all().count()
	skus_num_without_template = Item.objects.filter(hasTemp=False).count()
	skus_num_with_template = Item.objects.filter(hasTemp=True).count()
	skus_num_without_description = Item.objects.filter(hasDescription=False).count()
	skus_num_with_description = Item.objects.filter(hasDescription=True).count()
	return render_to_response('overview.html',{
		'containers':containers,
		'skus':skus,
		'containers_num':containers_num,
		'skus_num':skus_num,
		'skus_num_without_template':skus_num_without_template,
		'skus_num_with_template':skus_num_with_template,
		'skus_num_without_description':skus_num_without_description,
		'skus_num_with_description':skus_num_with_description,
		},context_instance=RequestContext(request))

@login_required
@permission_required('logistik.add_container',login_url='/403.html')
def add_container(request):
	if request.method == 'POST':
		skus = request.POST.getlist('sku',[])
		packing_list_no = request.POST['packing_list_no']
		datetime1 = request.POST['datetime1']
		datetime2 = clean_date(request.POST['datetime2'])
		datetime3 = clean_date(request.POST['datetime3'])
		datetime4 = clean_date(request.POST['datetime4'])
		if request.POST['packing_list_no'] == '':
			return HttpResponse('PackingListNo is required!')
		elif request.POST['datetime1'] =='':
			return HttpResponse('PackingList Date is required!')
		else:
			container = Container(
				PackingListNo = packing_list_no,
				packinglist_time = datetime1,
				depature_time = datetime2,
				leaving_port_time = datetime3,
				arrival_time = datetime4,
				)
			status = container.get_status()
			print status
			container = Container(
				PackingListNo = packing_list_no,
				packinglist_time = datetime1,
				depature_time = datetime2,
				leaving_port_time = datetime3,
				arrival_time = datetime4,
				status = status,
				)

			try:
				container.save()
			except:
				redirecting_id = Container.objects.get(PackingListNo=packing_list_no).id
				redirecturls = '/logistik/container/modify/id=' + str(redirecting_id)
				report = 'Exist! Redirecting to modify it!'
				return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})
			saved_container = Container.objects.get(PackingListNo=packing_list_no)
			try:
				for sku in skus:
					item = Item(sku = sku,hasTemp = False,container = saved_container)
					item.save()
			except:
				pass
			redirecturls = '/'
			report = 'Done! back to dashboard!'
			return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})
	else:
		return render_to_response('add_container.html',context_instance=RequestContext(request))

@login_required
@permission_required('logistik.change_container',login_url='/403.html')
def modify_container(request,id):
	db_id = id
	if request.method == 'POST':
		skus = request.POST.getlist('sku',[])
		sku_ids = request.POST.getlist('sku_id',[])
		print sku_ids
		hasTemps = request.POST.getlist('hasTemp',[])
		print hasTemps
		packing_list_no = request.POST['packing_list_no']
		datetime1 = request.POST['datetime1']
		datetime2 = clean_date(request.POST['datetime2'])
		datetime3 = clean_date(request.POST['datetime3'])
		datetime4 = clean_date(request.POST['datetime4'])
		print 'get data ok!'
		if request.POST['packing_list_no'] == '':
			return HttpResponse('PackingListNo is required!')
		elif request.POST['datetime1'] =='':
			return HttpResponse('PackingList Date is required!')
		else:
			container_to_modify = Container(
				PackingListNo = packing_list_no,
				packinglist_time = datetime1,
				depature_time = datetime2,
				leaving_port_time = datetime3,
				arrival_time = datetime4,
				)
			status = container_to_modify.get_status()
			print 'status check ok!'
			container_to_modify = Container(
				PackingListNo = packing_list_no,
				packinglist_time = datetime1,
				depature_time = datetime2,
				leaving_port_time = datetime3,
				arrival_time = datetime4,
				status = status,
				)

			Container.objects.filter(id=db_id).update(
				packinglist_time = datetime1,
				depature_time = datetime2,
				leaving_port_time = datetime3,
				arrival_time = datetime4,
				status = status,
				)
			container_to_modify = Container.objects.get(id=db_id)
			#old_skus = Item.objects.filter(container=container_to_modify)
			#old_skus.delete()
			hasTemps_list = []
			t = True
			f = False
			for p in hasTemps:
				if p == '1':
					hasTemps_list.append(t)
				else:
					hasTemps_list.append(f)
			for i in range(len(skus)):
				try:
					item = Item(id=sku_ids[i],sku = skus[i],container = container_to_modify)
					item.save()
				except IndexError:
					if not Item.objects.filter(sku = skus[i]):
						item = Item(sku = skus[i],container = container_to_modify)
						item.save()
					else:
						pass
			redirecturls = '/'
			report = 'Success!'
			return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})
	else:
		container_to_modify = Container.objects.get(id=db_id)
		skus = Item.objects.filter(container_id=db_id)
		return render_to_response('modify_container.html',{'container_to_modify':container_to_modify,'skus':skus})

@login_required
@permission_required('logistik.view_container',login_url='/403.html')
def detail_container(request,id):
	db_id = id
	container_to_view = Container.objects.get(id=db_id)
	skus = Item.objects.filter(container_id=db_id)
	return render_to_response('detail_container.html',{'container_to_view':container_to_view,'skus':skus},context_instance=RequestContext(request))

@login_required
@permission_required('logistik.view_container',login_url='/403.html')
def search(request):
	search_type = request.POST['target-type']
	keywords = request.POST['keywords']
	if keywords == '':
		results = ['you typed in nothing as keywords!']
		result_type = 'empty'
	else:
		if search_type == 'container':
			results = Container.objects.filter(PackingListNo__icontains=keywords)
			result_type = 'container'
		elif search_type == 'sku':
			results = Item.objects.filter(sku__icontains=keywords)
			result_type = 'item'
		else:
			pass
	return render_to_response('search_result.html',{'results':results,'result_type':result_type},context_instance=RequestContext(request))

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

@login_required
@permission_required('logistik.view_container',login_url='/403.html')
def all_containers(request,page_num):
	containers = Container.objects.all()
	paginator = Paginator(containers, 20)
	try:
		containers = paginator.page(page_num)
	except PageNotAnInteger:
		containers = paginator.page(1)
	except EmptyPage:
		containers = paginator.page(paginator.num_pages)
	return render_to_response('all_containers.html',{'containers':containers},context_instance=RequestContext(request))

@login_required
@permission_required('logistik.view_item',login_url='/403.html')
def all_items(request,page_num):
	items = Item.objects.all()
	paginator = Paginator(items, 20)
	try:
		items = paginator.page(page_num)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	return render_to_response('all_items.html',{'items':items},context_instance=RequestContext(request))