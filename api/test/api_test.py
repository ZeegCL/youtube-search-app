import pytest
from ..app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_root_returns_status_200(client):
    req = client.get('/')
    assert req.status_code == 200

def test_get_ping_returns_status_200(client):
    req = client.get('/ping')
    assert req.status_code == 200

def test_get_root_returns_status_400_when_terms_are_not_sent(client):
    req = client.get('/api/search')
    assert req.status_code == 400

def test_get_root_returns_status_200_when_terms_are_sent(client):
    req = client.get('/api/search?q=foo')
    assert req.status_code == 200