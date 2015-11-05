# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round_in_game', '0002_auto_20151102_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roundingame',
            name='type_rang',
            field=models.SmallIntegerField(choices=[(1, b'1/8'), (2, b'1/4'), (3, b'1/2'), (5, b'final'), (4, b'third_place'), (6, b'regular')]),
        ),
    ]
