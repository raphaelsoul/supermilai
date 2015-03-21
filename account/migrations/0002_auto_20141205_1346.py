# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('change_other_userprofile', 'Can Change others Profile'), ('stop_userprofile', 'Can userprofile'), ('read_sidebar_url', 'Can See the sidebar of user management'), ('read_sidebar_account', 'Can See the sidebar of user management'), ('read_sidebar_logistik', 'Can See the sidebar of logistik'), ('read_sidebar_mission', 'Can See the sidebar of mission'), ('read_sidebar_listverify', 'Can See the sidebar of listverify'), ('read_chiildsidebar_handle', 'Can See the sidebar of handle verify'))},
        ),
    ]
