from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client
from users.forms import RegistrationForm, ProfileForm
from users.models import Users


class UserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.csrf_client = Client(enforce_csrf_checks=True)
        self.django_user = User.objects.create_user(username='first',
                                                    first_name='user',
                                                    last_name='user',
                                                    email='email@vb.ru',
                                                    password='password')
        self.user = Users.objects.create(photo='', user=self.django_user)

    def test_index_view_have_users(self):
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(Users.objects.all().count(), 1)
        response = self.client.get(reverse_lazy('index:index'))
        self.assertQuerysetEqual(response.context['users_list'],
                                 ['<Users: first>'])

    def test_user_login(self):
        self.client.login({'username': 'first', 'password': 'password'})
        self.assertIsNotNone(self.client.session)

    def form_registration_test(self, data):
        form_data = data
        form = RegistrationForm(data=form_data)
        return self.assertTrue(form.is_valid())

    def test_user_registration(self):
        form_data = {'username': 'second',
                     'first_name': 'user2',
                     'last_name': 'user2',
                     'email': 'user2@bk.ru',
                     'password1': 'password2',
                     'photo': '',
                     'password2': 'password2'}
        if self.form_registration_test(form_data):
            self.csrf_client.post(reverse_lazy('index:registration'))
            self.assertEqual(len(User.objects.filter(username='second')), 1)
            self.assertEqual(len(Users.objects.filter(user__username='second')), 1)

    def test_user_profile(self):
        self.client.login(username='first', password='password')
        response = self.client.get(reverse_lazy('index:my_profile'))
        self.assertIsInstance(response.context['form'], ProfileForm)
