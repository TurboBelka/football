from django.db import models
from tournament.models import Tournament


class RoundInGame(models.Model):
    TYPE_RANG = (
        (1, '1/8'),
        (2, '1/4'),
        (3, '1/2'),
        (5, 'final'),
        (4, 'third_place'),
        (6, 'regular'),
    )

    tournament = models.ForeignKey(Tournament)
    type_rang = models.SmallIntegerField(choices=TYPE_RANG)
    date_start = models.DateField()
    date_end = models.DateField()
