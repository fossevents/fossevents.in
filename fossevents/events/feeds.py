# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

from .services import get_public_event_listings


class LatestEvents(Feed):
    title = "FOSS Events Latest Feed"
    link = '/'
    feed_type = Rss201rev2Feed
    item_guid_is_permalink = True

    def items(self):
        return get_public_event_listings()[:15]

    def item_title(self, item):
        return item.name

    def item_link(self, item):
        return item.get_absolute_url() + '?src=feed'

    def item_updateddate(self, item):
        return item.modified

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.description_html

    def feed_copyright(self):
        return "Copyright © FOSSEvents.in"


class AtomLatestEventFeed(LatestEvents):
    feed_type = Atom1Feed
