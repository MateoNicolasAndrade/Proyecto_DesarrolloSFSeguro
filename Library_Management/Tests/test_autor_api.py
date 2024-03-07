import requests

ENDPOINT = "http://localhost:8000/autores"

def test_llamar_autor():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_autor():
    payload = {
        "autor_nombre": "Juan Perez",
        "autor_fechaNac": "2024-03-06",
        "autor_nacionalidad": "Mexicano",
    }
    response = requests.post(ENDPOINT + '/', json=payload)
    assert response.status_code == 200 

    data = response.json()
    print(data)    
