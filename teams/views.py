import json
import random
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
from users.models import Users


class GetAllTourView(generic.ListView):
    template_name = 'teams/teams.html'
    context_object_name = 'tours'
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super(GetAllTourView, self).get_context_data(**kwargs)
        context['tour_id'] = self.request.GET.get('pk', default="")
        return context


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
    if t.mode != 1:
        if request.POST:
            if request.user.is_superuser:
                form_set = form_set_cls(request.POST, request.FILES)
                if form_set.is_valid():
                    new_teams = form_set.save(commit=False)
                    for team in new_teams:
                        l = check_team_exist(team.first_user, team.second_user)
                        if l[0]:
                            team.name = l[1]
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
    return render(request, 'teams/generate_teams.html', context={
        'all_users': users_info,
        'tour_id': pk})


def check_team_exist(first_user, second_user):
    fu_name = User.objects.get(users=first_user)
    su_name = User.objects.get(users=second_user)
    gen_name = '%s %s. + %s %s.' % (fu_name.first_name,
                                    fu_name.last_name[:1],
                                    su_name.first_name,
                                    su_name.last_name[:1])
    team_id = Team.objects.filter(Q(first_user=first_user,
                             second_user=second_user) | Q(first_user=second_user,
                                                          second_user=first_user))
    if team_id.exists():
        team_id = team_id.values_list('id', flat=True)
        return [False, gen_name, team_id]
    else:
        return [True, gen_name]


def generation_teams(request, pk):
    if request.POST:
        tour = Tournament.objects.get(id=pk)
        if tour.mode != 1:
            selected_users = json.loads(request.POST.get('users_id'))
            last_rang = Rang.objects.filter(user_id__in=selected_users).values(
                'user').annotate(Max('id')).values_list(
                'id__max', flat=True)
            players = list(Rang.objects.filter(id__in=last_rang).values_list(
                'user_id', flat=True).order_by('-rang'))
            if len(players) % 2 == 0:
                i = 0
                counts = len(players)
                players = my_replace(players)
                while i < (counts / 2):
                    first_user = Users.objects.get(id=players[i])

                    second_user = Users.objects.get(id=players[counts - 1 - i])
                    l = check_team_exist(first_user, second_user)
                    if l[0]:
                        new_team = Team.objects.create(name=l[1],
                                                       first_user=first_user,
                                                       second_user=second_user,
                                                       logo="")
                        new_team.tour.add(tour)
                        new_team.save()
                    else:
                        print l[2]
                        exist_team = Team.objects.get(id=l[2])
                        exist_team.tour.add(tour)
                        exist_team.save()
                    i += 1
                    # new_team = Team.objects.create()
            else:
                return HttpResponse(status='400')

            return HttpResponse(reverse_lazy('teams:teams'))
    else:
        return HttpResponseRedirect(reverse_lazy('teams:teams'))


def my_replace(players):
    count = len(players)
    i = 0
    rand_id2 = 50
    while i < count - 1:
        rand_id = random.randint(0, 100)
        if rand_id <= rand_id2:
            tmp = players[i]
            players[i] = players[i + 1]
            players[i + 1] = tmp
        i += 1
    return players


def create_tour(request):
    if request.POST:
        if request.user.is_superuser:
            form = CreateTeamForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('teams:teams'))
    else:
        return HttpResponseRedirect(reverse_lazy('teams:teams'))
