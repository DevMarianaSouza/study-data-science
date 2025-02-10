# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

# %%

tipo = input("Qual tipo de sorvete você gostaria? (casquinha, cascão ou cestinha)")

sabor = input("Escolha o sabor do sorvete: (morango, creme, chocolate) ")

cobertura = input("Escolha a cobertura: (caramelo, morango, chocolate, sem cobertura)")

valor = 0

sorvetes = {
    'casquinha': 1.00,
    'cascão': 2.5,
    'cestinha': 4.00
}

valor += sorvetes[tipo]


coberturas = {'caramelo':1.5,
              'morango':1.5,
              'chocolate':1.5,
              '':0}

valor += coberturas[cobertura]

print("Seu sorvete ", tipo, "de", sabor, "com cobertura de", cobertura, "custará: R$ ", valor)
# %%
