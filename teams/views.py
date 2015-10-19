from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.views import generic
from tournament.models import Tournament
from teams.models import Team
from match.models import Match


class GetAllTourView(generic.ListView):
    template_name = 'teams/teams.html'
    context_object_name = 'tours'
    model = Tournament


def get_team_in_tour(request):
    if request.method == 'GET':
        tour_id = request.GET['my_select']

        first_teams_id = Match.objects.filter(
            round__tournament_id=tour_id).values_list('first_team_id',
                                                      flat=True)
        second_teams_id = Match.objects.filter(
            round__tournament_id=tour_id).values_list('second_team_id',
                                                      flat=True)
        teams_in_tour = Team.objects.filter(Q(id__in=first_teams_id) |
                                            Q(id__in=second_teams_id))
        teams_in_tour = serializers.serialize("json", teams_in_tour)

        return HttpResponse(teams_in_tour,
                            content_type='application/json')
    else:
        return HttpResponse(status='400')
