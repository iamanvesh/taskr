# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_result_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 11, 17, 8, 40, 25, 440108, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
