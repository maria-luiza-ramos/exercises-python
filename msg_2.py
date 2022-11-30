def msg2():
    # Faça um Programa que pergunte em que turno você estuda.
    # Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    # Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    turnInput = str(input('Qual turno você estuda? ')).upper()[0]
    turn = {
        "M": "Bom dia",
        "V": "Boa Tarde",
        "N": "Boa noite"
    }
    print(turn.get(turnInput, 'Valor Inválido!'))


if __name__ == '__main__':
    msg2()
