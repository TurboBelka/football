from django.conf.urls import url
from match import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.ChooseRound.as_view(), name='match'),
    url(r'^save_changes/(?P<pk>[0-9]+)/', views.save_changes, name="save_changes"),
]