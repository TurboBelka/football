#!encoding=utf-8
from django.db import models
from tournament.models import Tournament
from users.models import Users


class Rang(models.Model):
    user = models.ForeignKey(Users)
    tournament = models.ForeignKey(Tournament, null=True)
    count = models.IntegerField(blank=True, null=True)
    rang = models.DecimalField(max_digits=5, decimal_places=2, default=25)
