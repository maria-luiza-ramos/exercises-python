# Faça um programa que calcule o mostre a média aritmética de N notas.

def media_aritmetica(n=list):
    soma = 0
    for c in n:
        soma += c
    m = soma / len(n)
    return m


if __name__ == '__main__':
    notas = []
    while True:
        nota = float(input('Digite a nota da prova: '))
        notas.append(nota)
        escolha = input('Deseja continuar [S/N]? ').upper()[0]
        if escolha == 'N':
            break
    media = media_aritmetica(notas)
    print(f'A média das notas foi: {media:.2f}')