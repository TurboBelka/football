from django.conf.urls import url
from tournament import views

urlpatterns = [
    url(r'^$', views.create_tour, name='tour'),
]