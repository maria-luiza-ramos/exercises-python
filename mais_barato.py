def mais_barato():
    # Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
    # sabendo que a decisão é sempre pelo mais barato.

    produtos = {}
    for p in range(3):
        produto = str(input('Qual o nome do produto? '))
        valor = float(input(f'Qual o valor do {produto}? '))
        produtos[produto] = valor

    print(f'O produto que deve ser comprado é:{min(produtos)}')


if __name__ == '__main__':
    mais_barato()