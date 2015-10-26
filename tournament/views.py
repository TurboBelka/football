from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from tournament.forms import CreateTourForm


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
