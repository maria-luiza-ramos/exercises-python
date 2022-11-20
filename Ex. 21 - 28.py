def caixa_eletronico():
    # Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
    # depois informar quantas notas de cada valor serão fornecidas.
    # As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
    # O valor mínimo é de 10 reais e o máximo de 600 reais.

    print('O valor para saque mínimo é de 10 reais e o máximo de 600 reais.')
    valor_saque = int(input('Qual o valor do saque? R$ '))
    notas = {'1': 0, '5': 0, '10': 0, '50': 0, '100': 0}
    print(f'Para sacar {valor_saque}, serão oferecidas:', end=' ')

    if valor_saque < 10 or valor_saque > 600:
        print('Valor inválido!')
    else:
        cem = valor_saque // 100
        valor_saque -= cem * 100
        notas['100'] = cem
        cinquenta = valor_saque // 50
        valor_saque -= cinquenta *50
        notas['50'] = cinquenta
        dez = valor_saque // 10
        valor_saque -= dez * 10
        notas['10'] = dez
        cinco = valor_saque // 5
        valor_saque -= cinco * 5
        notas['5'] = cinco
        um = valor_saque // 1
        valor_saque -= um * 1
        notas['1'] = um

    for keys, v in notas.items():
        if v > 0:
            print(f'{v} nota(s) de {keys} reais.', end=' ')


def e_par():
    # Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print(f'O número {num} é Par.')
    else:
        print(f'O número é Impar.')


def is_decimal():

    # Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
    # Dica: utilize uma função de arredondamento.

    num = input('Digite um número: ')

    if '.' in num or ',' in num:
        print('É um número decimal')
    else:
        print('É um número inteiro')


def operacao():
    # Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
    # O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    # par ou ímpar;
    # positivo ou negativo;
    # inteiro ou decimal.

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    op = input('Qual é a operação? [Soma / Subtração/ Multiplicação/ Divição] ').upper()[0:2]
    soma = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2

    if op == 'SO':
        print(f'O resultado é {soma}. Que é um número', end=' ')
        if soma % 2 == 0:
            print('par,', end=' ')
        else:
            print('impar,', end=' ')
        if soma // 1 == soma:
            print('inteiro e', end=' ')
        else:
            print('decimal e', end=' ')
        if soma > 0:
            print('posito.')
        else:
            print('negativo.')
    elif op == 'SU':
        print(f'O resultado é {sub}. Que é um número', end=' ')
        if sub % 2 == 0:
            print('par,', end=' ')
        else:
            print('impar,', end=' ')
        if sub // 1 == sub:
            print('inteiro e', end=' ')
        else:
            print('decimal e', end=' ')
        if sub > 0:
            print('posito.')
        else:
            print('negativo.')
    elif op == 'MU':
        print(f'O resultado é {mul}. Que é um número', end=' ')
        if mul % 2 == 0:
            print('par,', end=' ')
        else:
            print('impar,', end=' ')
        if mul // 1 == mul:
            print('inteiro e', end=' ')
        else:
            print('decimal e', end=' ')
        if mul > 0:
            print('posito.')
        else:
            print('negativo.')
    elif op == 'DI':
        print(f'O resultado é {div}. Que é um número', end=' ')
        if div % 2 == 0:
            print('par,', end=' ')
        else:
            print('impar,', end=' ')
        if div // 1 == div:
            print('inteiro e', end=' ')
        else:
            print('decimal e', end=' ')
        if div > 0:
            print('posito.')
        else:
            print('negativo.')


def crime():
    # Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    # "Telefonou para a vítima?"
    # "Esteve no local do crime?"
    # "Mora perto da vítima?"
    # "Devia para a vítima?"
    # "Já trabalhou com a vítima?"
    # O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    # entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

    print('Responda SIM ou NÃO para as perguntas abaixo.')
    classificacao = []
    sim = 0
    nao = 0

    pergunta_1 = input("Telefonou para a vítima? ").upper()[0]
    classificacao.append(pergunta_1)

    pergunta_2 = input("Esteve no local do crime? ").upper()[0]
    classificacao.append(pergunta_2)

    pergunta_3 = input("Mora perto da vítima? ").upper()[0]
    classificacao.append(pergunta_3)

    pergunta_4 = input("Devia para a vítima? ").upper()[0]
    classificacao.append(pergunta_4)

    pergunta_5 = input("Já trabalhou com a vítima? ").upper()[0]
    classificacao.append(pergunta_5)

    for c in classificacao:
        if c == 'S':
            sim += 1
        else:
            nao += 1

    if sim == 2:
        print('SUSPEITA.')
    elif 2 < sim < 5:
        print('CÚMPLICE.')
    elif sim == 5:
        print('ASSASSINO.')
    else:
        print('INOCENTE.')


