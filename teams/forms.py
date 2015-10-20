from PIL import Image
from django.forms import ModelForm
from teams.models import Team


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['first_user', 'second_user', 'name', 'logo']

    def save(self, commit=True):
        new_team = Team(first_user=self.cleaned_data['first_user'],
                        second_user=self.cleaned_data['second_user'],
                        name=self.cleaned_data['name'])
        if self.cleaned_data['logo']:
            new_team.logo = self.cleaned_data['logo']
            image = Image.open(new_team.logo)
            size = (50, 50)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(new_team.logo)
        if commit:
            new_team.save()
        return new_team
