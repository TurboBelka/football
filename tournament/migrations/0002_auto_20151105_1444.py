# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='mode',
            field=models.SmallIntegerField(choices=[(1, b'finished'), (2, b'current'), (3, b'not_started'), (4, b'voted')]),
        ),
    ]
