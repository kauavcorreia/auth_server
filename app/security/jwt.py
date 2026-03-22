# Configurações para JWT
from pydantic import BaseSettings   
from datetime import datetime, timedelta
import jwt

class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int = 5

settings = Settings()

def gerar_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.jwt_access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        return payload
    
    except jwt.ExpiredSignatureError:

        raise Exception("Token expirado")
    
    except jwt.InvalidTokenError:

        raise Exception("Token inválido")
    
