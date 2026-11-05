# Python básico
categories = [
    {"name": "Electronics", "description": "Devices and gadgets"},
    {"name": "Office", "description": "Office supplies and equipment"},
    3
]

for x in categories:
    if type(x)==dict and "name" in x and "description" in x:
        print(f"Categoría {x['name']} trata de: {x['description']}") # f-string
        # Python admite tanto "" como ''

class GoogleCaidoException(Exception):
    def __str__(self):
        pass

try:
    respuesta_de_google = 1
    raise GoogleCaidoException()
    # {"success": "True"}
    print(f"Google me ha respondido: {respuesta_de_google['success']}")
except ZeroDivisionError as e:
    print(e)
    print("Division por cero")
except GoogleCaidoException as e2:
    pass

print("Bye!")

# Métodos dunder --> Double UNDERscore

a = {}
a["37"] = "Hola"
print(a)
a["99"]="Adios"
print(a)

# List comprehensions / Dictionary comprehensions:
b = []
for i in [1,2,3,4]:
    b.append(2*i)
print(b)

b = [2*i for i in [1,2,3,4]]
print(b)

# duplicate = lambda x_list: [2*i for i in x_list]
# c = duplicate([23,44])
# print(c)

my_set = {2*x for x in [5,6,7]}
my_set
# set()


ejemplo = {
    "a": 1,
    "b": 2
}
for juan, mi_valor in ejemplo.items():
    print(juan)
    print(mi_valor)
