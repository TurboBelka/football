from django.views import generic
from tournament.models import Tournament


class GetAllTourView(generic.ListView):
    template_name = 'teams/teams.html'
    context_object_name = 'tours'
    model = Tournament
