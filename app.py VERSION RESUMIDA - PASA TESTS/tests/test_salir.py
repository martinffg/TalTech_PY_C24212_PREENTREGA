import unittest
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

class TestApp(unittest.TestCase):

    @patch('builtins.input', side_effect=["3"])  # Simulate choosing the option to exit
    def test_salir(self, mock_input):
        app.main()  # Call the main function
        assert True  # Verificamos que el programa termina sin errores
        
if __name__ == '__main__':
    unittest.main()
