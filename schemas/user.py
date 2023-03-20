from pydantic import BaseModel


# Para la creacion solicitar al usuario un: email y contraseña
class User(BaseModel):
    email: str
    password: str
