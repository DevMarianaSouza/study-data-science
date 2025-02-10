# %%

dados = {"nome":"Mari", "sobrenome":"Souza", "idade":"30"}
nome = dados["nome"]

print(nome)
# %%

# ex: como pegar a idade do meu primeiro filho

dados = {"nome":"Mari",
        "sobrenome":"Souza",
        "idade":"30",
        "filhos":[ {"nome":"Lara", "idade":2}, {"nome":"Raul", "idade":"1"}]}
nome = dados["nome"]
print(nome)

print(dados["filhos"][0]["nome"])
print(dados["filhos"][0]["idade"])
# %%
