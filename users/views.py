from django.shortcuts import render
from django.views import generic
from .models import Users
from django.http import HttpResponseRedirect
from .forms import RegistrationForm


def get_current_user(request):
    return render(request, 'users/loggedin.html')


# class UserRegistration(generic.FormView):
#     template_name = 'users/registration.html'
#     form_class = RegistrationForm
#     success_url = '/index/'
#
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
