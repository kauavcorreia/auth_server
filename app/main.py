from fastapi import FastAPI

app = FastAPI()



# importar rotas
from app.routes import users, auth
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


