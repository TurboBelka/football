from django.db import models
from users.models import Users


class Team(models.Model):
    name = models.CharField(max_length=200)
    first_user = models.ForeignKey(Users,
                                   related_name='%(class)s_requests_created')
    second_user = models.ForeignKey(Users)
