
import requests

ENDPOINT = "http://localhost:8000/prestamos"
USERNAME = "mateo"
PASSWORD = "mateo123"

global prestamo_id

def test_llamar_prestamos():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_prestamos():
    global prestamo_id
    payload = {
        "prestamo_fechaEnt": "2024-03-11",
        "prestamo_fechaDev": "2024-10-11",
        "estudiante": 1
    }
    response = requests.post(ENDPOINT + '/', json=payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 201

    data = response.json()
    print(data)

    prestamo_id = data.get('id')

def test_update_prestamos():
    global prestamo_id
    updated_payload = {
        "prestamo_fechaEnt": "2024-03-11",
        "prestamo_fechaDev": "2024-03-20",
        "estudiante": 1
    }
    response = requests.put(ENDPOINT + f'/{prestamo_id}/', json=updated_payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

    data = response.json()
    print(data)

def test_delete_prestamos():
    global prestamo_id
    response = requests.delete(ENDPOINT + f'/{prestamo_id}/', auth=(USERNAME, PASSWORD))
    assert response.status_code == 204

    response = requests.get(ENDPOINT + f'/{prestamo_id}')
    assert response.status_code == 404
