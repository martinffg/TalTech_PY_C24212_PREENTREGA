import unittest
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para mostrar productos cuando no hay y cuando hay productos
class TestApp(unittest.TestCase):

    @patch('builtins.input', side_effect=["2", "3"])  # Simulamos la opción de mostrar productos y luego salir
    def test_mostrar_productos_sin_productos(self, mock_input):
        """Caso: No hay productos registrados"""
        app.productos = []  # Asegúrate de que la lista de productos sea accesible y vacía
        with patch('builtins.print') as mocked_print:
            app.main()
            mocked_print.assert_any_call("No hay productos registrados.")
            self.assertEqual(len(app.productos), 0, "Por defecto no debe haber productos")

    @patch('builtins.input', side_effect=["1", "Producto 1", "5", "2", "3"])  # Simulamos agregar un producto y luego mostrar productos
    def test_agregar_y_mostrar_productos(self, mock_input):
        """Caso: Se agrega un producto y se muestra"""
        app.productos = []  # Reiniciar la lista de productos
        with patch('builtins.print') as mocked_print:
            app.main()
            mocked_print.assert_any_call("Producto agregado con éxito.")
            self.assertEqual(len(app.productos), 1, "Debe haber 1 producto después de agregar")

if __name__ == '__main__':
    unittest.main()
