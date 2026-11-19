import requests

url = "http://127.0.0.1:8000/users/"

user_data = {
    "username": "Alejandro",
    "email": "b@example.com",
    "age": 20
}

response = requests.post(url, json=user_data)
print(f"Código de respuesta: {response.status_code}")
guardar = response.json()
import json
with open("./prueba.json", encoding="utf-8", mode="w") as file_out:
    json.dump(guardar, file_out)
