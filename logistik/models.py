from account.models import UserProfile
from django.db import models

class Container(models.Model):
	#basic info
	PackingListNo = models.CharField(unique=True,max_length=30)

	#Timestamps
	packinglist_time = models.DateField(null=True,blank=True)
	depature_time = models.DateField(null=True,blank=True)
	leaving_port_time = models.DateField(null=True,blank=True)
	arrival_time = models.DateField(null=True,blank=True)

	status = models.CharField(max_length=10,null=True,blank=True)
	#Packing_items = models.ForeignKey(Item,through='Item')

	def __unicode__(self):
		return self.PackingListNo

	class Meta:
		ordering = ['PackingListNo']
		db_table = 'Container'
		permissions = (
			("view_container", "Can view containers"),
			)

	def get_status(self):
		if self.packinglist_time != None:
			if self.depature_time != None:
				status = 'shipping'
				if self.leaving_port_time != None:
					status = 'roading'
					if self.arrival_time != None:
						status = 'storing'
					else:
						status == 'roading'
				else:
					status = 'shipping'
			else:
				status = 'packing'
		else:
			status = 'error'
		return status

class Item(models.Model):
	sku = models.CharField(max_length=30,unique=True)
	hasTemp= models.BooleanField(default=False)
	hasDescription= models.BooleanField(default=False)
	manager = models.ForeignKey('account.UserProfile',null=True,blank=True)
	container = models.ForeignKey(Container)
	#temp_maker = models.CharField(max_length=30,null=True,blank=True)
	#description_maker = models.CharField(max_length=30,null=True,blank=True)

	def __unicode__(self):
		return self.sku

	class Meta:
		ordering = ['sku']
		db_table = 'Item'
		permissions = (
			("view_item", "Can view items"),
			)