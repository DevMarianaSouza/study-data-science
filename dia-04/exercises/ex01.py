#Faça um programa que receba 4 notas, armazene em uma lista e depois mostre a soma dessas notas.

# a1 = int(input("Entre com a altura 1: "))
# a2 = int(input("Entre com a altura 2: "))
# a3 = int(input("Entre com a altura 3: "))
# a4 = int(input("Entre com a altura 4: "))

# alturas = [n1,n2,n3,n4]

alturas = []

for i in range[4]:
    a = int(input(f"Entre com a altura em cm {i+1}: "))
    alturas.append(a)

soma = sum(alturas)

print(soma)