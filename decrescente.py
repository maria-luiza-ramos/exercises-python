import unittest


def decrescente(arr):
    # Faça um Programa que leia três números e mostre-os em ordem decrescente.
    arr.sort(reverse=True)
    return arr


class DecrescenteTest(unittest.TestCase):

    def test_decrescente(self):
        self.assertEquals(decrescente([3, 4, 1, 2, 8, 4]), [8, 4, 4, 3, 2, 1])

    def test_decrescente_2(self):
        self.assertEquals(decrescente([3, 1]), [3, 1])

    def test_decrescente_3(self):
        self.assertEquals(decrescente([1, -2, 3]), [3, 1, -2])


if __name__ == '__main__':
    numeros = []
    for n in range(3):
        num = int(input('Digite um número: '))
        numeros.append(num)
    print(decrescente(numeros))
