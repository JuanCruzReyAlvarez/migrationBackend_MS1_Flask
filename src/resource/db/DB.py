import mysql.connector
import os

class DB():

    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DB")
        self.conexion = None

    def connect(self):
        try:
            conexion = mysql.connector.connect(
                host = self.host,
                user= self.user,
                password = self.password,
                database = self.database
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                self.conexion = conexion
                return conexion
            else:
                print("No se pudo conectar a la base de datos")
                exit()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: ", error)
            exit()
        
    def closeConnection(self):
        if 'conexion' in locals() and self.conexion.is_connected():
            self.conexion.close()
        print("Conexión a Base de Datos cerrada con exito")
    