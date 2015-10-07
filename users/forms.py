from django.forms import ImageField
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    photo = ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'photo',
                  'password1', 'password2']

    def save(self, commit=True):
        print 123
        user = super(RegistrationForm, self).save(commit=commit)
        print user
        new_user = Users(user=user)
        new_user.photo = self.cleaned_data['photo']
        if commit:
            new_user.save()
        return new_user
