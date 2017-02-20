import pytest
from django.core.urlresolvers import reverse
from django.utils import timezone

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_homepage(client):
    event = f.EventFactory(is_published=False)
    event2 = f.EventFactory(is_published=False, start_date=timezone.now()-timezone.timedelta(days=9),
                            end_date=timezone.now()-timezone.timedelta(days=8))
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    # should have 'events' in the template context
    assert 'events' in response.context
    assert 'upcoming_events' in response.context
    assert 'past_events' in response.context

    # should not display any event, if none are published
    assert len(response.context['events']) == 0
    assert len(response.context['upcoming_events']) == 0
    assert len(response.context['past_events']) == 0

    # should now contain one event, after it's published
    event.is_published = True
    event.save()
    event2.is_published = True
    event2.save()
    response = client.get(url)
    assert len(response.context['events']) == 0
    assert len(response.context['upcoming_events']) == 1
    assert len(response.context['past_events']) == 1
    assert response.context['upcoming_events'][0].id == event.id
    assert response.context['past_events'][0].id == event2.id


def test_homepage_search(client):
    event = f.EventFactory(is_published=True, name='test_event')
    f.EventFactory(is_published=True, start_date=timezone.now()-timezone.timedelta(days=9),
                   end_date=timezone.now()-timezone.timedelta(days=8))
    url = reverse('home')
    response = client.get(url, {'q': 'test'})
    assert response.status_code == 200

    # should have 'events' in the template context
    assert 'events' in response.context
    assert 'upcoming_events' in response.context
    assert 'past_events' in response.context

    assert len(response.context['events']) == 1
    assert len(response.context['upcoming_events']) == 0
    assert len(response.context['past_events']) == 0
    assert response.context['events'][0].id == event.id


def test_event_create(client, mocker):
    url = reverse('event-create')

    data = {
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }

    response = client.post(url, data)
    assert response.status_code == 302


EventErrorCasesData = [
    ({}, 'name'),
    ({
        # Name required field
        'name': '',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'name'),
    ({
        # Description required field
        'name': 'Event01',
        'description': '',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'description'),
    ({
        # Start date required field
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'start_date'),
    ({
         # End date required field
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
         # Format of start date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '12-08-2016',
         'end_date': '2016-08-13',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'start_date'),
    ({
         # Format of end date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '13-08-2016',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
         # End date should be greater than start date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '2016-08-11',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
        # Owner email required field
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': ''
    }, 'owner_email'),
]


@pytest.mark.parametrize("test_data,error_field", EventErrorCasesData)
def test_event_create_error(test_data, error_field, client):
    url = reverse('event-create')
    response = client.post(url, test_data)
    assert response.status_code == 200
    assert len(response.context['form'][error_field].errors)
