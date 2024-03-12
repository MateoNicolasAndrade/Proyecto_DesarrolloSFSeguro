import requests

ENDPOINT = "http://localhost:8000/detalles"
USERNAME = "mateo"
PASSWORD = "mateo123"

global detalle_id

def test_llamar_detalleprestamos():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_detalleprestamos():
    global detalle_id
    payload = {
        "autor": 6,
        "libro": 12,
        "estudiante": 1,
        "prestamo": 1
    }
    response = requests.post(ENDPOINT + '/', json=payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 201

    data = response.json()
    print(data)

    detalle_id = data.get('id')

def test_update_detalleprestamos():
    global detalle_id
    updated_payload = {
        "autor": 6,
        "libro": 11,
        "estudiante": 1,
        "prestamo": 1
    }
    response = requests.put(ENDPOINT + f'/{detalle_id}/', json=updated_payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

    data = response.json()
    print(data)

def test_delete_detalleprestamos():
    global detalle_id
    response = requests.delete(ENDPOINT + f'/{detalle_id}/', auth=(USERNAME, PASSWORD))
    assert response.status_code == 204

    response = requests.get(ENDPOINT + f'/{detalle_id}')
    assert response.status_code == 404
