from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from tournament.forms import CreateTourForm, EditTourForm
from tournament.models import Tournament


def create_tour(request):
    if request.POST:
        if request.user.is_superuser:
            form = CreateTourForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('teams:teams'))
            else:
                return render(request, 'tour/create_tour.html', context={
                    'form': form})
    else:
        return render(request, 'tour/create_tour.html', context={
                    'form': CreateTourForm()})


class EditTour(UpdateView):
    model = Tournament
    template_name = 'tour/edit_tour.html'
    form_class = EditTourForm
    success_url = '/teams/'
