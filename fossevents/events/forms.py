from django import forms

from .models import Event, EventReview


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
    homepage = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'http://example.com', 'type': 'text'}))

    class Meta:
        model = Event
        exclude = ('auth_token', 'is_published')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Title'}),
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


class EventReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter notes or comments...', 'rows': 2},),
                              help_text='<a href="https://guides.github.com/features/mastering-markdown/">'
                                        'Markdown supported</a>',
                              required=False)

    class Meta:
        model = EventReview
        exclude = ('event', 'moderator')
        widgets = {'is_approved': forms.HiddenInput()}

    def clean(self):
        cleaned_data = super().clean()
        is_approved = cleaned_data.get('is_approved')
        comment = cleaned_data.get('comment')
        if not is_approved and not comment:
            self.add_error('comment', forms.ValidationError('Reject reason is required.'))
        return cleaned_data
