def cadastrar_produto(estoque):
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo in estoque:
            print("Produto já cadastrado.")
        else:
            descricao = input("Digite a descrição do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            estoque[codigo] = {"descricao": descricao, "preco": preco, "quantidade": quantidade}
            print("Produto cadastrado com sucesso.")
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    return estoque

def consultar_produto(estoque):
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo in estoque:
            produto = estoque[codigo]
            print(f"Descrição: {produto['descricao']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
        else:
            print("Produto não cadastrado.")
    except ValueError:
        print("Erro: Digite um código numérico válido.")
    return estoque

def remover_produto(estoque):
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo in estoque:
            del estoque[codigo]
            print("Produto removido com sucesso.")
        else:
            print("Produto não cadastrado.")
    except ValueError:
        print("Erro: Digite um código numérico válido.")
    return estoque

def menu():
    print("\n1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Remover produto")
    print("4 - Sair")
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        print("Erro: Digite um número válido.")
        return 0

def main():
    estoque = {}
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_produto(estoque)
        elif opcao == 2:
            consultar_produto(estoque)
        elif opcao == 3:
            remover_produto(estoque)
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
