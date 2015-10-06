from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.UsersView.as_view(), name='login'),
]