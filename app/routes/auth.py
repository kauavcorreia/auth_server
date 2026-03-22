from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conection import SessionLocal
from app.models import User
from app.security.hashing import verificar_senha
from pydantic import BaseModel
from pydantic import EmailStr
from passlib.context import CryptContext
from app.security import gerar_token, verificar_token
import jwt



router = APIRouter()
 
class criar_usuario(BaseModel):
    username: str
    password: str
    email: EmailStr

# cria usuário e salva no banco de dados e gera hash da senha
@router.post("/register/")
def criar_usuario(user: criar_usuario, db: Session = Depends(SessionLocal)):

    hashed_password = hash_senha(user.password)
    db_user = User(username=user.username, password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def hash_senha(password: str) -> str:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)


@router.post("/login/")
def verificar_login(username: str, password: str, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.username == username).first()

    if db_user is None:
        return {"error": "Usuário não encontrado"}
    
    if not verificar_senha(password, db_user.password):
        return {"error": "Senha incorreta"}
    
    else:
        jwt_token = gerar_token(db_user.username)
        return {"message": "Login bem-sucedido", "token": jwt_token}
    
@router.post("/logout/")
# encerrar sessão do usuário, invalidando o token JWT
def encerrar_sessao(jwt_token: str, db: Session = Depends(SessionLocal)):
    
    
   
   


        











   


    
