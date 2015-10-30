# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='first_team_goals',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team_goals',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
