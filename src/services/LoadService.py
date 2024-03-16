from src.resource.db.DB import DB
from sqlalchemy.exc import SQLAlchemyError
from flask import  jsonify
import pandas as pd


class LoadService():

    maxRowsTransaction = 1000

    @staticmethod
    def loadData(self,files,tablesInfo):

        if files:


            db = DB()
            db.connect()
            try:
                with db.engine.connect() as con:
                    with con.begin():

                        iterableDictionary = dict(zip(files,tablesInfo))

                        for csv_file, tableInfo in iterableDictionary.items():
                            df = pd.read_csv(csv_file)
                            num_rows = len(df)
                            # Si el archivo tiene menos de 1000 filas, procesa todas las filas juntas
                            if num_rows <= LoadService.maxRowsTransaction:
                                chunk = df
                                # Inserta los datos en la base de datos
                                if not chunk.empty:

                                    data = chunk[[column['name'] for column in tableInfo['columns']]]
                                    data.to_sql(tableInfo['table_name'], con=con, if_exists='append', index=False)

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
                                       data.to_sql(tableInfo['table_name'], con=con, if_exists='append', index=False)
            except SQLAlchemyError as e:
                return jsonify({'error': 'Error de base de datos: {}'.format(str(e))}), 500
            finally:
                db.close()
            return jsonify({'message': 'Data uploaded successfully'}), 200
        else:
            return jsonify({'error': 'No files provided'}), 400


