from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to="static/user_photo")
