# -*- coding: utf-8 -*-
# Standard Library
import threading
import datetime

# Third Party Stuff
import factory
from factory import fuzzy


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


class EventFactory(Factory):

    class Meta:
        model = "events.Event"
        strategy = factory.CREATE_STRATEGY

    name = factory.Sequence(lambda n: "fossevent{}".format(n))
    start_date = fuzzy.FuzzyDate(datetime.date.today(), datetime.date(2017, 1, 1)).fuzz()
    end_date = start_date + datetime.timedelta(3)
    # logo
    # status = factory.Iterator(dict(CONFERENCE_STATUS_LIST).keys())
