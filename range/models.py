#!encoding=utf-8
from django.db import models
from tournament.models import Tournament
from users.models import Users


class Range(models.Model):
    user = models.ForeignKey(Users)
    tournament = models.ForeignKey(Tournament)
    rang = models.DecimalField(max_digits=2, decimal_places=2)
    count = models.SmallIntegerField()
    # процентное соотношение по отношению к оценке(из 4х игроков оценка 4=100%)
