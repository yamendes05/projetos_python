
tesoura = 1
pedra = 1
papel = 1

# Entrada dos usuários
usuario1 = int(input("Usuário 1, escolha: 1- Pedra, 2- Tesoura, 3- Papel: "))
usuario2 = int(input("Usuário 2, escolha: 1- Pedra, 2- Tesoura, 3- Papel: "))

# Verificando resultados
if usuario2 == pedra and usuario1 == tesoura:
    print("Usuário 2 ganhou!")
elif usuario2 == pedra and usuario1 == papel:
    print("Usuário 1 ganhou!")
elif usuario2 == pedra and usuario1 == pedra:
    print("Empate!")
elif usuario2 == tesoura and usuario1 == pedra:
    print("Usuário 1 ganhou!")
elif usuario2 == tesoura and usuario1 == papel:
    print("Usuário 2 ganhou!")
elif usuario2 == tesoura and usuario1 == tesoura:
    print("Empate!")
elif usuario2 == papel and usuario1 == pedra:
    print("Usuário 2 ganhou!")
elif usuario2 == papel and usuario1 == tesoura:
    print("Usuário 1 ganhou!")
elif usuario2 == papel and usuario1 == papel:
    print("Empate!")
else:
    print("Entrada inválida. Por favor, escolha entre 1, 2 ou 3.")
