import pytest
from portifolio_app import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def resp_home(client):
    return client.get('/')


def teste_home(resp_home):
    assert resp_home.status_code == 200
