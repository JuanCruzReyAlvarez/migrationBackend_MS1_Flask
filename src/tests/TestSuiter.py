import unittest
import os
import sys

def create_test_suite():
    start_dir = os.getcwd()
    suite = unittest.TestSuite()
    sys.path.append(os.path.abspath(os.path.join(start_dir, '..')))  # Agregar el directorio padre al sys.path
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.startswith('Test_') and file.endswith('.py'):
                module_name = file[:-3]  # Eliminar la extensión '.py'
                import_path = os.path.relpath(os.path.join(root, module_name)).replace(os.sep, '.')
                module = __import__(import_path, fromlist=[module_name])
                suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
    return suite

if __name__ == '__main__':
    suite = create_test_suite()
    unittest.TextTestRunner().run(suite)