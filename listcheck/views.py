from models import ListPlan,Plan
#from django.contrib.auth.models import User
from account.models import UserProfile
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.template import RequestContext

@login_required
def overview(request,page_num): #handle
	plans = Plan.objects.all()
	paginator = Paginator(plans, 8)
	try:
		plans = paginator.page(page_num)
	except PageNotAnInteger:
		plans = paginator.page(1)
	except EmptyPage:
		plans = paginator.page(paginator.num_pages)
	return render_to_response('handle_plan.html',{'plans':plans},context_instance=RequestContext(request))

@login_required
@permission_required('listcheck.add_plan',login_url='/403.html')
def add_plan(request):
	if request.method == 'POST':
		#user = User.objects.get(username=request.user)
		poster = request.user.get_full_name()
		poster_id = request.user.id
		list_skus = request.POST.getlist('sku',[])
		meta_keywords = request.POST.getlist('keywords',[])
		former_prices = request.POST.getlist('former_price',[])
		planed_prices = request.POST.getlist('planed_price',[])
		bs_lists1 = request.POST.getlist('bs_url1',[])
		bs_prices1 = request.POST.getlist('bs_price1',[])
		bs_lists2 = request.POST.getlist('bs_url2',[])
		bs_prices2 = request.POST.getlist('bs_price2',[])
		bs_lists3 = request.POST.getlist('bs_url3',[])
		bs_prices3 = request.POST.getlist('bs_price3',[])
		planed_account = request.POST['planed_account']
		#print list_skus

		Plan.objects.create(poster = poster,poster_id = poster_id,planed_account = planed_account)
		plan_created = Plan.objects.filter(poster = poster,poster_id = poster_id).order_by('-id')[0]
		for i in range(len(list_skus)):
			content = ListPlan(
				list_sku = list_skus[i],
				meta_keyword = meta_keywords[i],
				former_price = former_prices[i],
				planed_price = planed_prices[i],
				best_seller_list1 = bs_lists1[i],
				best_seller_list2 = bs_lists2[i],
				best_seller_list3 = bs_lists3[i],
				seller_price1 = bs_prices1[i],
				seller_price2 = bs_prices2[i],
				seller_price3 = bs_prices3[i],
				)
			content.plan = plan_created
			content.save()
		redirecturls = '/listcheck/mylistplan/page=1'
		report = 'done!'
		return render_to_response('jumping.html',{'report':report})
	else:
		return render_to_response('add_plan.html',context_instance=RequestContext(request))

@login_required
@permission_required('listcheck.change_plan',login_url='/403.html')
def modify_plan(request,id):
	db_id = id
	if request.method == 'POST':
		poster = request.user.get_full_name()
		poster_id = request.user.id
		list_skus = request.POST.getlist('sku',[])
		meta_keywords = request.POST.getlist('keywords',[])
		former_prices = request.POST.getlist('former_price',[])
		planed_prices = request.POST.getlist('planed_price',[])
		bs_lists1 = request.POST.getlist('bs_url1',[])
		bs_prices1 = request.POST.getlist('bs_price1',[])
		bs_lists2 = request.POST.getlist('bs_url2',[])
		bs_prices2 = request.POST.getlist('bs_price2',[])
		bs_lists3 = request.POST.getlist('bs_url3',[])
		bs_prices3 = request.POST.getlist('bs_price3',[])
		planed_account = request.POST['planed_account']

		plan_to_modify = Plan.objects.get(id=db_id)
		plan_to_modify.planed_account = planed_account
		plan_to_modify.save()
		plan_to_modify = Plan.objects.get(id=db_id)
		relations = plan_to_modify.listplan_set.all()
		for ralation in relations:
			ralation.delete()
		for i in range(len(list_skus)):
			content = ListPlan(
				list_sku = list_skus[i],
				meta_keyword = meta_keywords[i],
				former_price = former_prices[i],
				planed_price = planed_prices[i],
				best_seller_list1 = bs_lists1[i],
				best_seller_list2 = bs_lists2[i],
				best_seller_list3 = bs_lists3[i],
				seller_price1 = bs_prices1[i],
				seller_price2 = bs_prices2[i],
				seller_price3 = bs_prices3[i],
				)
			content.plan = plan_to_modify
			content.save()
		redirecturls = '/listcheck/mylistplan/page=1'
		report = 'done!'
		return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})
	else:
		plan = Plan.objects.get(id=db_id)
		return render_to_response('modify_plan.html',{'plan':plan})

@login_required
@permission_required('listcheck.view_plan',login_url='/403.html')
def detail_plan(request,id):
	db_id = id
	plan = Plan.objects.get(id=db_id)
	return render_to_response('detail_plan.html',{'plan':plan},context_instance=RequestContext(request))

@login_required
def my_listplan(request,page_num):
	user = UserProfile.objects.get(username=request.user)
	print type(user)
	plans = Plan.objects.filter(poster_id=user.id)
	paginator = Paginator(plans, 8)
	try:
		plans = paginator.page(page_num)
	except PageNotAnInteger:
		plans = paginator.page(1)
	except EmptyPage:
		plans = paginator.page(paginator.num_pages)
	return render_to_response('my_listplan.html',{'plans':plans},context_instance=RequestContext(request))

@login_required
@permission_required('listcheck.delete_plan',login_url='/403.html')
def delete_plan(request,id):
	db_id = id
	try:
		plan_to_delete = Plan.objects.get(id=db_id)
		plan_to_delete.delete()
	except Plan.DoesNotExist:
		pass
	finally:
		redirecturls = '/listcheck/mylistplan/page=1'
		report = 'done!'
		return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})

@login_required
@permission_required('listcheck.pass_plan',login_url='/403.html')
def mark_passed(request): #ajax
	if request.method == 'POST':
		plan_id = request.POST['listplan_id']
		plan = Plan.objects.get(id=plan_id)
		plan.check_result = 'true'
		plan.save()
		return HttpResponse('done')

@login_required
@permission_required('listcheck.pass_plan',login_url='/403.html')
def add_note(request,id): #fake_ajax
	if request.method == 'POST':
		db_id = id
		note = request.POST['note']
		plan_to_note = Plan.objects.get(id=db_id)
		plan_to_note.note = note
		plan_to_note.save()
		redirecturls = '/listcheck/handle/page=1'
		report = 'done!'
		return render_to_response('jumping.html',{'redirecturls':redirecturls,'report':report})