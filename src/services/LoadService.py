from src.resource.db.DB import DB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKeyConstraint, PrimaryKeyConstraint
from flask import  jsonify
import pandas as pd


class LoadService():

    maxRowsTransaction = 1000

    @staticmethod
    def loadData(files,tablesInfo):

        LoadService.loadFK(tablesInfo)
        
        if files:
            
            db = DB()
            db.connect()
            engine = db.connect()
            
            try:
                with engine.connect() as conn:
                    with conn.begin():

                        iterableDictionary = dict(zip(files,tablesInfo))

                        for csv_file, tableInfo in iterableDictionary.items():
                            df = pd.read_csv(csv_file, names = tableInfo['columns'])
                            num_rows = len(df)

                            # Si el archivo tiene menos de 1000 filas, procesa todas las filas juntas
                            if num_rows <= LoadService.maxRowsTransaction:
                                chunk = df
                                print(chunk)
                                # Inserta los datos en la base de datos
                                if not chunk.empty:

                                    data = chunk[tableInfo['columns']]
                                    try:
                                        data.to_sql(tableInfo['table_name'], con=conn, if_exists='append', index=False)
                                        print("Datos insertados exitosamente en la tabla", tableInfo['table_name'])
                                    except Exception as e:
                                        print("Error al insertar datos en la tabla", tableInfo['table_name'], ":", e)

                            # Si el archivo tiene más de 1000 filas, procesa en lotes
                            else:
                                batch_size = LoadService.maxRowsTransaction  # Tamaño máximo del lote
                                print("MAS DE 1000")
                                num_batches = num_rows // batch_size + (1 if num_rows % batch_size > 0 else 0)  # Calculo el número de lote
                                print(num_batches)
                                for i in range(num_batches):
                                    start_idx = i * batch_size
                                    end_idx = min((i + 1) * batch_size, num_rows)
                                    chunk = df[start_idx:end_idx]
                                    print(chunk)
                                    # Inserta los datos en la base de datos
                                    if not chunk.empty:
                                        print(tableInfo['columns'])
                                        data = chunk[tableInfo['columns']]
                                        try:
                                            data.to_sql(tableInfo['table_name'], con=conn, if_exists='append', index=False)
                                            print("Datos insertados exitosamente en la tabla", tableInfo['table_name'])
                                        except Exception as e:
                                            print("Error al insertar datos en la tabla", tableInfo['table_name'], ":", e)
                                            
            except SQLAlchemyError as e:
                return jsonify({'error': 'Error de base de datos: {}'.format(str(e))}), 500
            finally:
                db.closeConnection(conn)
            return jsonify({'message': 'Data uploaded successfully'}), 200
        else:
            return jsonify({'error': 'No files provided'}), 400
        

    @staticmethod
    def loadFK(tablesInfo):

        if tablesInfo:   
            try:
                db = DB()
                db.connect()
                engine = db.connect()

                with engine.connect() as conn:
                    with conn.begin():

                        metadata = MetaData()

                        for table_data in tablesInfo:
                            table_name = table_data["table_name"]
                            # Creo una lista de columnas
                            columns = []
                            for col_name in table_data["columns"]:
                                    if col_name.startswith("id"):  # Si la columna comienza con 'id', la definimos como Integer
                                        columns.append(Column(col_name, Integer))
                                    else:
                                        columns.append(Column(col_name, String(255)))
                            table = Table(table_name, metadata, *columns)
                            table.append_constraint(PrimaryKeyConstraint("id"))
                            
                            # Definimos las claves foráneas si están presentes en el JSON
                            if "fk" in table_data:
                                for column_name, referenced_table in table_data["fk"].items():
                                    try:
                                        print(column_name, referenced_table)
                                        table.append_constraint(
                                            ForeignKeyConstraint([column_name], [f"{referenced_table}.id"]))
                                    except Exception as e:
                                            print("Error al crear FK", ":", e)
                        # Creo las tablas en la base de datos
                        try:
                            print("111111111111111111111111111111111111111")
                            metadata.create_all(engine)
                            print("222222222222222222222222222222222222222")
                            
                        except Exception as e:
                                            print("Error al crear las tablas", ":", e)

            except SQLAlchemyError as e:
                return jsonify({'error': 'Error de base de datos: {}'.format(str(e))}), 500
            finally:
                db.closeConnection(conn)
        else:
            return jsonify({'error': 'No files provided'}), 400


