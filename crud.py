from sqlalchemy.orm import Session
import models, schemas

# Crear un cliente
def crear_cliente(db: Session, cliente: schemas.ClienteCreate):
    nuevo_cliente = models.Cliente(nombre=cliente.nombre, email=cliente.email)
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

# Crear un auto
def crear_auto(db: Session, auto: schemas.AutoCreate):
    nuevo_auto = models.Auto(
        marca=auto.marca, modelo=auto.modelo, year=auto.year, cliente_id=auto.cliente_id
    )
    db.add(nuevo_auto)
    db.commit()
    db.refresh(nuevo_auto)
    return nuevo_auto

# Obtener todos los autos
def obtener_autos(db: Session):
    return db.query(models.Auto).all()

# Obtener un auto por ID
def obtener_auto_por_id(db: Session, auto_id: int):
    return db.query(models.Auto).filter(models.Auto.id == auto_id).first()

# Actualizar un auto
def actualizar_auto(db: Session, auto_id: int, auto_data: schemas.AutoCreate):
    auto = db.query(models.Auto).filter(models.Auto.id == auto_id).first()
    if auto:
        auto.marca = auto_data.marca
        auto.modelo = auto_data.modelo
        auto.year = auto_data.year
        auto.cliente_id = auto_data.cliente_id
        db.commit()
        db.refresh(auto)
        return auto
    return None

# Eliminar un auto
def eliminar_auto(db: Session, auto_id: int):
    auto = db.query(models.Auto).filter(models.Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
        return auto
    return None

# Crear una reparación
def crear_reparacion(db: Session, reparacion: schemas.ReparacionCreate):
    nueva_reparacion = models.Reparacion(
        descripcion=reparacion.descripcion, fecha=reparacion.fecha, auto_id=reparacion.auto_id
    )
    db.add(nueva_reparacion)
    db.commit()
    db.refresh(nueva_reparacion)
    return nueva_reparacion

# Actualizar una reparación
def actualizar_reparacion(db: Session, reparacion_id: int, reparacion_data: schemas.ReparacionCreate):
    reparacion = db.query(models.Reparacion).filter(models.Reparacion.id == reparacion_id).first()
    if reparacion:
        reparacion.descripcion = reparacion_data.descripcion
        reparacion.fecha = reparacion_data.fecha
        reparacion.auto_id = reparacion_data.auto_id
        db.commit()
        db.refresh(reparacion)
        return reparacion
    return None

# Eliminar una reparación
def eliminar_reparacion(db: Session, reparacion_id: int):
    reparacion = db.query(models.Reparacion).filter(models.Reparacion.id == reparacion_id).first()
    if reparacion:
        db.delete(reparacion)
        db.commit()
        return reparacion
    return None

# Obtener todas las reparaciones de un cliente
def obtener_reparaciones_cliente(db: Session, cliente_id: int):
    return db.query(models.Reparacion).join(models.Auto).filter(models.Auto.cliente_id == cliente_id).all()

# Obtener todos los clientes
def obtener_clientes(db: Session):
    return db.query(models.Cliente).all()

# Obtener cliente por ID
def obtener_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

# Actualizar un cliente
def actualizar_cliente(db: Session, cliente_id: int, cliente_data: schemas.ClienteCreate):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if cliente:
        cliente.nombre = cliente_data.nombre
        cliente.email = cliente_data.email
        db.commit()
        db.refresh(cliente)
        return cliente
    return None

# Eliminar un cliente
def eliminar_cliente(db: Session, cliente_id: int):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
        return cliente
    return None
