# Third Party Stuff
from django.conf.urls import url

from .views import EventCreateView, EventUpdateView, event_review

uuid_regex = '[a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}'

app_name = 'events'
urlpatterns = [
    url(r'^add/$', EventCreateView.as_view(), name="create"),
    url(r'^update/(?P<slug>[-\w]+)-(?P<pk>%s)-(?P<token>%s)/$' % (uuid_regex, uuid_regex),
        EventUpdateView.as_view(), name="update"),
    url(r'^review/(?P<slug>[-\w]+)-(?P<pk>%s)-(?P<token>%s)/$' % (uuid_regex, uuid_regex),
        event_review, name="review"),
]
