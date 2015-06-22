# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import reversion
from django.contrib import admin

from . import models


@admin.register(models.Event)
class EventAdmin(reversion.VersionAdmin):
    list_display = ['id', 'name', 'is_published', 'created', 'modified']
