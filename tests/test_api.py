import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from APIFIISPUCPR import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fiis_api(client):
    response = client.get('/api/fiis')
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    if data:
        item = data[0]
        assert "ticker" in item
        assert "price" in item
        assert "dividend_yield" in item
        assert "last_dividend" in item
        assert "last_dividend_date" in item

import pytest
from APIFIISPUCPR import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_fiis_api(client):
    response = client.get('/api/fiis')
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    if data:
        item = data[0]
        assert "ticker" in item
        assert "price" in item
        assert "dividend_yield" in item
        assert "last_dividend" in item
        assert "last_dividend_date" in item
