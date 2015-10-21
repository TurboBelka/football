import json
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q, Max
from django.db.models.fields.files import ImageFieldFile
from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from rang.models import Rang
from teams.forms import CreateTeamForm
from tournament.models import Tournament
from teams.models import Team
from django.contrib.auth.models import User


class GetAllTourView(generic.ListView):
    template_name = 'teams/teams.html'
    context_object_name = 'tours'
    model = Tournament


def serialize_image_field(obj):
    if isinstance(obj, ImageFieldFile):
        if obj:
            return obj.url
        else:
            return ""


def get_team_in_tour(request, pk):
    if request.method == 'GET':
        teams_in_tour = Team.objects.filter(tour__id=pk).values('id', 'logo',
                                                                'name')

        teams = json.dumps(list(teams_in_tour), default=serialize_image_field)
        return HttpResponse(teams,
                            content_type='application/json')
    else:
        return HttpResponse(status='400')


@user_passes_test(lambda u: u.is_superuser)
def create_team(request, pk):
    form_set_cls = modelformset_factory(Team, form=CreateTeamForm, extra=2,
                                        max_num=2)
    t = Tournament.objects.get(pk=pk)
    if request.POST:
        if request.user.is_superuser:
            form_set = form_set_cls(request.POST, request.FILES)
            if form_set.is_valid():
                new_teams = form_set.save(commit=False)
                for team in new_teams:
                    if not Team.objects.filter(Q(first_user=team.first_user,
                                                 second_user=team.second_user) |
                                                Q(first_user=team.second_user,
                                                  second_user=team.first_user)).exists():
                        fu_name = User.objects.get(users=team.first_user)
                        su_name = User.objects.get(users=team.second_user)

                        gen_name = '%s %s. + %s %s.' % (fu_name.first_name,
                                                        fu_name.last_name[:1],
                                                        su_name.first_name,
                                                        su_name.last_name[:1])

                        team.name = gen_name
                        team.save()

                        t.team_set.add(team)
                        t.save()
                return HttpResponseRedirect(reverse_lazy('teams:teams'))
            else:
                return render(request, 'teams/create_team.html', context={
                    'form_set': form_set})
    else:
        form_set = form_set_cls(queryset=Team.objects.none())
        return render(request, 'teams/create_team.html', context={
            'form_set': form_set})


def generate_teams(request, pk):
    last_rang = Rang.objects.values('user').annotate(Max('id'))
    arr = []
    for item in last_rang:
        arr.append(item['id__max'])
    users_last_rang = Rang.objects.filter(id__in=arr)
    users_info = []
    for item in users_last_rang:
        user = {
            'user_id': item.user.id,
            'first_name': item.user.user.first_name,
            'last_name': item.user.user.last_name,
            'rang': item.rang
        }
        users_info.append(user)
    print users_info
    return render(request, 'teams/generate_teams.html', context={
        'all_user': users_info})
