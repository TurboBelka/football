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
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to=b'static/teams_logo', blank=True)),
                ('first_user', models.ForeignKey(related_name='first_user', to='users.Users')),
                ('second_user', models.ForeignKey(related_name='second_user', to='users.Users')),
                ('tour', models.ManyToManyField(to='tournament.Tournament')),
            ],
        ),
    ]
