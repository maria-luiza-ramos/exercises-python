# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

def conjunto():

    num_maior = 0
    num_menor = 0
    soma = 0

    while True:
        num = int(input('Digite um número: '))
        if num > 1000 or num < 0:
            print('Valor Inválido. Digite novamente um número entre 0 e 1000.')
            num = int(input('Digite um número: '))

        escolha = input('Quer continuar? ').upper()[0]

        if soma == 0:
            num_maior = num
            num_menor = num
        if num > num_maior:
            num_maior = num
        if num < num_menor:
            num_menor = num
        soma += num
        if escolha == 'N':
            break
    print(f'O menor número foi {num_menor}, o maior número foi {num_maior}.'
          f' A soma de todos os números digitados é {soma}.')


if __name__ == '__main__':
    conjunto()