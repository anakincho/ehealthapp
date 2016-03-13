# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_app', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shared',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='shared',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
