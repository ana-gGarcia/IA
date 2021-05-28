#Ana Karla Garcia Gudiño
#David Olaf Menchaca Cruz
import json
with open ("caballos.json","r") as read_file:
	data = json.load(read_file)
	Conocimiento = data['conocimiento']
	
tabla = [[-1,0,-1],[0,0,0],[1,0,1]]
tba = [[1,0,1],[0,0,0],[-1,0,-1]]
tablero = [[0,1,2],[3,4,5],[6,7,8]]

def caballos(matrizini,mtzfin,mov):
	matriz=[[0,0,0],[0,0,0],[0,0,0]]
	i = 0
	while(i < 3):
		j = 0
		while(j < 3):
			if (matrizini[i][j] != 0):
				paso = matrizini[i][j]
				matrizini[i][j] = 0
				girar(i,j,paso,matriz,mov)
			j +=1
		i +=1
	for e in matriz:
		print (e)
	print ("")
	if (matriz != tabla):
		return caballos(matriz,mtzfin,mov)

def girar(e1,e2,paso,ta,p):
	ca = tablero[e1][e2]
	for e in Conocimiento:
		if (ca == e[0]):
			i = 0
			while(i <= 2):
				j = 0
				while(j <= 2):
					if (tablero[i][j] == e[p]):
						ta[i][j] = paso
						return ta
					j += 1
				i += 1

caballos(tba,tabla,1)
