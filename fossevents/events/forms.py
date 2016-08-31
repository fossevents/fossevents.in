from django.forms import ModelForm

from .models import Event


class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')
