import json
from tempfile import NamedTemporaryFile
from django.core.files import File
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg, Max
from django.shortcuts import render, redirect
from django.views import generic
from football.settings import VK_API_SECRET, VK_CLIENT_ID
from .models import Users
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm, ProfileForm, MyPasswordChangeForm
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.views import login as django_login
from django.contrib.auth.decorators import login_required
from rang.models import Rang


def get_current_user(request):
    return render(request, 'users/loggedin.html')


def vk_login(request):
    code = request.GET['code']
    url = 'https://oauth.vk.com/access_token'
    params = {
        'client_id': VK_CLIENT_ID,
        'client_secret': VK_API_SECRET,
        'redirect_uri': 'http://localhost:8000/index/vk_login',
        'code': code,
    }
    r = requests.get(url, params)
    d = json.loads(r.text)

    url1 = 'http://api.vkontakte.ru/method/users.get'
    params1 = {
        'uids': d['user_id'],
        'fields': 'photo_50',

    }
    r = requests.get(url1, params1)
    params = json.loads(r.text)
    params = params['response']
    file_name = '%s.jpeg' % d['email']

    user, created = User.objects.get_or_create(
        defaults={
            'first_name': params[0]['first_name'],
            'last_name': params[0]['last_name'],
            'username': d['email'],
        },
        email=d['email'])
    user.save()

    my_user, created = Users.objects.get_or_create(
        user=user)
    if created:
        f_tmp = NamedTemporaryFile()
        f_tmp.write(requests.get(params[0]['photo_50']).content)
        f_tmp.flush()
        my_user.photo.save(file_name, File(f_tmp))
        my_user.save()

    set_rang(my_user)

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    login(request, user)
    return redirect('/index/loggedin/')


def fb_login(request):
    user_info = json.loads(request.POST.get("user", ""))
    file_name = '%s.jpeg' % user_info['email']

    user, created = User.objects.get_or_create(
        defaults={
            'first_name': user_info['first_name'],
            'last_name': user_info['last_name'],
            'username': user_info['email'],
        },
        email=user_info['email'])
    user.save()

    my_user, created = Users.objects.get_or_create(
        user=user)
    picture = user_info['picture'].get('data')

    if created:
        f_tmp = NamedTemporaryFile()
        f_tmp.write(requests.get(picture['url']).content)
        f_tmp.flush()
        my_user.photo.save(file_name, File(f_tmp))
        my_user.save()

    set_rang(my_user)

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    login(request, user)
    return HttpResponse(reverse_lazy('index:loggedin'))


def set_rang(user):
    if Rang.objects.count() == 0:
        Rang.objects.create(rang=25, user=user)
    else:
        max_id = Rang.objects.values('user_id').annotate(Max('id'))
        id_arr = []
        for item in max_id:
            id_arr.append(item['id__max'])
        res = Rang.objects.filter(id__in=id_arr).aggregate(Avg('rang'))
        # rang_for_new_user = random.randint(0, my_round(res['rang__avg']))
        Rang.objects.create(rang=round(res['rang__avg'])*0.7,
                            user=user)


def register_user(request):
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            my_new_user = form.save()
            set_rang(my_new_user)

            return HttpResponseRedirect(reverse_lazy('index:index'))
        else:
            return render(request, 'users/registration.html', context={
                'form': form})
    else:
        return render(request, 'users/registration.html', context={
            'form': RegistrationForm()
        })


def block_login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    else:
        return django_login(request, 'users/login.html')


@login_required(login_url='/index/login/')
def my_profile(request):
    if request.method == 'POST':
        my_form = ProfileForm(request.POST, request.FILES,
                              instance=request.user)

        if my_form.is_valid():
            my_form.save()
            return HttpResponseRedirect(reverse_lazy('index:index'))
        else:
            return render(request, 'users/my_profile.html', context={
                'form': my_form
            })
    else:
        return render(request, 'users/my_profile.html', context={
            'form': ProfileForm(instance=request.user),
            'change_pass': MyPasswordChangeForm(user=request.user)
        })


def change_pass(request):
    if request.method == 'POST':
        change_pass_form = MyPasswordChangeForm(user=request.user,
                                                data=request.POST)

        if change_pass_form.is_valid():
            change_pass_form.save()
            return HttpResponseRedirect(reverse_lazy('index:my_profile'))
        else:
            return HttpResponse(json.dumps(change_pass_form.errors),
                                content_type='application/json')
    else:
        return HttpResponse(status='400')


class UsersView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users_list'
    model = Users
