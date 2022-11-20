import math


def reajuste_salario():
    # As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    # Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5%
    # Após o aumento ser realizado, informe na tela:
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento.

    salario = float(input('Qual o salário atual? '))

    if salario <= 280.0:
        aumento = 20
    elif 280 < salario < 700:
        aumento = 15
    elif 700 < salario < 1500:
        aumento = 10
    else:
        aumento = 5

    novo_salario = salario + (salario * aumento / 100)
    print(f'O salário era de R${salario}. Com o aumento de {aumento}% foi para R${novo_salario}')


def desconto_salario():
    # Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
    # que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
    # mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
    # O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    # Desconto do IR:

    # Salário Bruto até 900 (inclusive) - isento
    # Salário Bruto até 1500 (inclusive) - desconto de 5%
    # Salário Bruto até 2500 (inclusive) - desconto de 10%
    # Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    # No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    hora = int(input('Quantas horas você trabalhou esse mês? '))
    valor = float(input('Qual o valor da sua hora trabalhada? '))
    salario_bruto = valor * hora
    fgts = salario_bruto * 11 / 100
    inns = salario_bruto * 10 / 100

    if salario_bruto <= 900:
        salario_liquido = salario_bruto - inns

        print(f'{"Salário Bruto:":<10} ({valor} * {hora}) {": R$":>10} {salario_bruto}\n'
              f'{"(-) IR (0%)":<10} {": R$ 0,00":>30}\n'
              f'(-) INNS (10%) {": R$" :>22} {inns}\n'
              f'FGTS (11%) {": R$" :>26} {fgts}\n'
              f'Total de Descontos  {": R$" :>17} {inns}\n'
              f'Salário Liquido  {": R$" :>20}{salario_liquido}')

    elif 900 < salario_bruto < 1500:

        ir = salario_bruto * 5 / 100
        salario_liquido = salario_bruto - inns - ir
        print(f'{"Salário Bruto:":<10} ({valor} * {hora}) {": R$":>10} {salario_bruto}\n'
              f'{"(-) IR (5%)":<10} {": R$":>25} {ir}\n'
              f'(-) INNS (10%) {": R$" :>22} {inns}\n'
              f'FGTS (11%) {": R$" :>26} {fgts}\n'
              f'Total de Descontos  {": R$" :>17} {inns + ir}\n'
              f'Salário Liquido  {": R$" :>20} {salario_liquido}')

    elif 1500 < salario_bruto < 2500:
        ir = salario_bruto * 10 / 100
        salario_liquido = salario_bruto - inns - ir
        print(f'{"Salário Bruto:":<10} ({valor} * {hora}) {": R$":>10} {salario_bruto}\n'
              f'{"(-) IR (10%)":<10} {": R$":>25} {ir}\n'
              f'(-) INNS (10%) {": R$" :>22} {inns}\n'
              f'FGTS (11%) {": R$" :>26} {fgts}\n'
              f'Total de Descontos  {": R$" :>17} {inns + ir}\n'
              f'Salário Liquido  {": R$" :>20} {salario_liquido}')

    else:
        ir = salario_bruto * 20 / 100
        salario_liquido = salario_bruto - inns - ir
        print(f'{"Salário Bruto:":<10} ({valor} * {hora}) {": R$":>10} {salario_bruto}\n'
              f'{"(-) IR (20%)":<10} {": R$":>25} {ir}\n'
              f'(-) INNS (10%) {": R$" :>22} {inns}\n'
              f'FGTS (11%) {": R$" :>26} {fgts}\n'
              f'Total de Descontos  {": R$" :>17} {inns + ir}\n'
              f'Salário Liquido  {": R$" :>20} {salario_liquido}')


