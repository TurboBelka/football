from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.UsersView.as_view(), name='index'),
    url(r'^login', auth_views.login, name='login',
        kwargs={'template_name': 'users/login.html'}),
    url(r'^logout', auth_views.logout, name='logout',
        kwargs={'next_page': '/index/'}),
    url(r'^loggedin', views.get_current_user),
    url(r'^registration', views.register_user, name='registration'),
    url(r'^vk_login', views.vk_login, name='vk_login'),
]
