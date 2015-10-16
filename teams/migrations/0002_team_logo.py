# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(default=datetime.datetime(2015, 10, 16, 12, 24, 49, 339817, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
