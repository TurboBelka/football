# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('round_in_game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundingame',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2015, 11, 2, 11, 42, 17, 414912, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roundingame',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2015, 11, 2, 11, 42, 35, 85396, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
