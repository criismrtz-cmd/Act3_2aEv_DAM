import unittest
from registro_usuario import validar_email


class TestValidarEmail(unittest.TestCase):

    def test_email_valido(self):
        self.assertTrue(validar_email("ana@gmail.com"))

    def test_email_sin_arroba_invalido(self):
        self.assertFalse(validar_email("anagmail.com"))

    def test_email_empieza_con_arroba_invalido(self):
        self.assertFalse(validar_email("@ana@gmail.com"))


if __name__ == "__main__":
    unittest.main()