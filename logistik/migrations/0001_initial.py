# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PackingListNo', models.CharField(unique=True, max_length=30)),
                ('packinglist_time', models.DateField(null=True, blank=True)),
                ('depature_time', models.DateField(null=True, blank=True)),
                ('leaving_port_time', models.DateField(null=True, blank=True)),
                ('arrival_time', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'ordering': ['PackingListNo'],
                'db_table': 'Container',
                'permissions': (('view_container', 'Can view containers'), ('read_sidebar_url_logistik', 'Can see sidebar')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(unique=True, max_length=30)),
                ('hasTemp', models.BooleanField(default=False)),
                ('hasDescription', models.BooleanField(default=False)),
                ('container', models.ForeignKey(to='logistik.Container')),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sku'],
                'db_table': 'Item',
                'permissions': (('view_item', 'Can view items'),),
            },
            bases=(models.Model,),
        ),
    ]
