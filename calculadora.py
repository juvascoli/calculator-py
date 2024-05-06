def menu():

  opcao = -1
  while (opcao < 1 or opcao > 4):
    print(':D menu')
    print('1- adição')
    print('2- subtração')
    print('3- multiplicação')
    print('4- divisaõ')
    opcao = int(input('escolha a operação: '))
    if (opcao < 1 or opcao > 4):
        print('opção inválida')
    return opcao

def entrada_dados():
    print('entrada de dados')
    num = int(input('número: '))
    return num

def adicao(n1, n2):
    print('adição')
    return n1 + n2

def subtracao(n1, n2):
    print('subtração')
    return n1 - n2

def multiplicacao(n1, n2):
    print('multiplicação')
    return n1 * n2

def divisao(n1, n2):
    print('divisaõ')
    return n1 / n2

def imprimir(result):
    print('imprimir')
    print(f'resultado {result}')

def controlador(opcao, n1, n2):
    print('controlador')
    if opcao == 1:
        resultado = adicao(n1, n2)
    elif opcao == 2:
        resultado = subtracao(n1,n2)
    elif opcao == 3:
        resultado = multiplicacao(n1, n2)
    else:
        resultado = divisao(n1,n2)
    return resultado

#main
opcao = menu()
n1 = entrada_dados()
n2 = entrada_dados()
resultado = controlador(opcao, n1, n2)
imprimir(resultado)
