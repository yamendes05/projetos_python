def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return
def divisao(a,b):
    return a/b

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

def menu():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    return int(input("Digite a opção desejada: "))
while True:
    opcao = menu()
    if opcao == 1:
        print(soma(a,b))
    elif opcao == 2:
        print(subtracao(a,b))
    elif opcao == 3:
        print(multiplicacao(a,b))
    elif opcao == 4:
        print(divisao(a,b))
    elif opcao == 5:
        break
    else:
        print("Opção inválida")
