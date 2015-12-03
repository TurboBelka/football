from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from collections import OrderedDict
from tournament.models import Tournament

__author__ = 'user'


def get_names(request):

    my_menus = OrderedDict({
        'Home': reverse_lazy('index:index'),
    })
    form_for_login = AuthenticationForm()

    if not request.user.is_authenticated():
        my_menus['LogIn'] = reverse_lazy('index:login')
        return {'my_menus': my_menus, 'form_for_login': form_for_login}
    else:
        my_menus['My profile'] = reverse_lazy('index:my_profile')
        my_menus['Tours'] = reverse_lazy('teams:teams')
        my_menus['Round'] = reverse_lazy('round:choose_tour')
        my_menus['Match'] = reverse_lazy('match:match', kwargs={'pk': 1})
        last_tour_id = Tournament.objects.order_by('-id').distinct().values_list('id', flat=True)
        if last_tour_id:
            my_menus['Results'] = reverse_lazy('match:results', kwargs={'pk': last_tour_id[0]})
        my_menus['LogOut'] = reverse_lazy('index:logout')
        return {'my_menus': my_menus}
