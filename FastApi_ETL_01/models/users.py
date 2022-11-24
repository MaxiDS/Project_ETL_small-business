from sqlalchemy import Table, Column 
from sqlalchemy.types import DECIMAL, String, Date
from config.db import engine, meta 

users = Table("listaprecio",meta,
              Column("precio",DECIMAL(20,5)),
              Column("producto_id",String(30)),
              Column("sucursal_id",String(15)),
              Column("date",Date))

meta.create_all(engine)