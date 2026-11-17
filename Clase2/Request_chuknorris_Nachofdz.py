# Ejercicio de repaso, consulta apis externas.
import requests

BASE_URL = "https://api.chucknorris.io"
CATEGORIAS_URL = BASE_URL + "/jokes/categories"
RANDOM_URL = BASE_URL + "/jokes/random"
SEARCH_URL = BASE_URL + "/jokes/search"

# Carga la lista de categorias, se construye como 
def get_categorias() -> list:
    """Cargar las categorías de los chistes y definir donde metemos los datos"""
    response = requests.get(CATEGORIAS_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data

# toma el chiste 
def get_chiste(categoria: str) -> str:
    response = requests.get(RANDOM_URL, params={"category": categoria}, timeout=5) # al final del random la consulta ira con ?category: xxxx
    response.raise_for_status()
    chiste = response.json()
    print(response.url) # para controlar como se ha construido la url
    return chiste["value"]

# Guardo la categoría
categorias = get_categorias()

#recorremos la lista y e imprimir las categorías, quita 1 por que empieza en 0
for indice, valor in enumerate(categorias,start=1): 
        print(f"{indice}. {valor}")   


# pedir por pantalla la categoria
cat_elegida = input("Selecciona el nombre de una categoria: ")

# controlamos si la categoría esta en la lista e imprimir
if cat_elegida in categorias:
    print(get_chiste(cat_elegida))
else:
    print("Esa categoría no existe")
    

