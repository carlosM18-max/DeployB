from fastapi import FastAPI
from routes.persons import person
from routes.users import user
from routes.roles import rol
from routes.users_roles import users_roles

app = FastAPI()  # variable app
app.include_router(person)  # Luego agrega las rutas
# app.include_router(user)
app.include_router(user)
app.include_router(rol)
app.include_router(users_roles)

print("Bienvenido al servidor uvicorn")