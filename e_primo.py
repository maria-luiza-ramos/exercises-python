# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1

def e_primo(num):
    """
    :param num: espera um número inteiro
    :return: 1 - num primo / 0 - num não é primo
    """

    for n in range(2, num//2+1):
        resto = num % n
        if resto == 0:
            # print('Ele NÃO é primo')
            return 0
    # print(f'{num} é PRIMO.')
    return 1


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    e_primo(num)