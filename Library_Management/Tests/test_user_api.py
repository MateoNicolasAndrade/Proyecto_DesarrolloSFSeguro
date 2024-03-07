import requests

ENDPOINT = "http://localhost:8000/user"

def test_llamar_user():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    