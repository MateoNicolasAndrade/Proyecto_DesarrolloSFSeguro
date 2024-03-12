
import requests

ENDPOINT = "http://localhost:8000/user"
USERNAME = "mateo"
PASSWORD = "mateo123"

global user_id

def test_llamar_user():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_user():
    global user_id
    payload = {
        "name": "Usuario de Prueba",
        "lastname": "Cazares",
        "email": "test_user@hotmail.com",
        "password": "abc123jsjsjsfff",
        "role": "estudiante"
    }
    response = requests.post(ENDPOINT + '/', json=payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 201

    data = response.json()
    print(data)

    # Obtén el ID del autor creado
    user_id = data.get('id')

def test_update_user():
    global user_id
    updated_payload = {
        "name": "Usuario de Prueba Modif",
        "lastname": "Suarez",
        "email": "test_user1@hotmail.com",
        "password": "aaabbbccc12345",
        "role": "bibliotecario"
    }
    response = requests.put(ENDPOINT + f'/{user_id}/', json=updated_payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

    data = response.json()
    print(data)

def test_delete_user():
    global user_id
    response = requests.delete(ENDPOINT + f'/{user_id}/', auth=(USERNAME, PASSWORD))
    assert response.status_code == 204

    # Verifica que el autor haya sido eliminado
    response = requests.get(ENDPOINT + f'/{user_id}')
    assert response.status_code == 404


