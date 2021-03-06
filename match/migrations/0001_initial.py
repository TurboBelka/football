# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round_in_game', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_team_goals', models.SmallIntegerField()),
                ('second_team_goals', models.SmallIntegerField()),
                ('first_team', models.ForeignKey(related_name='first_team', to='teams.Team')),
                ('my_round', models.ForeignKey(to='round_in_game.RoundInGame')),
                ('second_team', models.ForeignKey(related_name='second_team', to='teams.Team')),
            ],
        ),
    ]
