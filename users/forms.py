from django.forms import ImageField
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class UsersForm(UserCreationForm):
    photo = ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'photo',
                  'password1', 'password2']

    def save(self, commit=True):
        user = super(UsersForm, self).save(commit=False)
        my_user = Users(user=user)
        my_user.photo = self.cleaned_data['photo']
        if commit:
            my_user.save()
        return my_user
