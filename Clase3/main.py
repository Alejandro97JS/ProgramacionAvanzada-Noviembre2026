import logging
from utils import mensaje_bienvenida
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str = Field(..., min_length=3, description="Nombre de usuario (mínimo 3 caracteres)")
    email: str = Field(..., description="Email del usuario")
    age: Optional[int] = Field(None, ge=0, description="Edad no negativa (opcional)")

    @field_validator("username")
    def username_with_vowels(cls, value):
        # encontrado = False
        # for vowel in ["a", "e", "i", "o", "u"]:
        #     if vowel in value:
        #         encontrado=True
        # if not encontrado:
        #     raise ValueError("You need vowels in your username!")
        if not any(vowel in value for vowel in 
                   ["a", "e", "i", "o", "u"]):
            raise ValueError("You need vowels in your username!")
        return value

    @model_validator(mode="after")
    def long_username_if_age_ge_50(cls, instance):
        if instance.age is None or instance.age >= 50:
            if len(instance.username) < 20:
                raise ValueError("You must provide a username longer than 20 chars")
        return instance

logging.basicConfig(
    level=logging.WARNING,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Mi primera API con FastAPI",
    description="Una API de ejemplo.",
    version="1.0.0"
)

@app.get("/")
def startup_completed():
    return mensaje_bienvenida()

@app.get("/hello")
def initial_greeting():
    logger.debug("Buenas!!")
    logger.info("Recibida petición al saludo genérico")
    return {"msg": "Hola mundo!!!"}

@app.get("/hello/{name}")
def custom_greeting(name:str):
    try:
        int(name)
        logger.warning("Alguien puso un número")
        return HTMLResponse("Mal...", 400)
    except:
        logger.info(f"Recibida petición al saludo personalizado para {name}")
        processed_name = name.capitalize()
        logger.info(f"Nombre tras .capitalize(): {processed_name}")
        if processed_name == "Pepe":
            logger.warning("Pepe ha entrado a la web!!")
        return {"msg": f"Hello, {processed_name}!!!"}

@app.post("/users/")
def create_user(user: User):
    logger.info(f"📥 Registro de usuario recibido: {user}")
    ... # Registrarlo en DB...
    return {
        "msg": "Usuario registrado correctamente",
        "usuario": user
    }

# Front de registro: sirve un HTML con un formulario cuyo JavaScript
# llama a la propia API (POST /users/ -> create_user)
REGISTER_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de usuarios</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; display: flex; justify-content: center; padding: 40px 16px; }
        .card { background: white; padding: 24px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); width: 100%; max-width: 380px; }
        h1 { margin-top: 0; font-size: 1.4em; }
        label { display: block; margin-top: 12px; font-weight: bold; }
        input { width: 100%; padding: 8px; margin-top: 4px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { margin-top: 20px; width: 100%; padding: 10px; background: #009688; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 1em; }
        button:hover { background: #00796b; }
        #resultado { margin-top: 16px; padding: 10px; border-radius: 4px; display: none; white-space: pre-wrap; }
        .ok { background: #e0f2f1; color: #00695c; }
        .error { background: #ffebee; color: #c62828; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Registro de usuarios</h1>
        <form id="form-registro">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required minlength="3">

            <label for="age">Edad (opcional)</label>
            <input type="number" id="age" name="age" min="0">

            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>

            <button type="submit">Registrar</button>
        </form>
        <div id="resultado"></div>
    </div>

    <script>
        const form = document.getElementById("form-registro");
        const resultado = document.getElementById("resultado");

        function mostrar(texto, clase) {
            resultado.textContent = texto;
            resultado.className = clase;
            resultado.style.display = "block";
        }

        form.addEventListener("submit", async (event) => {
            event.preventDefault();  // Evita que el formulario recargue la página

            const ageValue = document.getElementById("age").value;
            const payload = {
                username: document.getElementById("username").value,
                email: document.getElementById("email").value,
                age: ageValue === "" ? null : parseInt(ageValue, 10)
            };

            try {
                // Llamada a la propia API: endpoint create_user
                const response = await fetch("/users/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();

                if (response.ok) {
                    mostrar(data.msg + "\\n" + JSON.stringify(data.usuario, null, 2), "ok");
                    form.reset();
                } else if (response.status === 422) {
                    // Errores de validación de Pydantic
                    const errores = data.detail.map(e => "• " + e.msg).join("\\n");
                    mostrar("Errores de validación:\\n" + errores, "error");
                } else {
                    mostrar("Error " + response.status + ": " + JSON.stringify(data), "error");
                }
            } catch (err) {
                mostrar("No se pudo contactar con la API: " + err, "error");
            }
        });
    </script>
</body>
</html>
"""

@app.get("/register", response_class=HTMLResponse)
def register_form():
    logger.info("Sirviendo formulario de registro")
    return REGISTER_HTML
