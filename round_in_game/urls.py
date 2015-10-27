from django.conf.urls import url
from round_in_game import views

urlpatterns = [
    url(r'^$', views.get_all_in_tour, name='round'),
]