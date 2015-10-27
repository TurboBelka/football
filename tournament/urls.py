from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from tournament import views

urlpatterns = [
    url(r'^$', views.create_tour, name='tour'),
    url(r'^(?P<pk>[0-9]+)/', staff_member_required(views.EditTour.as_view()), name='edit'),
]