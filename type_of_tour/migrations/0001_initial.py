# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfTour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SmallIntegerField(choices=[(1, b'1/8'), (2, b'1/4'), (3, b'1/2'), (4, b'final'), (5, b'third_place'), (6, b'regular')])),
            ],
        ),
    ]
