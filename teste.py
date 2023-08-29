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
        if topo(tags)[1:] == tag[2:]:
            desempilhar
        else:
            print("ERRO: tag de fechamento não esperada (%s)" % (tag))
            break

            
