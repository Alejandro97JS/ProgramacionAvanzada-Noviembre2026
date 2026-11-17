import requests

# url = "http://127.0.0.1:8000/hello/12"
# response = requests.post(url)
# print(response.text)
# print(response.status_code)
# # Esto debe haber fallado, porque mi API no admite /hello/<num>
# assert response.status_code == 200 

# # Llamada correcta:
# url = "http://127.0.0.1:8000/hello/a"
# response = requests.get(url)
# # Esto debe haber fallado, porque mi API no admite /hello/<num>
# assert response.status_code == 200


url = "http://127.0.0.1:8000/users/"

user_data = {
    "username": "jnjna"*20,
    "email": "juan@example.com"
}

response = requests.post(url, json=user_data)
print(f"Código de respuesta: {response.status_code}")
print(f"Respuesta: {response.json()}")
