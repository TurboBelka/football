from django.db import models
from teams.models import Team
from round_in_game.models import RoundInGame


class Match(models.Model):
    first_team = models.ForeignKey(Team,
                                   related_name='first_team')
    second_team = models.ForeignKey(Team,
                                    related_name='second_team')
    first_team_goals = models.SmallIntegerField(blank=True, null=True)
    second_team_goals = models.SmallIntegerField(blank=True, null=True)
    my_round = models.ForeignKey(RoundInGame)
