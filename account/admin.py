from django.contrib import admin
from account.models import UserProfile
from django.contrib.auth.models import Permission, Group

class UserProfileAdmin(admin.ModelAdmin):
	#,'qq','first_name','last_name','truename','email','groups'
	fieldsets = [
	(None,{'fields':['username']}),
	('Profile',{'fields':['last_name','first_name','truename']}),
	('Contact Information',{'fields':['email','qq']}),
	('Permission Type',{'fields':['is_superuser','is_staff','is_active','groups']}),
	#('My Permission Type',{'fields':['mygroups']}),
	#('Timestamp',{'fields':['date_joined','last_login']}),
	]
	list_display = (
		'username',
		'truename',
		'email',
		'is_superuser',
		'is_staff',
		'date_joined',
		'last_login',
		#'groups',
		)
admin.site.register(UserProfile,UserProfileAdmin)

class PermissionAdmin(admin.ModelAdmin):
	list_display = ('name','content_type','codename')
admin.site.register(Permission,PermissionAdmin)
