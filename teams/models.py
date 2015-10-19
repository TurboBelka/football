from django.db import models
from users.models import Users


class Team(models.Model):
    name = models.CharField(max_length=200)
    first_user = models.ForeignKey(Users,
                                   related_name='first_user')
    second_user = models.ForeignKey(Users,
                                    related_name='second_user')
    logo = models.ImageField(blank=True, upload_to='static/teams_logo')
