import json
from django.shortcuts import render, redirect
from django.views import generic
import shutil
from football.settings import VK_API_SECRET, VK_CLIENT_ID
from .models import Users
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login


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
    path = '/static/user_photo/' \
           # % d['email']
    r = requests.get(params[0]['photo_50'])
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    if User.objects.filter(email=d['email']).exists():
        user = User.objects.get(email=d['email'])
        if not Users.objects.filter(user=user).exists():
            user.last_name = params[0]['last_name']
            user.first_name = params[0]['first_name']
            user.save()

            Users.objects.create(user=user, photo=f)
    else:
        user = User.objects.create_user(username=d['email'],
                                        email=d['email'],
                                        password='qwerty',)
        user.last_name = params[0]['last_name']
        user.first_name = params[0]['first_name']
        user.save()
        Users.objects.create(user=user, photo=f)

    # new_user = authenticate(username=user.username, password=user.password)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.save()
    login(request, user)
    return redirect('/index/loggedin/')

# class UserRegistration(generic.FormView):
#     template_name = 'users/registration.html'
#     form_class = RegistrationForm
#     success_url = '/index/'

#     def form_valid(self, request):
#         form = request.POST
#         form.save()


def register_user(request):
    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'users/registration.html', context={
                'form': form})
    else:
        return render(request, 'users/registration.html', context={
            'form': RegistrationForm()
        })


class UsersView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users_list'
    model = Users
