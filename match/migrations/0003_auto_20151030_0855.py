# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_auto_20151030_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='first_team_goals',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='second_team_goals',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
