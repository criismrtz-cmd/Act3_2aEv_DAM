import unittest
from registro_usuario import crear_usuario

class TestRegistroUsuario(unittest.TestCase):

    def test_crear_usuario_valido(self):
        usuario = crear_usuario("Ana", 25, "ana@gmail.com", "12345678A")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nombre"], "Ana")
        self.assertEqual(usuario["edad"], 25)

    def test_crear_usuario_invalido(self):
        self.assertIsNone(crear_usuario("", 25, "ana@gmail.com", "12345678A"))
        self.assertIsNone(crear_usuario("Ana", -5, "ana@gmail.com", "12345678A"))
        self.assertIsNone(crear_usuario("Ana", 25, "anagmail.com", "12345678A"))
        self.assertIsNone(crear_usuario("Ana", 25, "ana@gmail.com", "1234"))

    def test_edades_masivas(self):
        for i in range(0, 100):
            usuario = crear_usuario("Ana", i, "ana@gmail.com", "12345678A")
            self.assertIsNotNone(usuario)

if __name__ == '__main__':
    unittest.main()
