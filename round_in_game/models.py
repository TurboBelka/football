from django.db import models
from tournament.models import Tournament


# Create your models here.
class RoundInGame(models.Model):
    tournament = models.ForeignKey(Tournament)
