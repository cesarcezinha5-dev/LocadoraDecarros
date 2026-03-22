carros=[{"nome":"Chevrolet Onix", "preco":150, "tipo":"Automatico"},
        {"nome":"Fiat Pulse", "preco":135, "tipo":"Automatico"},
        {"nome":"Volkswagen Polo", "preco":140, "tipo":"Automatico"},
        {"nome":"Hyundai HB20S", "preco":130, "tipo":"Automatico"},
        {"nome":"Renault Kwid", "preco":80, "tipo":"Manual"},
        {"nome":"Volkswagen Gol", "preco":90, "tipo":"Manual"},
        {"nome":"Hyundai HB20", "preco":100, "tipo":"Manual"},
        {"nome":"Fiat Mobi", "preco":60, "tipo":"Manual"}]

seguros={"Basico":0.10, 
    "Intermediario":0.20,
     "Completo":0.30 }

print("FastCar - Sistema de Locação \n")
print("Escolha uma das opções abaixo: ")
escolha_menu=input("1 - Alugar carro\n2 - Sair\n")

if escolha_menu == "1":
    print("\nCarros disponiveis:\n")
    
    for i, carro in enumerate(carros):
        print(f"{i+1} - {carro['nome']} | R${carro['preco']}/Dia | {carro['tipo']}")

elif escolha_menu == "2":
    print("Obrigado...")
    exit()

escolha_carro=int(input("Qual carro deseja fazer a locação: "))

carro_escolhido=carros[escolha_carro-1]
print()
dias=int(input("Quantos dias? "))
print()

print("Escolha o tipo de seguro:\n")
for i,nome in enumerate(seguros):
    print(f'{i+1} - {nome} ({int(seguros[nome]*100)}%)')
escolha_seguro=int(input("Digite o numero do seguro que deseja: "))
lista_seguros = list(seguros.keys())
seguro_nome = lista_seguros[escolha_seguro - 1] 
seguro_taxa = seguros[seguro_nome]

valor_base = carro_escolhido["preco"] * dias
valor_seguro = valor_base * seguro_taxa
total = valor_base + valor_seguro   

print("\nResumo da locação:\n")
print(f"Carro: {carro_escolhido['nome']}")
print(f"Dias: {dias}")
print(f"Seguro: {seguro_nome}")
print(f"Total: R${total}")
        


