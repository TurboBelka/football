from django.forms import ModelForm
from tournament.models import Tournament


class CreateTourForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'mode', 'date_start', 'date_end']
