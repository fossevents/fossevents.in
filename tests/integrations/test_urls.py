import pytest

pytestmark = pytest.mark.django_db


def test_admin_interface(client):
    response = client.get('/admin/login/')
    assert response.status_code == 200
