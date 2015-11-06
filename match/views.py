import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum, F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from match.models import Match
from round_in_game.models import RoundInGame
from teams.models import Team
from tournament.models import Tournament


class ChooseRound(ListView):
    model = Match
    template_name = 'match/get_all_matchs.html'
    context_object_name = 'matchs'

    def get_context_data(self, **kwargs):
        context = super(ChooseRound, self).get_context_data(**kwargs)
        context[self.context_object_name] = Match.objects.filter(my_round_id=
        self.kwargs.get(
            'pk'))
        all_type_round = dict(RoundInGame.TYPE_RANG)
        cur_type = RoundInGame.objects.filter(
            id=self.kwargs.get('pk')).values_list('type_rang', flat=True)
        context['type_round'] = all_type_round.get(cur_type[0])
        tour_id = RoundInGame.objects.filter(
            id=int(self.kwargs.get('pk'))).values_list('tournament_id')
        tour = Tournament.objects.filter(id=tour_id).values_list('name',
                                                                 flat=True)
        context['tour'] = tour[0]
        context['round_id'] = self.kwargs.get('pk')
        return context


def save_changes(request, pk):
    if request.method == 'POST':
        options = dict()
        if request.POST['team'] == 'first':
            options['first_team_goals'] = int(request.POST['goals'])
        else:
            options['second_team_goals'] = int(request.POST['goals'])
        Match.objects.filter(id=pk).update(**options)
        return HttpResponse()
    else:
        return HttpResponse(status='400')


def grid(request, pk):
    tour_id = RoundInGame.objects.filter(id=pk).values_list('tournament_id',
                                                            flat=True)
    all_round = RoundInGame.objects.filter(tournament_id=tour_id[0]).exclude(
        type_rang=6).order_by('type_rang')
    return render(request, 'match/grid_template.html', context={
        'all_round': all_round})


def results(request, pk):
    my_query = '''select teams_team.id, teams_team.logo, teams_team.name, count(p.id) as count_games, sum(first_team_goals) as goals_scored, sum(second_team_goals) as goals_missed, first_team_id, sum(first_team_win) as first_victory,
                sum(second_team_win) as first_defeat, sum(first_team_win)*3 as points,
                case when sum(first_team_goals) > sum(second_team_goals) then sum(first_team_goals) - sum(second_team_goals)
                    else sum(second_team_goals) - sum(first_team_goals) end as difference
                from (
                    select match_match.first_team_id, match_match.first_team_goals, match_match.id as id, match_match.second_team_goals,
                            case when match_match.first_team_goals > match_match.second_team_goals then 1 else 0 end as first_team_win,
                            case when match_match.second_team_goals > match_match.first_team_goals then 1 else 0 end as second_team_win
                    from match_match
                        join round_in_game_roundingame on match_match.my_round_id=round_in_game_roundingame.id
                        join tournament_tournament on round_in_game_roundingame.tournament_id=tournament_tournament.id
                    where round_in_game_roundingame.type_rang=%(round_type)s and tournament_tournament.id=%(tour_id)s
                    union all
                    select match_match.second_team_id as first_team_id, match_match.second_team_goals as first_team_goals, match_match.id as id,
                            match_match.first_team_goals as second_team_goals,
                            case when match_match.second_team_goals > match_match.first_team_goals then 1 else 0 end as first_team_win,
                            case when match_match.first_team_goals > match_match.second_team_goals then 1 else 0 end as second_team_win
                    from match_match
                        join round_in_game_roundingame on match_match.my_round_id=round_in_game_roundingame.id
                        join tournament_tournament on round_in_game_roundingame.tournament_id=tournament_tournament.id
                    where round_in_game_roundingame.type_rang=%(round_type)s and tournament_tournament.id=%(tour_id)s) as p
                    join teams_team on teams_team.id=p.first_team_id
                group by first_team_id
                order by points desc, goals_scored desc''' % dict(tour_id=pk, round_type=6)

    res_table = Match.objects.raw(my_query)
    print res_table[0]
    for r in res_table:
        print r
    return render(request, 'match/results_table.html', context={
        'res_table': res_table
    })
