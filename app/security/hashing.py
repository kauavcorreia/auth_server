import passlib
from passlib.context import CryptContext
import bcrypt 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
passlib.hash.bcrypt.using(rounds=12)

def hash_senha(password: str) -> str:
    return pwd_context.hash(password)

def verificar_senha(password: str, hash_senha: str) -> bool:
    return pwd_context.verify(password, hash_senha)


