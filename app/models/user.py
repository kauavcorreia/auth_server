# Modelo para representar um usuário
from sqlalchemy import Column, Integer, String
from app.database.conection import Base
from passlib.context import CryptContext
from app.security.hashing import hash_senha


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)

   
# Sobrescreve o método de criação do usuário para hashear a senha
    def __init__(self, username: str, password: str, email: str):
        self.username = username.lower()
        self.password = hash_senha(password)
        self.email = email.lower()

# Sobrescreve o método de representação do usuário para não mostrar a senha
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

    

   





  