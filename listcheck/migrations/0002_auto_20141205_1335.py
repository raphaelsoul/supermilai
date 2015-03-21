# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listcheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['uploadtime'], 'permissions': (('view_plan', 'Can see detail of the plan'), ('pass_plan', 'Can mark the plan as passed and add notes'))},
        ),
    ]
