from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def make_temps(request):
	if request.method == 'POST':
		template_code = request.POST['template_code']
		#password = request.POST['password']  #'password' is forbidden
		password = 'hooya5000'
		if password != 'hooya5000':
			return HttpResponse('Wrong Password! Invalid Request!')
		else:
			if template_code == 'de-fdv':
				try:
					item_title = request.POST['item_title']
					sku = request.POST['sku']
					description_top = request.POST['description_top']

					features = request.POST.getlist('feature',[])
					model_no = request.POST['model_no']
					color = request.POST['color']

					specifications = request.POST.getlist('spec',[])
				finally:
					return render_to_response('temp_de.html',{
						'item_title':item_title,
						'sku':sku,
						'description_top':description_top,
						'features':features,
						'model_no':model_no,
						'color':color,
						'specifications':specifications,
						},context_instance=RequestContext(request))
			elif template_code == 'uk-sc':
				try:
					item_title = request.POST['item_title']
					sku = request.POST['sku']
					description_top = request.POST['description_top']

					features = request.POST.getlist('feature',[])
					model_no = request.POST['model_no']
					color = request.POST['color']

					specifications = request.POST.getlist('spec',[])

					img_first = request.POST['img_first']
					imgs = request.POST.getlist('img',[])
				finally:
					return render_to_response('savechannel_new.html',{
						'item_title':item_title,
						'sku':sku,
						'description_top':description_top,
						'features':features,
						'model_no':model_no,
						'color':color,
						'specifications':specifications,
						'img_first':img_first,
						'imgs':imgs,
						},context_instance=RequestContext(request))
			elif template_code == 'uk-ag':
				try:
					item_title = request.POST['item_title']
					sku = request.POST['sku']
					description_top = request.POST['description_top']

					features = request.POST.getlist('feature',[])
					model_no = request.POST['model_no']
					color = request.POST['color']

					specifications = request.POST.getlist('spec',[])

					img_first = request.POST['img_first']
					imgs = request.POST.getlist('img',[])
				finally:
					return render_to_response('UK-AG.html',{
						'item_title':item_title,
						'sku':sku,
						'description_top':description_top,
						'features':features,
						'model_no':model_no,
						'color':color,
						'specifications':specifications,
						'img_first':img_first,
						'imgs':imgs,
						},context_instance=RequestContext(request))
	else:
		return render_to_response('info-form.html',context_instance=RequestContext(request))