# Faça um Programa que peça dois números e imprima o maior deles.

def numero_maior(num_1, num_2):
    """
    :param num_1: espera um número inteiro
    :param num_2: espera outro número inteiro
    :return: o maior número
    """

    if num_1 > num_2:
        return num_1

    elif num_2 > num_1:
        return num_2

    else:
        print(f'Os números são iguais!')


if __name__ == '__main__':
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um segundo número: '))
    numero = numero_maior(num_1, num_2)
    print(f'O maior número é {numero}.')