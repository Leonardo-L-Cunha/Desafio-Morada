import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_should_return_the_minimum_number_of_cells(client):

    amount = {'valor': 380}

    response = client.post('/api/saque', json=amount)

    assert response.status_code == 200

    response_data = response.get_json()

    expected_response = {
        '100': 3,
        '50': 1,
        '20': 1,
        '10': 1,
        '5': 0,
        '2': 0,
    }

    assert response_data == expected_response