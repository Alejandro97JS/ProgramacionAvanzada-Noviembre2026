# SOLID Principles

# D - Dependency inversion (difícil según es Python?)

# OPCIÓN MALA:

class EmailSender:

    def __init__(self):
        pass

    def send_email(self, input_msg):
        # Conectarnos a un servidor de envío de correos...
        # Redactar el mensaje:
        if not input_msg:
            msg = "Aviso desde la aplicación Pontia"
        else:
            msg = input_msg
        # Enviar el email.


class Notificator:
    def __init__(self):
        self.channel = EmailSender()

    def check_if_send_notification(self, username):
        return username == "Pepe"

    def notificate(self):
        self.channel.send_email("Prueba Clase 2")

# OPCIÓN BUENA:
from abc import ABC, abstractmethod

class ChannelNotificationSender(ABC):

    @abstractmethod
    def send_notification(self, input_msg):
        pass

class EmailSender(ChannelNotificationSender):

    def __init__(self):
        pass

    def send_notification(self, input_msg):
        # Conectarnos a un servidor de envío de correos...
        # Redactar el mensaje:
        if not input_msg:
            msg = "Aviso desde la aplicación Pontia"
        else:
            msg = input_msg
        # Enviar el email.

class SMSSender(ChannelNotificationSender):

    def __init__(self):
            pass
    
    def send_notification(self, input_msg):
        # Conectarnos a nuestro proveedor de línea.
        # Redactar el mensaje.
        if not input_msg:
            msg = "Aviso desde la aplicación Pontia"
        else:
            msg = input_msg
        # CUIDADO!! Es un SMS, no conviene que sea largo.
        if len(msg) > 200:
            msg = msg[:200] + "..."


class Notificator:
    def __init__(self, channel_sender:ChannelNotificationSender):
        self.channel = channel_sender

    def check_if_send_notification(self, username):
        return username == "Pepe"

    def notificate(self, username):
        self.channel.send_notification("Prueba Clase 2")

channel_sender = SMSSender()
my_notificator = Notificator(channel_sender)
my_notificator.notificate("Hola"*30)

# Patrón Factory

class ChannelFactory:
    def __init__(self):
        pass

    def create_channel(self, username):
        if username == "PEPE":
            return SMSSender()
        else:
            return EmailSender()

# username = "PEPE"
# channel_sender = ChannelFactory().create_channel(username)
# my_notificator = Notificator(channel_sender)
# my_notificator.notificate("Hola"*30)


# === PROGRAMACIÓN WEB ===

import requests
# response = requests.get("https://es.wikipedia.org/")
# print(response.json())
# FALLA PORQUE ESTÁ PENSADO PARA WEB (NAVEGADOR) Y SOMOS UN "BOT"

# response = requests.get("https://catfact.ninja" + "/fact_asdfasdfas")
# print(response.text)
# print(response.ok)
# print(response.status_code)

num_frases = int(input("Introduce num frases gatos"))
max_length = int(input("Introduce longitud máxima"))
my_built_url = "https://catfact.ninja" + "/facts" + f"?max_length={max_length}&limit={num_frases}"
print(my_built_url)
my_response = requests.get(my_built_url)
# print(my_response.text)
for elem in my_response.json()["data"]:
    print(f"--> {elem['fact']}")
