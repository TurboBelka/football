from django.shortcuts import render
from django.views import generic
from .models import Users
from django.contrib.auth.models import User


class UsersView(generic.ListView):
    template_name = 'login.html'
    context_object_name = 'users'
    model = Users

