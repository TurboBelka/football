from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy

__author__ = 'user'


def get_names(request):

    my_menus = {
        'Home': reverse_lazy('index:index'),
    }
    form_for_login = AuthenticationForm()

    if not request.user.is_authenticated():
        my_menus['LogIn'] = reverse_lazy('index:login')
        return {'my_menus': my_menus, 'form_for_login': form_for_login}
    else:
        my_menus['LogOut'] = reverse_lazy('index:logout')
        my_menus['My profile'] = reverse_lazy('index:my_profile')
        my_menus['Tours'] = reverse_lazy('teams:teams')
        return {'my_menus': my_menus}
