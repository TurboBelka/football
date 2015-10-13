from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.UsersView.as_view(), name='index'),
    url(r'^login', views.block_login_page, name='login'),
    url(r'^logout', auth_views.logout, name='logout',
        kwargs={'next_page': '/index/'}),
    url(r'^loggedin', views.get_current_user, name='loggedin'),
    url(r'^registration', views.register_user, name='registration'),
    url(r'^vk_login', views.vk_login, name='vk_login'),
    url(r'^fb_login', views.fb_login, name='fb_login'),
    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^change_pass', views.change_pass, name='change_pass')
]
