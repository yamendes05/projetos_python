import math

valor_imovel = float(input("Digite o valor do imóvel: "))
investimento = float(input("Digite o valor do investimento inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))

# Calcula 1% do valor do imóvel para verificar a viabilidade do investimento
resultado = valor_imovel * 1 / 100

if investimento < resultado:
    print("Investimento não viável.")
else:
    
    vezes_por_ano = 12

    # Função para calcular o tempo necessário para atingir o valor do imóvel
    def calcular_tempo(valor_inicial, valor_final, taxa_juros, vezes_por_ano):
       
        taxa_decimal = taxa_juros / 100
        # Aplica a fórmula para calcular o tempo
        tempo = math.log(valor_final / valor_inicial) / (vezes_por_ano * math.log(1 + taxa_decimal / vezes_por_ano))
        return tempo

    tempo_em_anos = calcular_tempo(investimento, valor_imovel, taxa_juros, vezes_por_ano)
    tempo_em_meses = tempo_em_anos * 12  


    anos = int(tempo_em_meses // 12)
    meses = int(tempo_em_meses % 12)

    print(f"Você precisará de aproximadamente {anos} anos e {meses} meses para atingir o valor do imóvel.")
