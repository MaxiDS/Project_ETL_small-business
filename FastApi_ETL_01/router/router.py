#Modularizar o dividir nuestros routers
from fastapi import APIRouter
from schemas.user_schemas import Precio
from config.db import engine
from typing import List
from models.users import users
from fastapi import File, UploadFile

#ETL:
import pandas as pd
import datetime

user = APIRouter()

@user.get("/api/listaprecios/{id}", response_model = List[Precio],tags=["Precios"])
async def Lista_Precios(id:str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.producto_id == {id})).fetchall()
        
        return result
        

@user.post("/file/", tags=["Precios"])
async def Cargar_archivo(file: UploadFile= File(...)):
    with engine.connect() as conn:
        name = file.filename.split(".")[0]
        name = name[-8:]
        dataText = pd.read_csv(file.file, sep="|", decimal=".",)

        dataText["date"]= name[-8:-4]+"-"+name[-4:-2]+"-"+name[-2:]

        dataText['producto_id'] = dataText['producto_id'].fillna(int(0)).apply(lambda x: str(int(float(x))).zfill(13))
        dataText['sucursal_id'] = dataText['sucursal_id'].apply(lambda x: ('{0}-{1}-{2}'.format(int(x.day),int(x.month),int(x.year))) if(type(x) == datetime.datetime) else x)
        dataText['sucursal_id'] = dataText['sucursal_id'].apply(lambda x: str(x))
        
        dataText.to_sql(con=conn, name='listaprecio',if_exists='append', index=False)

        return {"Archivo cargado correctamente:",file.filename}
