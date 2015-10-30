from django.conf.urls import url
from match import views

urlpatterns = [
    url(r'', views.ChooseMatchInRound.as_view(), name='choose_round')
]