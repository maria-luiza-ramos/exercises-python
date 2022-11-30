# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
import unittest


def genero(s: str) -> str:
    """
    :param s: uma string contendo o valor 'F' ou 'M'
    :return: Retorna uma string para a letra informada, caso não seja um dos valores definidos retorna 'outro'
    """
    s = s.upper()[0]
    if s == 'F':
        return 'Feminino'
    if s == 'M':
        return 'Masculino'
    return 'Outro'


class GeneroTest(unittest.TestCase):

    def test_feminino(self):
        self.assertEquals(genero("f"), "Feminino", "Deveria ter retornado Feminino")

    def test_feminino_maiusculo(self):
        self.assertEquals(genero("F"), "Feminino",  "Deveria ter retornado Feminino")

    def test_masculino(self):
        self.assertEquals(genero("m"), "Masculino",  "Deveria ter retornado Masculino")

    def test_masculino_maiusculo(self):
        self.assertEquals(genero("M"), "Masculino",  "Deveria ter retornado Masculino")
    def test_outro(self):
        self.assertEquals(genero("G"), "Outro",  "Deveria ter retornado Outro")


if __name__ == '__main__':
    sexo = str(input('Digite o sexo: '))
    print(genero(sexo))
