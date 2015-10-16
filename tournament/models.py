from django.db import models


class Tournament(models.Model):
    MODE_TOUR = (
        (1, 'finished'),
        (2, 'current'),
        (3, 'not_started'),
    )
    TYPE_TOUR = (
        (1, '1/8'),
        (2, '1/4'),
        (3, '1/2'),
        (4, 'final'),
        (5, 'third_place'),
        (6, 'regular'),
    )
    mode = models.SmallIntegerField(choices=MODE_TOUR)
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
    type_tour = models.SmallIntegerField(choices=TYPE_TOUR)
