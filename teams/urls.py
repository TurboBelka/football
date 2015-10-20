from django.conf.urls import url
from teams import views

__author__ = 'user'

urlpatterns = [
    url(r'^$', views.GetAllTourView.as_view(), name='teams'),
    url(r'^teams', views.get_team_in_tour, name='team_in_tour'),
    url(r'^create_team', views.create_team, name='create_team'),
    url(r'^generate', views.generate_teams, name='generate_teams')
]
