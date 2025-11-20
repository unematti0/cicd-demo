import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == '2.0.0'  # Uuendatud vastavalt uuele versioonile
    assert 'message' in data

def test_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    products = response.get_json()
    assert len(products) == 2
    
    # Kontrolli et kõik hinnad on positiivsed
    for product in products:
        assert product['price'] > 0, f"Hind peab olema positiivne! Leitud: {product['price']}"

def test_version_endpoint(client):
    response = client.get('/api/version')
    assert response.status_code == 200
    data = response.get_json()
    assert data['version'] == '2.0.0'
    assert data['build'] == 'stable'

def test_status_endpoint(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    data = response.get_json()
    assert data['api'] == 'running'
    assert data['version'] == '2.0.0'
    assert 'endpoints' in data
    assert '/api/status' in data['endpoints']
