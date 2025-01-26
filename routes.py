from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints crear clientes
@router.post("/clientes/", response_model=schemas.Cliente, tags=["Clientes"])
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, cliente)

# Obtener clientes
@router.get("/clientes/", response_model=List[schemas.Cliente], tags=["Clientes"])
def obtener_clientes(db: Session = Depends(get_db)):
    return crud.obtener_clientes(db)

# Obtener cliente por ID
@router.get("/clientes/{cliente_id}", response_model=schemas.Cliente, tags=["Clientes"])
def obtener_cliente_por_id(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.obtener_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Actualizar cliente
@router.put("/clientes/{cliente_id}", response_model=schemas.Cliente, tags=["Clientes"])
def actualizar_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    cliente_actualizado = crud.actualizar_cliente(db, cliente_id, cliente)
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado

# Eliminar cliente
@router.delete("/clientes/{cliente_id}", tags=["Clientes"])
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_eliminado = crud.eliminar_cliente(db, cliente_id)
    if not cliente_eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"message": "Cliente eliminado correctamente"}

# Endpoints para autos:
@router.post("/autos/", response_model=schemas.Auto, tags=["Autos"])
def crear_auto(auto: schemas.AutoCreate, db: Session = Depends(get_db)):
    return crud.crear_auto(db, auto)

# Obtener todos los autos
@router.get("/autos/", response_model=List[schemas.Auto], tags=["Autos"])
def obtener_autos(db: Session = Depends(get_db)):
    return crud.obtener_autos(db)

# Obtener un auto por ID
@router.get("/autos/{auto_id}", response_model=schemas.Auto, tags=["Autos"])
def obtener_auto_por_id(auto_id: int, db: Session = Depends(get_db)):
    auto = crud.obtener_auto_por_id(db, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto

# Actualizar un auto
@router.put("/autos/{auto_id}", response_model=schemas.Auto, tags=["Autos"])
def actualizar_auto(auto_id: int, auto: schemas.AutoCreate, db: Session = Depends(get_db)):
    auto_actualizado = crud.actualizar_auto(db, auto_id, auto)
    if not auto_actualizado:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto_actualizado

# Eliminar un auto
@router.delete("/autos/{auto_id}", tags=["Autos"])
def eliminar_auto(auto_id: int, db: Session = Depends(get_db)):
    auto_eliminado = crud.eliminar_auto(db, auto_id)
    if not auto_eliminado:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return {"message": "Auto eliminado correctamente"}

# Endpoints para reparaciones
@router.post("/reparaciones/", response_model=schemas.Reparacion, tags=["Reparaciones"])
def crear_reparacion(reparacion: schemas.ReparacionCreate, db: Session = Depends(get_db)):
    return crud.crear_reparacion(db, reparacion)

# Actualizar una reparación
@router.put("/reparaciones/{reparacion_id}", response_model=schemas.Reparacion, tags=["Reparaciones"])
def actualizar_reparacion(reparacion_id: int, reparacion: schemas.ReparacionCreate, db: Session = Depends(get_db)):
    reparacion_actualizada = crud.actualizar_reparacion(db, reparacion_id, reparacion)
    if not reparacion_actualizada:
        raise HTTPException(status_code=404, detail="Reparación no encontrada")
    return reparacion_actualizada

# Eliminar una reparación
@router.delete("/reparaciones/{reparacion_id}", tags=["Reparaciones"])
def eliminar_reparacion(reparacion_id: int, db: Session = Depends(get_db)):
    reparacion_eliminada = crud.eliminar_reparacion(db, reparacion_id)
    if not reparacion_eliminada:
        raise HTTPException(status_code=404, detail="Reparación no encontrada")
    return {"message": "Reparación eliminada correctamente"}

@router.get("/clientes/{cliente_id}/reparaciones", response_model=List[schemas.Reparacion], tags=["Clientes y Reparaciones"])
def obtener_reparaciones(cliente_id: int, db: Session = Depends(get_db)):
    return crud.obtener_reparaciones_cliente(db, cliente_id)
