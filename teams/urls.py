from django.conf.urls import url
from teams import views

__author__ = 'user'

urlpatterns = [
    url(r'^$', views.GetAllTourView.as_view(), name='teams'),
    url(r'^teams', views.get_team_in_tour, name='team_in_tour'),
]
