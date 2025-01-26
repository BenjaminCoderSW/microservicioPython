from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class ReparacionBase(BaseModel):
    descripcion: str
    fecha: str

class ReparacionCreate(ReparacionBase):
    auto_id: int

class Reparacion(ReparacionBase):
    id: int
    auto_id: int

    # Configuración para Pydantic v2
    model_config = ConfigDict(from_attributes=True)

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

    # Configuración para Pydantic v2
    model_config = ConfigDict(from_attributes=True)

class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    autos: List[Auto] = []

    # Configuración para Pydantic v2
    model_config = ConfigDict(from_attributes=True)
