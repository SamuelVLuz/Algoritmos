from pilha import *
linhas = []
f = open("teste.txt","r")
for linha in f:
    linhas.append(linha.strip())
f.close()
print(linhas)
