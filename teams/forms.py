from PIL import Image
from django.forms import ModelForm, ValidationError
from teams.models import Team
from tournament.models import Tournament
from users.models import Users


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['first_user', 'second_user', 'logo']

    def __init__(self, *args, **kwargs):
        tour_id = kwargs.pop("tour_id")
        super(CreateTeamForm, self).__init__(*args, **kwargs)
        all_in_tour = Team.objects.filter(tour__id=tour_id).values_list('first_user', 'second_user')
        users_in_tour = []
        for item in all_in_tour:
            users_in_tour.append(item[0])
            users_in_tour.append(item[1])
        self.fields['first_user'].queryset = Users.objects.exclude(id__in=users_in_tour)
        self.fields['second_user'].queryset = Users.objects.exclude(id__in=users_in_tour)

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

    def clean(self):
        cleaned_data = super(CreateTeamForm, self).clean()
        f_user = cleaned_data.get("first_user")
        s_user = cleaned_data.get("second_user")

        if f_user == s_user:
            raise ValidationError("First user is equal second user")
        return cleaned_data
