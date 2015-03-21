from django.db import models

class Plan(models.Model):
	poster = models.CharField(max_length=20,null=True,blank=True)
	poster_id = models.CharField(max_length=20,null=True,blank=True)
	uploadtime = models.DateTimeField(auto_now_add=True)
	planed_account = models.CharField(max_length=20)

	note = models.TextField(null=True,blank=True)
	check_result = models.CharField(max_length=10,null=True,blank=True,default='false')

	class Meta:
		ordering = ['uploadtime']
		#db_table = 'Plan' #raises error, unknown reason
		permissions = (
			#("view_task", "Can see available tasks"),
			("view_plan", "Can see detail of the plan"),
			("pass_plan", "Can mark the plan as passed and add notes"),
			)



class ListPlan(models.Model): ##here ist content of clas Plan
	list_sku = models.CharField(max_length=30)
	meta_keyword = models.CharField(max_length=50)
	former_price = models.CharField(max_length=10)
	planed_price = models.CharField(max_length=10)
	best_seller_list1 = models.URLField(null=True,blank=True)
	best_seller_list2 = models.URLField(null=True,blank=True)
	best_seller_list3 = models.URLField(null=True,blank=True)
	seller_price1 = models.CharField(max_length=10,null=True,blank=True)
	seller_price2 = models.CharField(max_length=10,null=True,blank=True)
	seller_price3 = models.CharField(max_length=10,null=True,blank=True)

	plan = models.ForeignKey(Plan)

	class Meta:
		#db_table = 'ListPlanDetail'
		permissions = (
			#("view_task", "Can see available tasks"),
			)


