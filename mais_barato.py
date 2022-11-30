import unittest
from unittest.mock import patch


def get_value_to_compair(key_value):  # ["banana", 12.50]
    return key_value[1]


def mais_barato(input_t):
    # Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    # sabendo que a decisão é sempre pelo mais barato.

    produtos = {}
    for p in range(3):
        produto = str(input_t('Qual o nome do produto? '))
        valor = float(input_t(f'Qual o valor do {produto}? '))
        produtos[produto] = valor
    items = produtos.items()  # [["banana", 12.50].["Abacate", 12],...]
    return min(items, key=get_value_to_compair)[0]


class MaisBaratoTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['Banana', '2', 'Abacate', '20', 'maçã', '30'])
    def test_mais_barato(self, mock_input):
        self.assertEquals(mais_barato(mock_input), 'Banana')

    @ patch('builtins.input', side_effect=['Banana', '20', 'Abacate', '20', 'maçã', '1'])
    def test_mais_barato_2(self, mock_input):
        self.assertEquals(mais_barato(mock_input), 'maçã')


if __name__ == '__main__':
    produto = mais_barato(input)
    print(f'O produto que deve ser comprado é:{produto}')
