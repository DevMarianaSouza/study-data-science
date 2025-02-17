# Como podemos ler arquivos

# %%
## PARA ABRIR UM ARQUIVO USA OPEN
# E DIZER O QUE VC QUER FAZER, NO CASO W DE WRITE

arquivo = open("aquivo.txt", 'w')
# %%

arquivo.write("Mari ana")


# %%
## PARA QUE 'SALVE' AS INFORMAÇÕES NO NOVO ARQ CRIADO
## É NECESSÁRIO FECHAR O ARQ.
arquivo.close()
# %%
## O 'A' SERVE PARA ADICIONAR COISAS NO ARQUIVO
arquivo = open("arquivo.txt", 'a')
arquivo.write("1")
arquivo.close()

# %%

## PARA LER ALGUM ARQUIVO

arquivo = open("arquivo.txt", 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
print(type(conteudo))
# %%

## usar with para abrir arquivo, para conexão de banco de dados.

## Esse with está falando: 
#Enquanto esse arquivo estiver aberto, você executa isso, no caso, read. E quando sair, vai fechar o arquivo sozinho.
#É preferivel usar o with pq ele garante que no final da execução ele vai fechar o arquivo. 
#Dentro do with é como se já tivesse a função close dentro. 
with open("arquivo.txt", 'r') as file:
    conteudo = file.read()

print(conteudo) 