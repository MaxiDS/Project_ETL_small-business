from pydantic import BaseModel
from datetime import date

class Precio(BaseModel):
    precio: float
    producto_id: str
    sucursal_id: str
    date: date
    
