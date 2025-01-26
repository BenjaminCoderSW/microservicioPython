from pydantic import BaseModel
from typing import List, Optional

class ReparacionBase(BaseModel):
    descripcion: str
    fecha: str

class ReparacionCreate(ReparacionBase):
    auto_id: int

class Reparacion(ReparacionBase):
    id: int
    auto_id: int

    class Config:
        orm_mode = True

class AutoBase(BaseModel):
    marca: str
    modelo: str
    year: int

class AutoCreate(AutoBase):
    cliente_id: int

class Auto(AutoBase):
    id: int
    cliente_id: int
    reparaciones: List[Reparacion] = []

    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    autos: List[Auto] = []

    class Config:
        orm_mode = True
