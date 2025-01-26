from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    autos = relationship("Auto", back_populates="propietario")

class Auto(Base):
    __tablename__ = "autos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    year = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    propietario = relationship("Cliente", back_populates="autos")
    reparaciones = relationship("Reparacion", back_populates="auto")

class Reparacion(Base):
    __tablename__ = "reparaciones"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    fecha = Column(String, index=True)
    auto_id = Column(Integer, ForeignKey("autos.id"))

    auto = relationship("Auto", back_populates="reparaciones")
