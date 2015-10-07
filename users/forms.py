from PIL import Image
from django.forms import ImageField
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    photo = ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'photo',
                  'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=commit)
        new_user = Users(user=user)
        if self.cleaned_data['photo']:
            new_user.photo = self.cleaned_data['photo']
            image = Image.open(new_user.photo)
            size = (50, 50)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(new_user.photo)
        if commit:
            new_user.save()

        return new_user
