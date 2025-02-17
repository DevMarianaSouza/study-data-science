# %% 
def soma(*args):
    total = 0

    for i in args:
        total += i
    return total
soma(1,2,3,4,5,6,7,8,9,10)
# %%

def operacao(op, *num): 
    total = 0

    if op == 'soma':
        for i in num:
            total += 1
    elif op == 'mult':
        total = 1
        for i in num:
            total *= 1 
    return total
operacao('multi', 1,2,3,4,5,6,7,8,9,10)

# %%

#Unpack de uma lista, usando *

dados = ['Mari', 'Souza', 30, 'Virgem', 'Solteira']

nome, sobrenome, *lixo = dados
# ou nome, sobrenome, *_ = dados
print(nome)
print(sobrenome)

# %%
