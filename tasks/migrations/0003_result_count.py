# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20151117_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
