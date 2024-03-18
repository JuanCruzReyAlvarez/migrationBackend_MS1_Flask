from src.controller.ETLController import ETLController
from src.resource.db.DB import DB
import json
import unittest
from flask import  jsonify
from src import init_app
from config import config
from flask import Request


class TestExtraction(unittest.TestCase):

        def setUp(self):

            # Configura un contexto de aplicación antes de cada prueba

            configuration = config['development']

            app = init_app(configuration)

            self.app_context = app.app_context()

            self.app_context.push()

        def tearDown(self):

            # Limpia el contexto de la aplicación después de cada prueba

            self.app_context.pop()

        def test_extraction(self):

            ruta_archivo = 'src/tests/integration/jsonExtract.json'

            with open(ruta_archivo, 'r') as archivo:

                jsonReactMS = json.load(archivo)
            
                request = Request.from_values(json=jsonReactMS)

                data = request.get_json()

                try:
                     ETLController.extractData(data)
                except Exception as e:
                     self.fail(f"Se lanzó una excepción: {e}")


