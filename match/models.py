from django.db import models
from teams.models import Team
from round.models import Round


# Create your models here.
class Match(models.Model):
    first_team = models.ForeignKey(Team,
                                   related_name='%(class)s_requests_created')
    second_team = models.ForeignKey(Team)
    first_team_goals = models.SmallIntegerField()
    second_team_goals = models.SmallIntegerField()
    round = models.ForeignKey(Round)
