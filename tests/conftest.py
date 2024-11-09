import sys
import os

# Añadir el directorio raíz del proyecto al sys.path para que todos los tests lo encuentren
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
