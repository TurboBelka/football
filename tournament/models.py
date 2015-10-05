from django.db import models


# Create your models here.
class Tournament(models.Model):
    mode = models.CharField(max_length=200)
