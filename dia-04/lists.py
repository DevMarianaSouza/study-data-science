# %%

minha_lista = ["Mari", "Souza", 30, 1,70]
print(minha_lista)
# %%

minha_lista[0]
# %%

#para saber a ultima posição de uma lista

minha_lista[len(minha_lista)-1]

# é a mesma coisa que: 

minha_lista[-1]


# %%

#Fatiamento de lista (slice)
#0 começa, 2 termina, sem contar com o elemento 2
minha_lista[0:2]
# %%

#pegar todos os elementos menos o ultimo 

minha_lista[0:-1]
# %%
minha_lista[::-1] #inversão da lista
# %%
minha_lista = ["Mari", "Souza", 30, 1.70]
minha_lista[::2] # do inicio ao fim pulando 1
# %%

notas = []
nota = 7.75

notas.append(nota)

#%%

#usando for em listas

nomes = ['mari', 'souza', 'dev']
for nome in nomes:
    print(nome)
# %%
nomes = ['mari', 'souza', 'dev']
for i in nomes:
    print(i.title())
# %%

#como acessar um elemento dentro de uma lista dentro de uma lista

dados = ['Mari', 'Souza', 'Dev', ['Mãe', 'Pai', 'Irmã'], ['Max']]

dados[3][-1] #quero acessar minha irmã
# %%
#quero acessar a primeira letra do nome do meu cachorro

dados[-1][0][0]
# %%
