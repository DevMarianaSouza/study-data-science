# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipo = input("Qual tipo de sorvete você gostaria? (casquinha, cascão ou cestinha)")

sabor = input("Escolha o sabor do sorvete: (morango, creme, chocolate) ")

cobertura = input("Escolha a cobertura: (caramelo, morango, chocolate, sem cobertura)")

valor = 0

if tipo == 'casquinha':
    valor = valor + 1.00
elif tipo == 'cascão':
    valor += 2.50
elif tipo == 'cestinha':
    valor += 4.00
else: 
    print("Não foi possível encontrar esse tipo, escolha corretamente!")

coberturas = 'caramelo,morango,chocolate'

if cobertura in coberturas:
    valor += 1.5
elif cobertura == '':
    pass
else: 
    print("Escolha uma opção de cobertura válida!")

print("Seu sorvete ", tipo, "de", sabor, "com cobertura de", cobertura, "custará: R$ ", valor)