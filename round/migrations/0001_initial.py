# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
        ('type_of_tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tournament', models.ForeignKey(to='tournament.Tournament')),
                ('type_of_tour', models.ForeignKey(to='type_of_tour.TypeOfTour')),
            ],
        ),
    ]
