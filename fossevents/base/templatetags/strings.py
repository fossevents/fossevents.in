from urlparse import urlparse

from django import template

register = template.Library()


@register.filter
def to_domain(value):
    parsed_url = urlparse(value.lower())
    return parsed_url.netloc
