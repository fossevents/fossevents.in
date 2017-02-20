# -*- coding: utf-8 -*-
# Standard Library
import threading
import datetime

# Third Party Stuff
import factory
from django.conf import settings
from django.utils import lorem_ipsum


class Factory(factory.DjangoModelFactory):
    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True

    _SEQUENCE = 1
    _SEQUENCE_LOCK = threading.Lock()

    @classmethod
    def _setup_next_sequence(cls):
        with cls._SEQUENCE_LOCK:
            cls._SEQUENCE += 1
        return cls._SEQUENCE


class UserFactory(Factory):

    class Meta:
        model = settings.AUTH_USER_MODEL
        strategy = factory.CREATE_STRATEGY

    username = factory.Sequence(lambda n: 'user%04d' % n)
    first_name = 'User'
    last_name = factory.Sequence(lambda n: '%04d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
    password = factory.PostGeneration(lambda obj, *args, **kwargs: obj.set_password('test'))


class EventFactory(Factory):

    class Meta:
        model = "events.Event"
        strategy = factory.CREATE_STRATEGY

    name = factory.Sequence(lambda n: "fossevent{}".format(n))
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=3)
    description = lorem_ipsum.paragraph()
    # logo
    # status = factory.Iterator(dict(CONFERENCE_STATUS_LIST).keys())
