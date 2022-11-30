# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def genero(s):
    """
    :param s: espera uma string
    :return: None
    """
    s = s.upper()[0]
    if s == 'F':
        print('Feminino')
    elif s == 'M':
        print('Masculino')
    else:
        print('Outro')


if __name__ == '__main__':
    sexo = str(input('Digite o sexo: '))
    genero(sexo)