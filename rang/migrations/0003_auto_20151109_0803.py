# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rang', '0002_rang_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rang',
            name='count',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
