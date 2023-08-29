from pilha import *
linhas = []
f = open("teste.txt","r")
for linha in f:
    linhas.append(linha.strip())
f.close()
#print(linhas)
tags = criarPilha()
for tag in linhas:
    if tag[1] != "/":
        empilhar(tags, tag)
    else:
        if ("<" + tag[2:]) in tags:
            empilhar(tags, tag)

print(tags)
            
