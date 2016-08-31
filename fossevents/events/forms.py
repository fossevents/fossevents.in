from django.forms import ModelForm, ValidationError

from .models import Event


class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if end_date:
            if end_date < start_date:
                raise ValidationError('End date should be greater than start date.')
        return end_date
