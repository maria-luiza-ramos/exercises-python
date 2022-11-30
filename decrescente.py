def decrescente():
    # Faça um Programa que leia três números e mostre-os em ordem decrescente.

    decrescente_numeros = []

    for n in range(3):
        num = int(input('Digite um número: '))

        decrescente_numeros.append(num)

    decrescente_numeros.sort(reverse=True)
    print(decrescente_numeros)


if __name__ == '__main__':
    decrescente()