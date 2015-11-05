from django.conf.urls import url
from match import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.ChooseRound.as_view(), name='match'),
    url(r'^(?P<pk>[0-9]+)/grid/$', views.grid, name='grid'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^save_changes/(?P<pk>[0-9]+)/', views.save_changes, name="save_changes"),
]