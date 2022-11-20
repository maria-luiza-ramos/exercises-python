def numero_maior():
    # Faça um Programa que peça dois números e imprima o maior deles.

    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um segundo número: '))

    if num_1 > num_2:
        print(f'O número {num_1} é maior!!')

    elif num_2 > num_1:
        print(f'O número {num_2} é maior!!')

    else:
        print(f'Os números são iguais!')


def valor_positivo():
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

    num = int(input('Digite um número: '))

    if num > 0:
        print('O número é positvo')
    elif num == 0:
        print("O numero é 0")
    else:
        print('O número é negativo')


def genero():
    # Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    # Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

    sexo = str(input('Digite o sexo: ')).upper()[0]

    if sexo == 'F':
        print('Feminino')
    elif sexo == 'M':
        print('Masculino')
    else:
        print('Outro')


def vogal():
    # Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    letra = str(input('Digite a letra: ')).lower()

    if letra in 'aeiou':
        print('A letra digitada é uma VOGAL')

    else:
        print('A letra gigitada é uma CONSOANTE')


def media_nota():
    # Faça um programa para a leitura de duas notas parciais de um aluno.
    # O programa deve calcular a média alcançada por aluno e apresentar:
    # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # A mensagem "Reprovado", se a média for menor do que sete;
    # A mensagem "Aprovado com Distinção", se a média for igual a dez.

    notas = 0
    for c in range(2):
        nota = float(input(f'Qual a nota da {c + 1} prova? '))
        notas += nota
    media = notas / 2
    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aluno APROVADO!')
    else:
        print('Aluno REPROVADO!')


def numero_maior_2():
    # Faça um Programa que leia três números e mostre o maior deles.
    # Faça um Programa que leia três números e mostre o maior e o menor deles.

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


def mais_barato():
    # Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    # sabendo que a decisão é sempre pelo mais barato.

    produtos = {}
    for p in range(3):
        produto = str(input('Qual o nome do produto? '))
        valor = float(input(f'Qual o valor do {produto}? '))
        produtos[produto] = valor

    print(f'O produto que deve ser comprado é:{min(produtos)}')


def decrescente():
    # Faça um Programa que leia três números e mostre-os em ordem decrescente.

    decrescente_numeros = []

    for n in range(3):
        num = int(input('Digite um número: '))

        decrescente_numeros.append(num)

    decrescente_numeros.sort(reverse=True)
    print(decrescente_numeros)


def msg():
    # Faça um Programa que pergunte em que turno você estuda.
    # Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    # Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    turno = str(input('Qual turno você estuda? ')).upper()[0]
    turn = {
        "M": "Bom dia",
        "V": "Boa Tarde",
        "N": "Boa noite"
    }
    if turno == 'M':
        print('Bom dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor Inválido!')


def msg2():
    # Faça um Programa que pergunte em que turno você estuda.
    # Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
    # Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    turnInput = str(input('Qual turno você estuda? ')).upper()[0]
    turn = {
        "M": "Bom dia",
        "V": "Boa Tarde",
        "N": "Boa noite"
    }
    print(turn.get(turnInput, 'Valor Inválido!'))


if __name__ == '__main__':
    msg2()
