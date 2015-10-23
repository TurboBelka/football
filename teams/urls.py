from django.conf.urls import url
from teams import views

__author__ = 'user'

urlpatterns = [
    url(r'^$', views.GetAllTourView.as_view(), name='teams'),
    url(r'^(?P<pk>[0-9]+)/', views.get_team_in_tour, name='team_in_tour'),
    url(r'^create_team/(?P<pk>[0-9]+)/', views.create_team, name='create_team'),
    url(r'^generate/(?P<pk>[0-9]+)/', views.generate_teams, name='generate_teams'),
    url(r'^generation/(?P<pk>[0-9]+)/', views.generation_teams, name='generation'),
    url(r'^create_tour', views.create_tour, name='create_tour')
]
