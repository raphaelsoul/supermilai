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
			("read_sidebar_url", "Can See the sidebar of user management"),
			)