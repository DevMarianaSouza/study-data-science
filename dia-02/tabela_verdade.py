# Números
# 1
# 10.0
# -5
# -7.54

soma = 2 + 4 = 4

# Booleanos
True 
False

# %%

idade = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

# AND: Para que a condição seja TRUE, tudo deverá ser verdade. 
if idade >= 18 and cnh == 'sim':
    print("Siga em frente!")
else:
    print("Preso em nome da lei")

# %%

print("True e True =", bool(1 * 1))
print("False e True =", bool(0 * 1))
print("True e False =", bool(1 * 0))
print("False e False =", bool(0 * 0))
# %%

# OU: Para que a condição seja true, pelo menos uma deverá ser verdade.
print("True ou True =", bool(1 + 1))
print("False ou True =", bool(0 + 1))
print("True ou False =", bool(1 + 0))
print("False ou False =", bool(0 + 0))
# %%
