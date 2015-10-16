from django.conf.urls import url
from teams import views

__author__ = 'user'

urlpatterns = [
    url(r'^$', views.GetAllTourView.as_view(), name='teams'),
]
