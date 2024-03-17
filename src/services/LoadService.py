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
                                        data.to_sql(tableInfo['table_name'], con=conn, if_exists='replace', index=False)
                                        print("Datos insertados exitosamente en la tabla", tableInfo['table_name'])
                                    except Exception as e:
                                        print("Error al insertar datos en la tabla", tableInfo['table_name'], ":", e)
                                    print(888888)

                            # Si el archivo tiene más de 1000 filas, procesa en lotes
                            else:
                                batch_size = 1000  # Tamaño máximo del lote
                                num_batches = num_rows // batch_size + (1 if num_rows % batch_size > 0 else 0)  # Calcula el número de lotes
                                for i in range(num_batches):
                                    start_idx = i * batch_size
                                    end_idx = min((i + 1) * batch_size, num_rows)
                                    chunk = df[start_idx:end_idx]
                                    # Inserta los datos en la base de datos
                                    if not chunk.empty:
                                       data = chunk[[column['name'] for column in tableInfo['columns']]]
                                       data.to_sql(tableInfo['table_name'], con=conn, if_exists='append', index=False)
            except SQLAlchemyError as e:
                return jsonify({'error': 'Error de base de datos: {}'.format(str(e))}), 500
            finally:
                db.closeConnection(conn)
            return jsonify({'message': 'Data uploaded successfully'}), 200
        else:
            return jsonify({'error': 'No files provided'}), 400


