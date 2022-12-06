# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
# por quais número ele é divisível.

def e_primo_2(num):

    n_divisivel = list()

    for n in range(2, num//2+1):
        resto = num % n
        if resto == 0:
            n_divisivel.append(n)
            # print('Ele NÃO é primo')
            # return
    if len(n_divisivel) > 0:
        print(f'O número {num} NÃO é primo, pois ele é divisível por {n_divisivel}.')
    else:
        print(f'{num} é PRIMO.')


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    e_primo_2(num)