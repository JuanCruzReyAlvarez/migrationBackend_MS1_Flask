from src.resource.db.DB import DB
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from flask import  jsonify
import pandas as pd


class LoadService():

    maxRowsTransaction = 1000

    @staticmethod
    def loadData(files,tablesInfo):

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


