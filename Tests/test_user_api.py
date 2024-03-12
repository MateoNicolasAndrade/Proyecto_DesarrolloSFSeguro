import requests

ENDPOINT = "http://localhost:8000/user"

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_doce = response.status_code
print(status_doce)