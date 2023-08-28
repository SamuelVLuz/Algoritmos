from fila import *

time = ["A", "B", "C", "D", "E"]

loop = True

while loop:
    le = time[0]
    ld = time[1]

    je, jd = map(int, input("Pontuação: Time %s, Time %s " %(le, ld)).split())
        
    if je > jd:
        enfileirar(time, ld)
        time.pop(1)
        print("Jogador da esquerda, %s ganhou" % le)
        
    elif je < jd:
        enfileirar(time, le)
        desenfileirar(time)
        le = time[1]
        time.pop(1)
        time.insert(0,le)
        print("Jogador da direita, %s ganhou" % ld)
        
    else:
        loop = False
    
    
