# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rang', models.DecimalField(default=25, max_digits=5, decimal_places=2)),
                ('tournament', models.ForeignKey(to='tournament.Tournament', blank=True)),
                ('user', models.ForeignKey(to='users.Users')),
            ],
        ),
    ]
