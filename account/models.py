from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class UserProfile(AbstractUser):
	truename = models.CharField(max_length=20,null=True,blank=True)
	qq = models.CharField(max_length=20,null=True,blank=True)

	#role = models.ManyToManyField(Role, verbose_name='roles',blank=True)

	class Meta:
		permissions = (
			#("view_task", "Can see available tasks"),
			("change_other_userprofile", "Can Change others Profile"),
			("stop_userprofile", "Can userprofile"),

			#permission on sidebar#
			("read_sidebar_account", "Can See the sidebar of user management"),

			("read_sidebar_logistik", "Can See the sidebar of logistik"),

			("read_sidebar_mission", "Can See the sidebar of mission"),

			("read_sidebar_listverify", "Can See the sidebar of listverify"),
			("read_chiildsidebar_handle", "Can See the sidebar of handle verify"),
			)