def precao_posto():
    # Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    # Álcool:
    # até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro
    # Gasolina:
    # até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6% por litro
    # Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
    #  calcule e imprima o valor a ser pago. preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

    litros = float(input('Qual a quantidade de litros? '))
    combustivel = input('Qual o combustível? [Gasolina / Alccol] ').upper()[0]

    if combustivel == 'A':
        valor = 1.90 * litros
        if litros <= 20:
            valor_desconto = valor - (valor * 3 / 100)
        else:
            valor_desconto = valor - (valor * 5 / 100)
    elif combustivel == 'G':
        valor = 2.50 * litros
        if litros <= 20:
            valor_desconto = valor - (valor * 4 / 100)
        else:
            valor_desconto = valor - (valor * 6 / 100)
    else:
        print('Opção inválida!')
    print(f'O valor pago é R$ {valor_desconto:.2f}')


def frutaria():
    # Morango -  Até 5 Kg  - R$ 2,50 por Kg  / Acima de 5 - Kg R$ 2,20 por Kg
    # Maçã - Até 5 Kg  - R$ 1,80 por Kg   / Acima de 5 - R$ 1,50 por Kg
    # Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    # receberá ainda um desconto de 10% sobre este total.
    # Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
    # escreva o valor a ser pago pelo cliente.

    morango_kg = float(input('Qual a quantidade de morangos em KG? '))
    maca_kg = float(input('Qual a quantidade de maçao em KG? '))
    total_kg = morango_kg + maca_kg

    if morango_kg <= 5:
        valor_morango = morango_kg * 2.50
    else:
        valor_morango = morango_kg * 2.20
    if maca_kg <= 5:
        valor_maca = maca_kg * 1.80
    else:
        valor_maca = maca_kg * 1.50

    valor_total = valor_maca + valor_morango

    if total_kg > 8 or valor_total > 25:
        valor_desc = valor_total - (valor_total * 10 / 100)
        print(f'O valor total da compra com desconto de 10% é: {valor_desc}')
    else:
        print(f'O valor da compra é: {valor_total}')


def supermecado():
    # Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    # porém não há limites para a quantidade de carne por cliente.
    # Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
    # Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    # falando: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

    print('CLIENTE PODE LEVAR APENAS UM TIPO DE CORTE DE CARNE')
    carne = input('Qual o corte de carne? [File Duplo, Alcatra ou Picanha] ').upper()[0]
    quant = float(input('Quantos kg? '))
    pagamento = input('Qual o pagamento? [Cartão Tabajara ou Dinheiro]').upper()[0]

    if carne == 'F':
        if quant <= 5:
            valor = quant * 4.90
        else:
            valor = quant * 5.80
    elif carne == 'A':
        if quant <= 5:
            valor = quant * 5.90
        else:
            valor = quant * 6.80
    elif carne == 'P':
        if quant <= 5:
            valor = quant * 6.90
        else:
            valor = quant * 7.80
    else:
        print('Não tem essa opção de corte.')

    if pagamento == 'C':
        desc = valor * 10 / 100
        print(f'NOTA'.center(30))
        print(f'{carne} ----- {quant}KG\n'
              f'Pagamento: {pagamento}\n'
              f'Valor total R${valor}\n'
              f'Desconto: R${desc}\n'
              f'Valor a pagar: R${valor - desc}')
    else:
        print(f'NOTA'.center(30))
        print(f'{carne} ----- {quant} KG\n'
              f'Pagamento: {pagamento}\n'
              f'Valor total R$ {valor}\n'
              f'Desconto: R$ 0.00\n'
              f'Valor a pagar: R$ {valor}')


if __name__ == '__main__':
    supermecado()