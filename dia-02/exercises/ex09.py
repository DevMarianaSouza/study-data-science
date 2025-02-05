# Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Entre com o seu nome completo")

nome = nome.lower() #coloca os elementos da string em minuscula

if "calvo" in nome:
    print("Você pertence a família Calvo")
else:
    print("Você não pertence a família Calvo")