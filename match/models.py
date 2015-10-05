from django.db import models
from teams.models import Team
from round.models import Round


# Create your models here.
class Match(models.Model):
    id_first_team = models.ForeignKey(Team)
    id_second_team = models.ForeignKey(Team)
    first_team_goals = models.IntegerField()
    second_team_goals = models.IntegerField()
    id_round = models.ForeignKey(Round)
