
def reajuste_salario(salario):
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

    if salario <= 280.0:
        aumento = 20
    elif 280 < salario < 700:
        aumento = 15
    elif 700 < salario < 1500:
        aumento = 10
    else:
        aumento = 5

    novo_salario = salario + (salario * aumento / 100)

    return [aumento, novo_salario]

if __name__ == "__main__":
    salario = float(input('Qual o salário atual? '))
    [aumento, novo_salario] = reajuste_salario(salario)
    print(f'O salário era de R${salario}. Com o aumento de {aumento}% foi para R${novo_salario}')
