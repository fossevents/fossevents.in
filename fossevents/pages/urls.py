# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^privacy/$', TemplateView.as_view(template_name='pages/privacy.html'), name="privacy"),
    url(r'^search/$', views.search, name="search"),
]
