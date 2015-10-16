# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.SmallIntegerField(choices=[(1, b'finished'), (2, b'current'), (3, b'not_started')])),
                ('name', models.CharField(max_length=200)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('type_tour', models.SmallIntegerField(choices=[(1, b'1/8'), (2, b'1/4'), (3, b'1/2'), (4, b'final'), (5, b'third_place'), (6, b'regular')])),
            ],
        ),
    ]
