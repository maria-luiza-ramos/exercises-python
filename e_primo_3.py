# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
from e_primo import e_primo


def e_primo_3(n):

    list_primo = [1]
    for num in range(2, n+1):

        c = e_primo(num)
        if c == 1:
            list_primo.append(num)

    return print(list_primo)


if __name__ == '__main__':
    num = int(input('Quer a lista de números primos até qual número? '))
    e_primo_3(num)