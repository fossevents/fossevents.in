# Third Party Stuff
from django.conf.urls import url

from .views import EventCreateView, EventUpdateView

uuid_regex = '[a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}'

urlpatterns = [
    url(r'^add/$', EventCreateView.as_view(), name="event-create"),
    url(r'^update/(?P<slug>[-\w]+)-(?P<pk>%s)/$' % uuid_regex, EventUpdateView.as_view(), name="event-update"),
]
