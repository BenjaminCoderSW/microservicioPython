from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos SQLite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./taller_mecanico.db"

# URL de la base de datos SQLite en memoria
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# Motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Sesión de conexión a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos de las tablas
Base = declarative_base()
