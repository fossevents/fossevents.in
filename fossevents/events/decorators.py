import uuid

from django.http import HttpResponseRedirect

from . import models


def match_token(function):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """

    def wrapper(request, *args, **kwargs):
        token = uuid.UUID(kwargs['token']) if kwargs.get('token') else ''
        event_id = kwargs.get('pk')
        event = models.Event.objects.filter(id=event_id, auth_token=token)
        if not event.exists():
            return HttpResponseRedirect('/')
        return function(request, *args, **kwargs)
    return wrapper
