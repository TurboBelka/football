import json
import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse_lazy
from django.db.models.fields.files import ImageFieldFile
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from match.models import Match
from round_in_game.models import RoundInGame
from teams.models import Team
from tournament.models import Tournament
from django.core.serializers.json import DjangoJSONEncoder


class ChooseTourView(ListView):
    model = Tournament
    template_name = 'my_round/get_all_in_tour.html'
    context_object_name = 'tours'


def get_all_in_tour(request, pk):
    if request.method == 'GET':
        all_round = RoundInGame.objects.filter(tournament__id=pk).order_by('date_start')
        all_round = [{'id': r.id,
                      'type_rang': r.type_rang,
                      'type_name': r.get_type_rang_display(),
                      'date_start': r.date_start,
                      'date_end': r.date_end} for r in
                     all_round]

        return HttpResponse(json.dumps(all_round, cls=DjangoJSONEncoder),
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
        all_teams = Match.objects.filter(my_round_id=pk).values('first_team_id',
                                                             'second_team_id')
        teams_id = {i for item in all_teams for i in item.itervalues()}
        teams_in_round = Team.objects.filter(id__in=teams_id)
        teams = []
        for item in teams_in_round:
            teams.append(model_to_dict(item, fields=['id', 'name', 'logo']))
        return HttpResponse(json.dumps(teams, default=serialize_image_field),
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


def add_teams(request, pk):
    if request.method == 'GET':
        all_teams = Match.objects.filter(my_round_id=pk).values('first_team_id',
                                                             'second_team_id')
        teams_id = {i for item in all_teams for i in item.itervalues()}
        teams_in_round = Team.objects.exclude(id__in=teams_id)
        teams = []
        for item in teams_in_round:
            teams.append(model_to_dict(item, fields=['id', 'name', 'logo',
                                                     'first_user_id',
                                                     'second_user_id']))
        return HttpResponse(json.dumps(teams, default=serialize_image_field),
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


def gen_matchs(request, pk):
    if request.method == 'POST':
        my_round = get_object_or_404(RoundInGame, pk=pk)
        teams_id = json.loads(request.POST['teams_id'])
        count_teams = len(teams_id)
        if my_round.type_rang != 6:
            for i in xrange(count_teams-1):
                new_match = Match.objects.create(first_team_id=teams_id[i],
                                                 second_team_id=teams_id[count_teams-i-1],
                                                 my_round=my_round)
        else:
            count_match = int(request.POST['count_match'])
            for i in xrange(count_match):
                for j in xrange(count_teams-1):
                    new_match = Match.objects.create(
                        first_team_id=teams_id[j],
                        second_team_id=teams_id[j + 1],
                        my_round=my_round)
                    j += 1
                i += 1
                teams_id.reverse()
        return HttpResponse(reverse_lazy('round:choose_tour'))
    else:
        return HttpResponse(status='400')


def choose_type(request, pk):
    if request.method == 'GET':
        exists_type = RoundInGame.objects.filter(tournament__id=pk).exclude(type_rang=6).values_list(
                                                'type_rang', flat=True)
        types_round = dict(RoundInGame.TYPE_RANG)
        for item in exists_type:
            if item in types_round.iterkeys():
                types_round.pop(item)

        return HttpResponse(json.dumps(types_round.values()),
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


@staff_member_required
def create(request):
    if request.method == 'POST':
        tour = Tournament.objects.get(id=request.POST['tour_id'])
        RoundInGame.objects.get_or_create(
            type_rang=request.POST['type_id'],
            tournament=tour,
            date_start=request.POST['date_start'],
            date_end=request.POST['date_end'])
        return HttpResponse(reverse_lazy('round:choose_tour'))
    else:
        return HttpResponse(status='400')
