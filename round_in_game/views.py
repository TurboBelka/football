from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from round_in_game.models import RoundInGame
from tournament.models import Tournament


def get_all_in_tour(request, pk):
    tours = Tournament.objects.all()
    # rounds = RoundInGame.objects.filter(tournament_id=pk)
    return render(request, 'my_round/get_all_in_tour.html', context={
        'tours': tours})
