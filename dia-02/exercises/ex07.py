# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

escolha = input("Você gostaria de uma garrafa de água mineral ou com gás? (mineral/gás): ")

if escolha == "mineral":
    print("Você me deve R$1,50")
elif escolha == "gás":
    print("Você me deve R$2,50")
else:
    print("Faça uma esclha válida!") 

# Altere o programa anterior para considerar a quantidade de água

escolha = input("Você gostaria de uma garrafa de água mineral ou com gás? (mineral/gás): ")

quantidade = int(input("Quantas águas você deseja? "))

if escolha == "mineral":
    total = 1.5 * quantidade
    
elif escolha == "gás":
    total = 2.5 * quantidade
else:
    print("Faça uma esclha válida!") 

print("Você me deve R$", total)