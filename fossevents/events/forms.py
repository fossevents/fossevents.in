from django import forms
from django_markdown.widgets import MarkdownWidget

from .models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': MarkdownWidget(attrs={'placeholder': 'Enter description here'}),
            'start_date': forms.DateTimeInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'end_date': forms.DateTimeInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'http://example.com'}),
            'owner_email': forms.EmailInput(attrs={'placeholder': 'user@example.com'}),
        }

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if end_date:
            if end_date < start_date:
                raise forms.ValidationError('End date should be greater than start date.')
        return end_date
