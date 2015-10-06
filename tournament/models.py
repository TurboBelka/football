from django.db import models


class Tournament(models.Model):
    MODE_TOUR = (
        (1, 'finished'),
        (2, 'current'),
        (3, 'not_started'),
    )
    mode = models.SmallIntegerField(choices=MODE_TOUR)
