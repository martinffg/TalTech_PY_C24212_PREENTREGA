import unittest
import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch


class TestApp(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "Manzana", "10", "3"])
    def test_agregar_producto(self, mock_input):
        app.main()

        with self.subTest("Verificando cantidad de productos"):
            self.assertEqual(
                len(app.productos),
                1,
                "Debería haber exactamente 1 producto después de agregar.",
            )

        with self.subTest("Verificando contenido del producto agregado"):
            self.assertEqual(
                app.productos[0],
                ["Manzana", 10],
                "El producto agregado debería ser 'Manzana' con cantidad 10.",
            )


if __name__ == "__main__":
    unittest.main()
