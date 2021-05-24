# -*- coding: utf-8 -*-

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db

global_footer_links = [
    'About',
    'Developers',
    'Privacy',
    'Report an issue',
]


def assert_title_and_links_on_page(browser, url, title, links_text):
    browser.visit(url)
    assert title in browser.title
    for link_text in links_text:
        assert browser.find_link_by_text(link_text)


def test_homepage(browser):
    url = reverse('home')
    assert_title_and_links_on_page(browser, url, "FossEvents", global_footer_links)


def test_about_page(browser):
    url = reverse('about')
    assert_title_and_links_on_page(browser, url, "About", global_footer_links)


def test_privacy_page(browser):
    url = reverse('privacy')
    assert_title_and_links_on_page(browser, url, "Privacy", global_footer_links)
