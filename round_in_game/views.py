import json
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.db.models.fields.files import ImageFieldFile
from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from match.models import Match
from round_in_game.models import RoundInGame
from teams.models import Team
from tournament.models import Tournament


class ChooseTourView(ListView):
    model = Tournament
    template_name = 'my_round/get_all_in_tour.html'
    context_object_name = 'tours'


def get_all_in_tour(request, pk):
    if request.method == 'GET':
        all_round = RoundInGame.objects.filter(tournament__id=pk)
        all_round = [{'id': r.id,
                      'type_rang': r.type_rang,
                      'type_name': r.get_type_rang_display()} for r in all_round]

        return HttpResponse(json.dumps(list(all_round)),
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


def serialize_image_field(obj):
    if isinstance(obj, ImageFieldFile):
        if obj:
            return obj.url
        else:
            return ""


def get_teams(request, pk):
    if request.method == 'GET':
        all_teams = Match.objects.filter(round_id=pk).values('first_team_id', 'second_team_id')
        teams_id = {i for item in all_teams for i in item.itervalues()}
        teams_in_round = Team.objects.filter(id__in=teams_id)
        teams = []
        for item in teams_in_round:
            teams.append(model_to_dict(item, fields=['name', 'logo', 'first_user_id',
                                                     'second_user_id']))
        return HttpResponse(json.dumps(teams, default=serialize_image_field),
                            content_type='application/json')
    else:
        return HttpResponse(status='400')
