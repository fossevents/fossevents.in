from django import forms

from .models import Event
from .tasks import send_aync_confirmation_email


class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description here Markdown'}),)
    start_date = forms.DateTimeField(input_formats=["%d-%m-%Y", "%d-%m-%Y %H:%M:%S", "%d-%m-%Y %H:%M:%S %Z"],
                                     widget=forms.DateTimeInput(attrs={'placeholder': 'DD-MM-YYYY HH:MM:SS'}))
    end_date = forms.DateTimeField(input_formats=["%d-%m-%Y", "%d-%m-%Y %H:%M:%S", "%d-%m-%Y %H:%M:%S %Z"],
                                   widget=forms.DateTimeInput(attrs={'placeholder': 'DD-MM-YYYY HH:MM:SS'}))

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
        send_aync_confirmation_email.apply_async((str(instance.id),))
        return instance
