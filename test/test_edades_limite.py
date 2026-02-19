import unittest
# Cambia esto por el import correcto de tu función
from ED_Codigo_Testear import crear_usuario


class TestEdadesLimite(unittest.TestCase):

    def test_edad_valida_cero(self):
        usuario = crear_usuario("Ana", 0, "ana@gmail.com", "12345678A")
        self.assertIsNotNone(usuario)

    def test_edad_muy_grande(self):
        usuario = crear_usuario("Ana", 150, "ana@gmail.com", "12345678A")
        self.assertIsNotNone(usuario)   # según tu lógica actual

    def test_edad_none_invalida(self):
        usuario = crear_usuario("Ana", None, "ana@gmail.com", "12345678A")
        self.assertIsNone(usuario)      # o assertIsNotNone si tu lógica dice otra cosa