import unittest


# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


def msg_by_turn(turnInput):
    turn = {
        "M": "Bom dia",
        "V": "Boa Tarde",
        "N": "Boa noite"
    }
    #.get recebe uma chave e procura no dict e retorna o valor dela, caso não tenha a chave ela retorna
    # o valor definido no segundo parametro que tem o valor default None
    return turn.get(turnInput, 'Valor Inválido!')


class MsgTest(unittest.TestCase):
    def test_bom_dia(self):
        self.assertEqual(msg_by_turn("M"), "Bom dia")

    def test_boa_tarde(self):
        self.assertEqual(msg_by_turn("V"), "Boa Tarde")

    def test_boa_noite(self):
        self.assertEqual(msg_by_turn("N"), "Boa noite")

    def test_invalido(self):
        self.assertEqual(msg_by_turn(3), 'Valor Inválido!')

    def test_invalido_2(self):
        self.assertEqual(msg_by_turn("B"), 'Valor Inválido!')


if __name__ == '__main__':
    turnInput = str(input('Qual turno você estuda? ')).upper()[0]
    print(msg_by_turn(turnInput))
