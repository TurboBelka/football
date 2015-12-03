from django.conf.urls import url
from round_in_game import views

urlpatterns = [
    url(r'^$', views.ChooseTourView.as_view(), name='choose_tour'),
    url(r'^(?P<pk>[0-9]+)/$', views.get_all_in_tour, name='get_round_in_tour'),
    # url(r'^(?P<pk>[0-9]+)/teams/$', views.get_teams, name='get_teams'),
    url(r'^(?P<pk>[0-9]+)/teams/$', views.TeamList.as_view(), name='get_teams'),
    url(r'^(?P<pk>[0-9]+)/round/$', views.add_teams, name='add_teams'),
    url(r'^(?P<pk>[0-9]+)/gen_teams/$', views.gen_matchs, name='gen_matchs'),
    url(r'^create/$', views.create, name='create_round'),
    url(r'^(?P<pk>[0-9]+)/choose_type/$', views.choose_type, name='choose_type_round'),
]