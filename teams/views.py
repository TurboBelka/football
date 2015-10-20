import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q, Max
from django.db.models.fields.files import ImageFieldFile
from django.forms import model_to_dict, modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from rang.models import Rang
from teams.forms import CreateTeamForm
from tournament.models import Tournament
from teams.models import Team
from match.models import Match
from users.models import Users


class GetAllTourView(generic.ListView):
    template_name = 'teams/teams.html'
    context_object_name = 'tours'
    model = Tournament


def serialize_image_field(obj):
    if isinstance(obj, ImageFieldFile):
        return obj.url


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
        teams = []
        for team in teams_in_tour:
            if team.logo == "":
                team.logo = "static/teams_logo/your-logo-here.png"

            teams.append(model_to_dict(team,
                                       fields=['model', 'pk', 'logo',
                                               'name']))
        teams = json.dumps(teams, default=serialize_image_field)
        return HttpResponse(teams,
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


@user_passes_test(lambda u: u.is_superuser)
def create_team(request):
    form_set_cls = modelformset_factory(Team, form=CreateTeamForm, extra=2,
                                        max_num=2)
    if request.POST:
        if request.user.is_superuser:
            form_set = form_set_cls(request.POST, request.FILES)
            if form_set.is_valid():
                form_set.save()
                return HttpResponseRedirect(reverse_lazy('teams:teams'))
            else:
                return render(request, 'teams/create_team.html', context={
                    'form_set': form_set})
    else:
        form_set = form_set_cls(queryset=Team.objects.none())
        return render(request, 'teams/create_team.html', context={
            'form_set': form_set})


def generate_teams(request):
    # all_users = Users.objects.values_list('id', 'username')
    all_users = Rang.objects.value('user_id').annotate(Max('id'))

    return render(request, 'teams/generate_teams.html', context={
        'all_user': all_users})
