
from src.services.ExtractService import ExtractService
## from src.services.TransformService import TransformService
from src.services.LoadService import LoadService
from flask import  jsonify


class ETLController():

    @staticmethod
    def extractData(json):
            try:
                
                ## 1° -> Extract
                data =  ExtractService.extractData(json) 
                files = data[0] 
                tablesInfo = data[1]

                ## 2° -> Transform
                ## filesTransformed = TransformService.transformData(files)  // -> No need in this project, it is prepared if it´s necessary 

                ## 3° -> Load
                LoadService.loadData(files, tablesInfo)  ## batch transactions (1 up to 1000 rows) with one request
            


                ## En caso de exito: 
                response = jsonify({'message': 'La migración de datos ha sido completada exitosamente.'})
                response.status_code = 202  # Código de estado HTTP 202 - Accepted
                return response
            except Exception as e:

            # En caso de error:
            
                error_message = f"Error durante la migración de datos: {str(e)}"
                response = jsonify({'message': error_message})
                response.status_code = 500  # Código de estado HTTP 500 - Internal Server Error
                return response