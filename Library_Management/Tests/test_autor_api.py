
import requests

ENDPOINT = "http://localhost:8000/autores"
USERNAME = "mateo"
PASSWORD = "mateo123"

global autor_id

def test_llamar_autor():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_autor():
    global autor_id
    payload = {
        "autor_nombre": "Juan Perez",
        "autor_fechaNac": "2024-03-06",
        "autor_nacionalidad": "Mexicano",
    }
    response = requests.post(ENDPOINT + '/', json=payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 201

    data = response.json()
    print(data)

    # Obtén el ID del autor creado
    autor_id = data.get('id')

def test_update_autor():
    global autor_id
    updated_payload = {
        "autor_nombre": "Juan Perez Modificado",
        "autor_fechaNac": "2024-03-07",
        "autor_nacionalidad": "Mexicano",
    }
    response = requests.put(ENDPOINT + f'/{autor_id}/', json=updated_payload, auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_delete_autor():
    global autor_id
    response = requests.delete(ENDPOINT + f'/{autor_id}/', auth=(USERNAME, PASSWORD))
    assert response.status_code == 204

    # Verifica que el autor haya sido eliminado
    response = requests.get(ENDPOINT + f'/{autor_id}')
    assert response.status_code == 404

# Ejecuta las pruebas
#test_llamar_autor()
#test_create_autor()
#test_update_autor()
#test_delete_autor()


