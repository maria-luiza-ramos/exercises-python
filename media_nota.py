# Faça um programa para a leitura de duas notas parciais de um aluno.
    # O programa deve calcular a média alcançada por aluno e apresentar:
    # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # A mensagem "Reprovado", se a média for menor do que sete;
    # A mensagem "Aprovado com Distinção", se a média for igual a dez.

def media_nota(n1, n2):
    notas = n1+n2
    media = notas / 2

    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aluno APROVADO!')
    else:
        print('Aluno REPROVADO!')


if __name__ == '__main__':
    notas = []
    for c in range(2):
        nota = float(input(f'Qual a nota da {c + 1} prova? '))
        notas.append(nota)
    media_nota(notas[0], notas[1])