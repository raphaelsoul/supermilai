# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistik', '0002_auto_20141204_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='container',
            options={'ordering': ['PackingListNo'], 'permissions': (('view_container', 'Can view containers'),)},
        ),
    ]
