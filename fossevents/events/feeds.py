from django.contrib.syndication.views import Feed
from .models import Event
from django.utils.feedgenerator import Atom1Feed


class LatestEvents(Feed):
    title = "Foss Events Latest Feed"
    link = '/'

    def items(self):
        return Event.objects.filter(is_published=True).order_by('start_date')[:400]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description


class AtomLatestEventFeed(LatestEvents):
    feed_type = Atom1Feed