def dia_semana():
    # Faça um Programa que leia um número e exiba o dia correspondente da semana.
    # (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

    num_semana = {1: 'Domingo', 2: 'Segunda', 3: 'Terça',
                  4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
    num = int(input('Digite o número do dia da semana: '))

    try:
        print(num_semana[num])

    except:
        print('Valor Inválido')


def media_nota():
    # Faça um programa que lê as duas notas parciais, e calcule a sua média.
    #   Entre 9.0 e 10.0 - A * Entre 7.5 e 9.0 - B * Entre 6.0 e 7.5 - C * Entre 4.0 e 6.0 - D * Entre 4.0 e zero - E
    # O algoritmo deve mostrar na tela as notas, a média, o conceito e a mensagem “APROVADO” se for A, B ou C ou
    # “REPROVADO” se o conceito for D ou E.

    nota_1 = float(input('Qual foi a pontuação da primeira prova? '))
    nota_2 = float(input('E a potuação da segunda prova?'))
    media = (nota_2 + nota_1) / 2

    if 9 < media <= 10:
        print(f'APROVADO! A média entre as notas {nota_1} e {nota_2} foi {media}.\n'
              f'Aluno conceito - A -')
    elif 7.5 < media <= 9:
        print(f'APROVADO! A média entre as notas {nota_1} e {nota_2} foi {media}.\n'
              f'Aluno conceito - B -')
    elif 6 < media <= 7.5:
        print(f'APROVADO! A média entre as notas {nota_1} e {nota_2} foi {media}.\n'
              f'Aluno conceito - C -')
    elif 4 < media <= 6:
        print(f'REPROVADO! A média entre as notas {nota_1} e {nota_2} foi {media}.\n'
              f'Aluno conceito - D -')
    elif 0 < media <= 6:
        print(f'REPROVADO! A média entre as notas {nota_1} e {nota_2} foi {media}.\n'
              f'Aluno conceito - E -')


def e_triangulo():
    # Faça um Programa que peça os 3 lados de um triângulo.
    # O programa deverá informar se os valores podem ser um triângulo.
    # Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    # Dicas:
    # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    # Triângulo Equilátero: três lados iguais;
    # Triângulo Isósceles: quaisquer dois lados iguais;
    # Triângulo Escaleno: três lados diferentes;

    l1 = int(input('Informe o primeiro lado de um triângulo: '))
    l2 = int(input('Informe o segundo lado: '))
    l3 = int(input('Informe o valor do terceiro lado: '))

    if not (l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2):
        print('Não é um Triângulo')
    elif l1 == l2 == l3:
        print('É um Triângulo Equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('É um Triângulo Isósceles!')
    else:
        print('É um Triângulo Escaleno!')


def equacao_2():
    # Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
    # O programa deverá pedir os valores de a, b e c e fazer as consistências,
    # informando ao usuário nas seguintes situações:
    # Se A for igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores
    # Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    # Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    # Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

    a = int(input('Informe o valor de -a- da equação do segundo grau: '))

    if a == 0:
        print('A com valor igual a zero, a equação não é do segundo grau')
        return  # early return: evita a necessidade de else pq sai da função neste momento

    b = int(input('Informe o valor de -b- da equação do segundo grau: '))
    c = int(input('Informe o valor de -c- da equação do segundo grau: '))

    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('A equação não possui raizes reais.')
        return

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    if x1 == x2:
        print(f'A equação possui uma raiz real. Que é {x1}')
        return
    print(f'A equação possui duas raiz reais. Que são {x1} e {x2}')


def ano_bissexto():
    # Faça um Programa que peça um número correspondente a um
    # determinado ano e em seguida informe se este ano é bissexto.

    ano = int(input('Digite o ano: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('Bissexto')
    else:
        print('Não é bissexto')


def data():
    # Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    data = str(input(f'Informa a data (dd/mm/aaaa): '))

    t_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    if int(data[3:5]) in t_mes and 0 < int(data[0:2]) <= 31 and int(data[6:]) != 0:
        print('Data Válida')

    else:
        print('Data Inválida ')


def numero():
    # Faça um Programa que leia um número inteiro menor que 1000 e moste as centenas, dezenas e unidades do mesmo.
    # Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    # 326 = 3 centenas, 2 dezenas e 6 unidades
    # 12 = 1 dezena e 2 unidades Testar
    #  com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    num = str(input('Digite o número: '))
    plural = ['unidades', 'dezenas', 'centenas', "unidades de milhar", "dezenas de milhar", "centenas de milhar"]
    singular = ['unidade', 'dezena', 'centena', "unidade de milhar", "dezena  de milhar", "centena  de milhar"]
    num_list = list(num)
    num_list.reverse()
    formatted_array = []
    for index in range(len(num_list)):
        value = int(num_list[index])
        desc = singular[index] if value == 1 else plural[index]
        if value != 0:
            formatted_array.append(f"{value} {desc}")
    formatted_array_with_separator = []
    for index in range(len(formatted_array)):
        if index == 0:
            separator = ""
        elif index == 1:
            separator = " e "
        else:
            separator = ", "
        formatted_array_with_separator.append(f'{formatted_array[index]}{separator}')

    formatted_array_with_separator.reverse()
    print(f'{num} = {"".join(formatted_array_with_separator)}')


def media_nota_2():
    # Faça um Programa para leitura de três notas parciais de um aluno.
    # A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    # A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    # A mensagem "Aprovado com Distinção", se a média for igual a 10.

    nota_1 = float(input('Qual foi a pontuação da primeira prova? '))
    nota_2 = float(input('E a potuação da segunda prova?'))
    nota_3 = float(input('Qual a pontuação da terceira prova? '))

    media = (nota_2 + nota_2 + nota_3) / 3

    if media == 10:
        print(f'APROVADO COM DISTINÇÃO! Sua média foi {media:.2f}')
    elif media >= 7:
        print(f'APROVADO! Sua média foi {media:.2f}')
    elif media < 7:
        print(f'REPROVADO! Sua média foi {media:.2f}')


if __name__ == '__main__':
    numero()
