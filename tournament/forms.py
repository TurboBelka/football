from django.core.exceptions import ValidationError
from django.forms import ModelForm
from tournament.models import Tournament


class FormControlMixin(object):
    def __init__(self, *args, **kwargs):
        super(FormControlMixin, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs.update({'class': 'form-control'})


class CreateTourForm(FormControlMixin, ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'mode', 'date_start', 'date_end']

    def clean(self):
        cleaned_data = super(CreateTourForm, self).clean()
        start_date = cleaned_data['date_start']
        end_date = cleaned_data['date_end']

        if start_date > end_date:
            raise ValidationError("Change date start")
        return cleaned_data


class EditTourForm(FormControlMixin, ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'mode', 'date_start', 'date_end']

    def clean(self):
        cleaned_data = super(EditTourForm, self).clean()
        start_date = cleaned_data['date_start']
        end_date = cleaned_data['date_end']

        if start_date > end_date:
            raise ValidationError("Change date start")
        return cleaned_data

