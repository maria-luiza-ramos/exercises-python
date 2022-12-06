# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def fatorial_2():

    while True:

        num = int(input('Qual o número cuja o fatorial deve ser calculado? '))
        if num > 16 or num < 0:
            print('Valor Inválido. Digite novamente um número menor 16 e positivo.')
            num = int(input('Qual o número cuja o fatorial deve ser calculado? '))
        fat = 1

        for c in range(1, num + 1):
            fat *= c

        print(fat)

        escolha = input('Quer continuar? ').upper()[0]
        if escolha == 'N':
            break


if __name__ == '__main__':
    fatorial_2()