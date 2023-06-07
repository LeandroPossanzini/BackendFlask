from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:telecom2023@database-lightsail.c0kapvnmfb70.us-east-1.rds.amazonaws.com:5432/agenda'


def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion a base de datos ok")
    else:
        print("Error en la conexion de la base de datos")

    return s

