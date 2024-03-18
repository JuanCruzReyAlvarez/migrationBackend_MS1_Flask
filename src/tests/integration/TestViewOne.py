from src.controller.ViewController import ViewController
import unittest
from flask import  jsonify
from src import init_app
from config import config



class TestViewOne(unittest.TestCase):

        def setUp(self):

            # Configura un contexto de aplicación antes de cada prueba

            configuration = config['development']

            app = init_app(configuration)

            self.app_context = app.app_context()

            self.app_context.push()

        def tearDown(self):

            # Limpia el contexto de la aplicación después de cada prueba

            self.app_context.pop()

        def test_viewOne(self):

                try:
                     ViewController.viewEmployeesHiredWithRestriction()

                except Exception as e:

                     self.fail(f"Se lanzó una excepción: {e}")