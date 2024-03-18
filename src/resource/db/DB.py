import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class DB():

    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = os.getenv("MYSQL_PORT")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DB")

    def getURI(self):
        return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
    def connect(self):
        try:
            self.engine = create_engine(self.getURI())
            print("Conexión exitosa a la base de datos")
            return self.engine

        except SQLAlchemyError as e:
            print("Error al conectar a la base de datos:", e)
            exit()
        
    def closeConnection(self, con):
        if self.engine is not None:
            self.engine.dispose()
            print("Conexión a la base de datos cerrada con éxito")
    