import pytest

pytestmark = pytest.mark.django_db


def test_admin_interface(client):
    public_urls = [
        '/admin/login/',
        '/',
        '/about/',
        '/privacy/',
    ]
    for url in public_urls:
        response = client.get('/admin/login/')
        assert response.status_code == 200
