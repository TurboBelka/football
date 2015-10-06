from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User)
    photo = models.CharField(max_length=200)
    rang = models.DecimalField(max_digits=2, decimal_places=2)
