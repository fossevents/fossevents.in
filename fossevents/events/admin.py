# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from . import models


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Event, EventAdmin)
