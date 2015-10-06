from django.db import models


class TypeOfTour(models.Model):
    TYPE_TOUR = (
        (1, '1/8'),
        (2, '1/4'),
        (3, '1/2'),
        (4, 'final'),
        (5, 'third_place'),
        (6, 'regular'),
    )
    name = models.SmallIntegerField(choices=TYPE_TOUR)
