from django.db import models
from tournament.models import Tournament


# Create your models here.
class RoundInGame(models.Model):
    TYPE_RANG = (
        (1, '1/8'),
        (2, '1/4'),
        (3, '1/2'),
        (4, 'final'),
        (5, 'third_place'),
        (6, 'regular'),
    )
    tournament = models.ForeignKey(Tournament)
    type_rang = models.SmallIntegerField(choices=TYPE_RANG)
