from PIL import Image
from django.forms import ModelForm
from teams.models import Team
from tournament.models import Tournament


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['first_user', 'second_user', 'logo']

    def save(self, commit=True):
        new_team = Team(first_user=self.cleaned_data['first_user'],
                        second_user=self.cleaned_data['second_user'])
        if self.cleaned_data['logo']:
            new_team.logo = self.cleaned_data['logo']
            image = Image.open(new_team.logo)
            size = (50, 50)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(new_team.logo)
        if commit:
            new_team.save()
        return new_team


class CreateTourForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'mode', 'type_tour', 'date_start', 'date_end']
