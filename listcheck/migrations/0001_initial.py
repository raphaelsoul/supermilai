# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_sku', models.CharField(max_length=30)),
                ('meta_keyword', models.CharField(max_length=50)),
                ('former_price', models.CharField(max_length=10)),
                ('planed_price', models.CharField(max_length=10)),
                ('best_seller_list1', models.URLField(null=True, blank=True)),
                ('best_seller_list2', models.URLField(null=True, blank=True)),
                ('best_seller_list3', models.URLField(null=True, blank=True)),
                ('seller_price1', models.CharField(max_length=10, null=True, blank=True)),
                ('seller_price2', models.CharField(max_length=10, null=True, blank=True)),
                ('seller_price3', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poster', models.CharField(max_length=20, null=True, blank=True)),
                ('poster_id', models.CharField(max_length=20, null=True, blank=True)),
                ('uploadtime', models.DateTimeField(auto_now_add=True)),
                ('planed_account', models.CharField(max_length=20)),
                ('note', models.TextField(null=True, blank=True)),
                ('check_result', models.CharField(default=b'false', max_length=10, null=True, blank=True)),
            ],
            options={
                'ordering': ['uploadtime'],
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='listplan',
            name='plan',
            field=models.ForeignKey(to='listcheck.Plan'),
            preserve_default=True,
        ),
    ]
