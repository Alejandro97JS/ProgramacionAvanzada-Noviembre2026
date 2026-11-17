# ORM ---> Object - Relational Mapper
input_username = input("LOGIN. Introduce tu username: ")
sql = f"SELECT * FROM USUARIOS WHERE USERNAME = {input_username}"
... # Sigue la lógica del login
# u1 = my_db.execute(sql)

# u2 = Usuarios.filter(username={input_username}).first()

# SQL Injection:
"SELECT * FROM USUARIOS WHERE USERNAME = el_rubius OR TRUE"
"SELECT * FROM USUARIOS"

from main import startup_completed

mi_resultado = startup_completed()
print(mi_resultado)
