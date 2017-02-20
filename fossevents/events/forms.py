from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description...'},),
                                  help_text='<a href="https://guides.github.com/features/mastering-markdown/">'
                                            'Markdown supported</a>')
    start_date = forms.DateTimeField(input_formats=["%Y-%m-%d", "%Y-%m-%d %H:%M"],
                                     widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM',
                                                                       'type': 'datetime'},
                                                                format='%Y-%m-%d %H:%M'))
    end_date = forms.DateTimeField(input_formats=["%Y-%m-%d", "%Y-%m-%d %H:%M"],
                                   widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM',
                                                                     'type': 'datetime'},
                                                              format='%Y-%m-%d %H:%M'))

    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title'}),
            'homepage': forms.URLInput(attrs={'placeholder': 'http://example.com'}),
            'owner_email': forms.EmailInput(attrs={'placeholder': 'user@example.com'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if end_date and start_date:
            if end_date < start_date:
                self.add_error('end_date',
                               forms.ValidationError('End date should be greater than or equal to start date.'))
        return cleaned_data
