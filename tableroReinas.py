#Ana Karla Garcia Gudiño
#David Olaf Menchaca Cruz
tablr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
lugar=[]
r = 0
pos=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def reinas(reina, tablr, r,pos):
    matrizini = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    n=0
    print("Reina",reina)
 
    if reina == 1:
        return resultante(tablr)
    else: 
        for x in range(len(tablr)):
            for r in range(len(tablr[x])):
                
                if n == 0:
					
                    if pos[x][r] != 3:
                        if(tablr[x][r] == 0):

                            if reina == 4:
                                pos[x][r] = 3
                            tablr[x][r] = 1
                            n = n +1
                            lugar.append([x,r])
        tablr = vh(tablr,lugar)
        lugar.pop(0)
        for x in tablr:
            if 0 in x:
                r = 0
            else:
                r = 1
        if r == 1:
            reina=4
            r=0
            print("Nueva llenado")
            return reinas(reina,matrizini,r,pos)
        if r == 0:
            reina=reina-1
            return reinas(reina,tablr,r,pos)
def vh(tablr,lugar):
    print("--------")
    e1 = lugar[0][0]
    y1 = lugar[0][1]
    r = range(len(tablr))
    uno = y1
    dos = e1
    print(lugar)
    for x in range(len(tablr)):
        for r in range(len(tablr[x])):
            tablr[e1][r] = 2
            tablr[x][y1] = 2
    #imp(tablr)
    for x in range(len(tablr)):
        uno = uno-1
        dos = dos -1
        if (uno >= 0)and(dos >=0):
            tablr[dos][uno] = 2
    uno = y1
    dos = e1
    for x in range(len(tablr)):
        dos = dos +1
        uno = uno +1
        if (dos <= r)and(uno <= r):
            tablr[dos][uno] = 2
    uno = y1
    dos = e1
    imp(tablr)
    for x in range(len(tablr)):
        uno = uno+1
        dos = dos -1
        if (uno < r)and(dos >=0):
            tablr[dos][uno] = 2
    uno = y1
    dos = e1
    
    for x in range(len(tablr)):
        uno = uno-1
        dos = dos + 1
        if (uno >= 0)and(dos <r):
            tablr[dos][uno] = 2
    tablr[e1][y1]=1
    imp(tablr)
    print("--------")
    return tablr

def resultante(tablr):
    for x in range(len(tablr)):
        for r in range(len(tablr[x])):
            if (tablr[x][r]) == 0:
                tablr[x][r] = 1
    print("Matriz Resultante")
    for x in tablr:
        print(x)

def imp(tablr):
    print("--------")
    for x in tablr:
        print(x)

reinas(4,tablr,0,pos)

