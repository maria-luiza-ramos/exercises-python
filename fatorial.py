# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

def fatorial():

    num = int(input('Qual o número cuja o fatorial deve ser calculado? '))
    fat = 1

    for c in range(1, num+1):
        fat *= c

    print(fat)

if __name__ == '__main__':
    fatorial()