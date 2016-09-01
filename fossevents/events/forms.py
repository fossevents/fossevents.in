from django import forms

from .models import Event
from .services import send_confirmation_mail


class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description here Markdown'}),)
    start_date = forms.DateTimeField(input_formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M"],
                                     widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DDTHH:MM',
                                                                       'type': 'datetime-local'},
                                                                format='%Y-%m-%dT%H:%M'))
    end_date = forms.DateTimeField(input_formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M"],
                                   widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DDTHH:MM',
                                                                     'type': 'datetime-local'},
                                                              format='%Y-%m-%dT%H:%M'))

    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'http://example.com'}),
            'owner_email': forms.EmailInput(attrs={'placeholder': 'user@example.com'}),
        }

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if end_date and start_date:
            if end_date < start_date:
                raise forms.ValidationError('End date should be greater than start date.')
        return end_date

    def save(self, commit=True):
        instance = super(EventCreateForm, self).save(commit=commit)
        send_confirmation_mail(instance)
        return instance
