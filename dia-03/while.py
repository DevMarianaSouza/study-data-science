# %%

quantidade = int(input("Quantos oies você quer dar? "))

count = 1
while count <= quantidade:
    print("Oie")
    count += 1  # count = count + 1

# %%

while True:

    senha = input("Entre com a senha: ")
    if senha == "1234":
        break
    elif senha == "123":
        print("Quase lá...")
        continue
    print("de novo")

print("Sai do laço!")

# %%

#Imprimir somente números pares

contador = 1
while contador <= 15:
    if contador % 2 == 0:
        print(contador)
    contador += 1
# %%
