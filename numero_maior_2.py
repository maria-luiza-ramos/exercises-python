# Faça um Programa que leia três números e mostre o maior deles.
# Faça um Programa que leia três números e mostre o maior e o menor deles.

def numero_maior_2():

    maior_num = 0
    menor_num = 0
    for c in range(3):
        num = int(input(f'Digite o {c + 1} número: '))

        if c == 0:
            menor_num = num
            maior_num = num

        if num > maior_num:
            maior_num = num

        if num < menor_num:
            menor_num = num

    print(f'O maior número é: {maior_num}!')
    print(f'O menor número é: {menor_num}!')


if __name__ == '__main__':
    numero_maior_2()