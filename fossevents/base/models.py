# -*- coding: utf-8 -*-


import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(TimeStampedModel, UUIDModel):
    '''
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    '''

    class Meta:
        abstract = True
