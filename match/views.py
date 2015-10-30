from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView
from match.models import Match
from teams.models import Team


class ChooseRound(ListView):
    model = Match
    template_name = 'match/get_all_matchs.html'
    context_object_name = 'matchs'

    def get_context_data(self, **kwargs):
        context = super(ChooseRound, self).get_context_data(**kwargs)
        context[self.context_object_name] = Match.objects.filter(my_round_id=
                                            self.kwargs.get('pk'))
        return context


def save_changes(request, pk):
    if request.method == 'POST':
        options = dict()
        if request.POST['team'] == 'first':
            options['first_team_goals'] = int(request.POST['goals'])
        else:
            options['second_team_goals'] = int(request.POST['goals'])
        Match.objects.filter(id=pk).update(**options)
        return HttpResponse(reverse_lazy('match:match', kwargs={'pk': pk}))
    else:
        return HttpResponse(status='400')
