import random 

def adivinha(x):
    random_num = random.randint(1, x)  # ou defina um valor fixo, por exemplo: random_num = 5
    adivinha = 0
    while adivinha != random_num:
        adivinha = int(input(f'Adivinha um número entre 1 e {x}: '))
        if adivinha < random_num:
            print("Número maior")
        elif adivinha > random_num:
            print("Número menor")
    print("Você adivinhou o número!")

adivinha(10)  # Você pode definir o limite até 10 ou outro valor
