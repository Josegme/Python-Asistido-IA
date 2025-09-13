import unittest
from funciones import division


# Importar la función si está en otro archivo, por ejemplo:
# from mi_modulo import division

def division(numero1, numero2):
    """
    Realiza la división de dos números con validaciones.
    """
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Los valores deben ser números (int o float)")
    if numero2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return numero1 / numero2


class TestDivision(unittest.TestCase):

    def test_division_positivos(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_decimales(self):
        self.assertAlmostEqual(division(7.5, 2.5), 3.0)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            division("10", 2)

    def test_division_negativos(self):
        self.assertEqual(division(-10, -2), 5)
        self.assertEqual(division(-10, 2), -5)


if __name__ == "__main__":
    unittest.main()
