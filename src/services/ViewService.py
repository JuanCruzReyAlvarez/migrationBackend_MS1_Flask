
import pandas as pd
from sqlalchemy import create_engine
from src.resource.db.DB import DB
class ViewService():

    @staticmethod
    def viewEmployeesHiredWithRestriction2021():
        
        

        # Conexión a la base de datos
        db = DB()
        db.connect()
        engine = db.connect()  # SQLAlchemy engine

        # Consulta SQL para obtener los datos
        query = """
        SELECT e.*, d.department, j.job
        FROM employees e
        JOIN departments d ON e.id_department = d.id
        JOIN jobs j ON e.id_job = j.id
        WHERE YEAR(e.datetime) = 2021
        """

        # Leer datos desde la base de datos utilizando Pandas y la conexión de SQLAlchemy
        try:
            hired_employees = pd.read_sql(query, engine.connect())
            print("Datos extaidos correctamente")
        except Exception as e:
            print("Error al traer los datos: ", e)
        finally:
                db.closeConnection(engine)

        hired_employees = pd.read_sql(query, engine.connect())
        
        # Convertir la columna 'datetime' a formato de fecha

        # Agrupar por departamento, trabajo y trimestre y contar el número de empleados contratados
        hired_employees['quarter'] = hired_employees['datetime'].dt.quarter



        hired_employees_grouped = hired_employees.groupby(['department', 'job', 'quarter']).size().unstack(fill_value=0)

        print(33333333333)
        # Reordenar las columnas por trimestre
        hired_employees_grouped = hired_employees_grouped[[1, 2, 3, 4]].reset_index()

        hired_employees_grouped.columns = ['department', 'job', 'Q1', 'Q2', 'Q3', 'Q4']

        hired_employees_grouped = hired_employees_grouped.sort_values(by=['department', 'job'])


        # Mostrar la tabla resultante
        print(hired_employees_grouped)

        
        return hired_employees_grouped




    @staticmethod
    def viewEmployeesIdNameNumberWithRestriction2021():

        # Conexión a la base de datos
        db = DB()
        db.connect()
        engine = db.connect()  # SQLAlchemy engine

        # Consulta SQL para obtener los datos
        query = """
        SELECT d.id AS id_department, d.department, COUNT(e.id) AS hired
        FROM employees e
        JOIN departments d ON e.id_department = d.id
        WHERE YEAR(e.datetime) = 2021
        GROUP BY d.id, d.department
        HAVING COUNT(e.id) > (
            SELECT AVG(department_count.hired)
            FROM (
                SELECT COUNT(*) AS hired
                FROM employees
                WHERE YEAR(datetime) = 2021
                GROUP BY id_department
            ) AS department_count
        )
        ORDER BY hired DESC
        """

        # Leer datos desde la base de datos utilizando Pandas y la conexión de SQLAlchemy
        try:
            hired_employees = pd.read_sql(query, engine.connect())
            print("Datos extaidos correctamente")
        except Exception as e:
            print("Error al traer los datos: ", e)
        finally:
            db.closeConnection(engine)


        print(hired_employees)

        return hired_employees




