
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
        Select  d.department, j.job, 
        SUM(CASE WHEN QUARTER(datetime) = 1 THEN 1 ELSE 0 END) Q1,
        SUM(CASE WHEN QUARTER(datetime) = 2 THEN 1 ELSE 0 END) Q2,
        SUM(CASE WHEN QUARTER(datetime) = 3 THEN 1 ELSE 0 END) Q3,
        SUM(CASE WHEN QUARTER(datetime) = 4 THEN 1 ELSE 0 END) Q4
        from employees e INNER JOIN jobs j ON ( e.id_job = j.id ) INNER JOIN departments d ON ( e.id_department = d.id )
        Where Year(datetime) = 2021 
        Group By id_job, id_department
        order by d.department, j.job
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


        # Mostrar la tabla resultante
        print(hired_employees)

        
        return hired_employees




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






## Otra forma de realizar las consultas es utilizando pandas y realizando logica con dicha biblioteca:

## Por ejemplo en la primer vista podemos hacer:

#  query = """
#         SELECT e.*, d.department, j.job
#         FROM employees e
#         INNER JOIN departments d ON e.id_department = d.id
#         INNER JOIN jobs j ON e.id_job = j.id
#         WHERE YEAR(e.datetime) = 2021
#         """

#         # Leer datos desde la base de datos utilizando Pandas y la conexión de SQLAlchemy
#         try:
#             hired_employees = pd.read_sql(query, engine.connect())
#             print("Datos extaidos correctamente")
#         except Exception as e:
#             print("Error al traer los datos: ", e)
#         finally:
#                 db.closeConnection(engine)

#         hired_employees = pd.read_sql(query, engine.connect())
        
#         # Convertir la columna 'datetime' a formato de fecha

#         # Agrupar por departamento, trabajo y trimestre y contar el número de empleados contratados
#         hired_employees['quarter'] = hired_employees['datetime'].dt.quarter



#         hired_employees_grouped = hired_employees.groupby(['department', 'job', 'quarter']).size().unstack(fill_value=0)

#         # Reordenar las columnas por trimestre
#         hired_employees_grouped = hired_employees_grouped[[1, 2, 3, 4]].reset_index()

#         hired_employees_grouped.columns = ['department', 'job', 'Q1', 'Q2', 'Q3', 'Q4']

#         hired_employees_grouped = hired_employees_grouped.sort_values(by=['department', 'job'])


#         # Mostrar la tabla resultante
#         print(hired_employees_grouped)

        
#         return hired_employees_grouped