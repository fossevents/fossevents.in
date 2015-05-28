# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)-(?P<pk>[-\w]+)/$', views.event_detail, name="detail"),
]
