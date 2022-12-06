# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
# se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
from media_aritmetica import media_aritmetica


def media_idade(id=list):
    media = media_aritmetica(id)
    if media <= 25:
        return print('A turma é JOVEM!')
    elif media <= 60:
        return print('A turma é ADULTA!')
    else:
        return print('A turma é IDOSA!')


if __name__ == '__main__':
    idades = []
    while True:
        idade = float(input('Qual idade da pessoa? '))
        idades.append(idade)
        escolha = input('Deseja continuar [S/N]? ').upper()[0]
        if escolha == 'N':
            break
    media_idade(idades)
