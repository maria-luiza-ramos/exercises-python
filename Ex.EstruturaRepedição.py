def valor_valido():
    # Faça um programa que peça uma nota, entre zero e dez.
    # Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

    while True:
        nota = float(input('Digite uma nota entre zero e dez: '))
        if nota > 10 or nota < 0:
            print('Valor inválido. Digite novamente.')
        else:
            print('Valor válido!')
            break


def digite_nome():
    # Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
    # mostrando uma mensagem de erro e voltando a pedir as informações

    while True:
        nome = input('Digite seu nome: ').replace(" ", "")
        senha = input('Digite a senha: ').replace(" ", "")

        if senha in nome:
            print('ERRO! Senha inválida.')
        else:
            break


def informacao():
    # Faça um programa que leia e valide as seguintes informações:
    # Nome: maior que 3 caracteres;
    # Idade: entre 0 e 150;
    # Salário: maior que zero;
    # Sexo: 'f' ou 'm';
    # Estado Civil: 's', 'c', 'v', 'd';

    while True:
        nome = input('Digite seu nome: ')
        if len(nome) < 3:
            print('Nome inválido!')
        else:
            break
    while True:
        idade = int(input('Qual sua idade? '))
        if idade < 0 or idade > 150:
            print('Opção Inválida!')
        else:
            break
    while True:
        salario = float(input('Digite seu salário: '))
        if salario < 0:
            print('Opção Inválida!')
        else:
            break
    while True:
        sexo = input('Qual seu sexo [F/M]? ').upper()[0]
        if sexo in 'FM':
            break
        else:
            print('Opção Inválida!')
    while True:
        estado_civil = input('Qual seu Estado Civil? [Solteiro/ Casado/ Viúvo/ Divorciado] ').upper()[0]
        if estado_civil in 'SCVD':
            break
        else:
            print('Opção Inválida!')


def crescimento_populacao():
    # Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
    # e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
    # Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou
    # iguale a população do país B, mantidas as taxas de crescimento.

    pais_a = 80000
    pais_b = 200000
    cont = 0

    while True:
        if pais_a < pais_b:
            pais_a += pais_a * 3 / 100
            pais_b += pais_b * 1.5 / 100
            cont += 1
        else:
            break
    print(f'Levara {cont} para o país A ultrapasse a população do país B.')
    print(f'A população do país A é: {pais_a:.2f}')
    print(f'A população do país B é: {pais_b:.2f}')


def cres_populacao_2(p1, p2, tx1, tx2):
    '''
        Função calcula o número de anos necessários para que a população do país A ultrapasse ou
        iguale a população do país B, mantidas as taxas de crescimento.
        :param p1: número da população A - int
        :param p2: Número da população B - int
        :param tx1: Taxa de crescimento anual população A - FLOAT
        :param tx2: Taxa de crescimento anual da população B - FLOAT
    '''
    # Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
    # Valide a entrada e permita repetir a operação.

    populacao_1 = p1
    populacao_2 = p2
    cont = 0

    while True:

        if populacao_1 < populacao_2:
            populacao_1 += populacao_1 * tx1 / 100
            populacao_2 += populacao_2 * tx2 / 100
            cont += 1
        else:
            break

    print(f'Levara {cont} anos para o país A ultrapasse a população do país B.')
    print(f'A população do país A é: {populacao_1:.2f}')
    print(f'A população do país B é: {populacao_2:.2f}')


def numeros():
    # Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
    # Depois modifique o programa para que ele mostre os números um ao lado do outro.

    for c in range(20):
        print(f'{c+1}', end=' ')


def maior_numero():
    # Faça um programa que leia 5 números e informe o maior número.
    maior = 0
    for n in range(5):
        num = int(input('Digite um número:'))
        if num > maior:
            maior = num
    print(f'O maior número digitado foi {maior}.')


def media_numero():
    # Faça um programa que leia 5 números e informe a soma e a média dos números.

    soma = 0
    for n in range(5):
        num = float(input('Digite um número:'))
        soma += num
    media = soma / 5
    print(f'A média dos 5 números digitados foi {media}')


def numero_impar():
    # Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
    print('Os números ímpares entre 1 e 50 são:', end=' ')
    for n in range(1, 51):
        if n % 2 == 1:
            print(n, end=' ')


def intervalo(n1, n2):
    #Faça um programa que receba dois números int e gere os números int que estão no intervalo compreendido por eles.
    # Altere o programa para mostrar no final a soma dos números.

    print(f'Os números que estão no intervalo entre {n1} e {n2} são: ', end='')
    soma = 0
    for n in range(n1, n2):
        if n != n1:
            print(n, end=' ')
            soma += n
    print(f'\nA soma dos número é {soma}')


def tabuada():
    # Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
    # O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    num = int(input('De qual número deseja ver a tabuada? '))
    print('TABUADA'.center(20))
    for n in range(10):
        resultado = (n+1) * num
        print(f'{n+1} * {num} = {resultado}')


if __name__ == '__main__':
    tabuada()