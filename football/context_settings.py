from django.core.urlresolvers import reverse_lazy

__author__ = 'user'


def get_names(request):

    my_menus = {
        'Home': reverse_lazy('index:index'),

        # 'My profile': reverse_lazy(''),
                # 'Tournament': reverse_lazy(''),
                # 'LogIn': reverse_lazy('index:login'),
                # 'LogOut': reverse_lazy('index:logout'),
                }
    user = request.user
    if not user.is_authenticated():
        my_menus['LogIn'] = reverse_lazy('index:login')
    else:
        my_menus['LogOut'] = reverse_lazy('index:logout')
        my_menus['My profile'] = reverse_lazy('index:my_profile')
    return {'my_menus': my_menus}
