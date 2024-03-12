
import requests

ENDPOINT = "http://localhost:8000/libros"
USERNAME = "mateo"
PASSWORD = "mateo123"

global libro_id

def test_llamar_libro():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_libro():
    global libro_id
    payload = {
        "libro_nombre": "Libro de Prueba",
        "libro_fechaPub": "2024-03-11",
        "libro_descripcion": "Prueba",
        "libro_stock": 5,
        "autor_id": 7
    }
    response = requests.post(ENDPOINT + '/', json=payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 201

    data = response.json()
    print(data)

    # Obtén el ID del autor creado
    libro_id = data.get('id')

def test_update_libro():
    global libro_id
    updated_payload = {
        "libro_nombre": "Libro de Prueba Modificado",
        "libro_fechaPub": "2024-03-11",
        "libro_descripcion": "Prueba Modificada",
        "libro_stock": 3,
        "autor_id": 7
    }
    response = requests.put(ENDPOINT + f'/{libro_id}/', json=updated_payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_delete_libro():
    global libro_id
    response = requests.delete(ENDPOINT + f'/{libro_id}/', auth=(USERNAME, PASSWORD))
    assert response.status_code == 204

    # Verifica que el autor haya sido eliminado
    response = requests.get(ENDPOINT + f'/{libro_id}')
    assert response.status_code == 404

