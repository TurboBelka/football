from django.core.urlresolvers import reverse_lazy

__author__ = 'user'


def get_names(request):

    my_menus = {
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
    return {'my_menus': my_menus}
