#Um sistema simples onde o usuário pode adicionar e remover tarefas.
tarefa = []

def adicionar_tarefa(tarefa,tarefas):
    tarefa.append(input("Digite a tarefa que deseja adicionar: "))
    print("Tarefa adicionada com sucesso!")
    return tarefa
def remover_tarefa(tarefa):
    tarefa.remove(input("Digite a tarefa que deseja remover: "))
    print("Tarefa removida com sucesso!")
    return tarefa

while True:
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        adicionar_tarefa(tarefa,tarefa)
    elif opcao == 2:
        remover_tarefa(tarefa)
    elif opcao == 3:
        break
    else:
        print("Opção inválida!")

print("Tarefas: ",tarefa)
print("Até mais!")
