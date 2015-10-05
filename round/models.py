from django.db import models
from tournament.models import Tournament
from type_of_tour.models import TypeOfTour


# Create your models here.
class Round(models.Model):
    id_tournament = models.ForeignKey(Tournament)
    id_type_of_tour = models.ForeignKey(TypeOfTour)
