# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_app', '0003_auto_20160313_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
