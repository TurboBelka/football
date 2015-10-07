from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(blank=True, upload_to="static/user_photo")

    def __str__(self):
        return self.user.username
