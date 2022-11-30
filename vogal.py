# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def vogal(letra):

    letra = letra.lower()

    if letra in 'aeiou':
        print('A letra digitada é uma VOGAL')

    else:
        print('A letra gigitada é uma CONSOANTE')


if __name__ == '__main__':
    letra = str(input('Digite a letra: '))
    vogal(letra)