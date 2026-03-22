# criar rota para criar usuário
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.conection import SessionLocal
from app.models import User
from pydantic import BaseModel

router = APIRouter()




