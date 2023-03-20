import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


"""Nombre de la BD"""
sql_database = "../database.sqlite"

"""Nombre de la usta donde se encuentra la BD"""
base_dir = os.path.dirname(os.path.realpath(__file__))

"""La ruta de la base datos para que el sistema se enlace"""
database_url = f"sqlite:///{os.path.join(base_dir, sql_database)}"

"""Nuestro motor de base de datos sera """
engine = create_engine(database_url, echo=True)

"""Creamos la sesion para conectarnos a la base de datos"""
Session = sessionmaker(bind=engine)

"""Declarative_base sirve para manipular todas las tablas de la BD"""
Base = declarative_base()