#Modularizar o dividir nuestros routers
from fastapi import APIRouter
from schemas.user_schemas import Precio
from config.db import engine
from typing import List
from models.users import users


user = APIRouter()

@user.get("/")
def Rutaas():
    return "hello world"


@user.get("/api/listaprecios/{id}", response_model = List[Precio])
def ListaPrecios(id:str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.producto_id == {id})).fetchall()
        
        return result
        