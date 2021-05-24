from django.urls import reverse
from django.http import HttpResponseRedirect

from . import models


def match_token(function):
    """
    Decorator for views that checks that the user is authorized using the token.
    """

    def wrapper(request, *args, **kwargs):
        token = kwargs.get('token', '')
        event_id = kwargs.get('pk', '')
        event = models.Event.objects.filter(id=event_id, auth_token=token)
        if not event.exists():
            return HttpResponseRedirect(reverse('home'))
        return function(request, *args, **kwargs)
    return wrapper
