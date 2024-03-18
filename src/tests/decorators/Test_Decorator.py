import unittest
from datetime import datetime
from src.decorator.DateTimeString import DateTimeString 

class Test_DateTimeString(unittest.TestCase):
    def test_process_bind_param_string(self):
        # Prueba de que process_bind_param convierte correctamente una cadena a objeto datetime
        datetime_string = "2022-03-20T12:00:00"
        expected_datetime = datetime.fromisoformat(datetime_string)
        converter = DateTimeString()
        result = converter.process_bind_param(datetime_string, None)
        self.assertEqual(result, expected_datetime)

    def test_process_bind_param_datetime(self):
        # Prueba de que process_bind_param no cambia un objeto datetime
        current_datetime = datetime.now()
        converter = DateTimeString()
        result = converter.process_bind_param(current_datetime, None)
        self.assertEqual(result, current_datetime)

    def test_process_bind_param_none(self):
        # Prueba de que process_bind_param no cambia None
        converter = DateTimeString()
        result = converter.process_bind_param(None, None)
        self.assertIsNone(result)