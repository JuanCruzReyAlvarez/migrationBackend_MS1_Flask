from flask import  jsonify
from src.services.ViewService import ViewService

class ViewController():

    @staticmethod
    def viewEmployeesHiredWithRestriction():    ## Esta vista corresponde una query que solicita: Number of employees hired for each job and department in 2021 divided by quarter. 
                                                    ##Thetable must be ordered alphabetically by department and job.
            try:
                
                ## Ejecuto y consigo la vista
                hired_employees = ViewService.viewEmployeesHiredWithRestriction2021()

                file = hired_employees.to_csv(index=False)

                # Devolver los datos como JSON con código de respuesta 202
                return jsonify({
                    'status': 'success',
                    'data': file
                }), 202

            except Exception as e:

            # En caso de error:
            
                error_message = f"Error durante el acceso a la vista: {str(e)}"
                response = jsonify({'message': error_message})
                response.status_code = 500  # Código de estado HTTP 500 - Internal Server Error
                return response


    @staticmethod
    def viewEmployeesIdNameNumberWithRestriction2021():     ## List of ids, name and number of employees hired of each department that hired more
                                                            ## employees than the mean of employees hired in 2021 for all the departments, ordered
                                                            ## by the number of employees hired (descending).
            try:
                
                ## Ejecuto y consigo la vista
                hired_employees = ViewService.viewEmployeesIdNameNumberWithRestriction2021()

                file = hired_employees.to_csv(index=False)

                # Devolver los datos como JSON con código de respuesta 202
                return jsonify({
                    'status': 'success',
                    'data': file
                }), 202

            except Exception as e:

            # En caso de error:
            
                error_message = f"Error durante el acceso a la vista: {str(e)}"
                response = jsonify({'message': error_message})
                response.status_code = 500  # Código de estado HTTP 500 - Internal Server Error
                return response