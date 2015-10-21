# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
        ('teams', '0003_auto_20151019_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tour',
            field=models.ManyToManyField(to='tournament.Tournament'),
        ),
    ]
