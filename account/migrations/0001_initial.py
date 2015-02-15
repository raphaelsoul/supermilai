# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=75, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('truename', models.CharField(max_length=20, blank=True, null=True)),
                ('qq', models.CharField(max_length=20, blank=True, null=True)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', verbose_name='groups', to='auth.Group', blank=True, related_query_name='user')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', to='auth.Permission', blank=True, related_query_name='user')),
            ],
            options={
                'permissions': (('change_other_userprofile', 'Can Change others Profile'), ('stop_userprofile', 'Can userprofile'), ('read_first_menu_account', 'Can See the first menu of user management'), ('read_second_menu_user', 'Can See the second menu of user management'), ('read_second_menu_group', 'Can See the second menu of group'), ('read_second_menu_permission', 'Can See the second menu of permission')),
            },
            bases=(models.Model,),
        ),
    ]
