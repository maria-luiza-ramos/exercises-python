# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def valor_positivo(num):

    if num > 0:
        print('O número é positvo')
    elif num == 0:
        print("O numero é 0")
    else:
        print('O número é negativo')


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    valor_positivo(num)