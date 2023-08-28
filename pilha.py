def criarPilha():
    return []

def empilhar(p,valor):
    p.append(valor)

def desempilhar(p):
    return p.pop()

def mostrarPilha(p):
    print(p)

def topo(p):
    return p[-1]

def pilhaVazia(p):
    if len(p) == 0:
        return True
    return False
