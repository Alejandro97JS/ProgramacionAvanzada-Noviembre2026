import requests

URL_BASE = "http://127.0.0.1:8000"

url_user = URL_BASE + "/users"


user_data = {
    "username": "Juan",
    "email": "bc@example.com",
    "age": 20
}

url_order = URL_BASE + "/orders"



# response = requests.post(url_user, json=user_data)
# print(f"Código de respuesta: {response.status_code}")
# guardar = response.json()
# import json
# with open("./prueba.json", encoding="utf-8", mode="w") as file_out:
#     json.dump(guardar, file_out)


order_data = {
    "user_id": 1,
    "product": "Pizza",
    "quantity": 1,
    "price": 5
}
# response = requests.post(url_order, json=order_data)
# print(f"Código de respuesta: {response.status_code}")
# guardar = response.json()
# import json
# with open("./prueba.json", encoding="utf-8", mode="w") as file_out:
#     json.dump(guardar, file_out)


orders_of_user_response = requests.get(URL_BASE + "/users/1/orders")
print(orders_of_user_response.status_code)
print(orders_of_user_response.json())
