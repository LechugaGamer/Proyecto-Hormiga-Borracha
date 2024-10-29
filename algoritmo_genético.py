import random

#For debbug:
#quiero tener una matriz visual en la que trabajar, por eso lo hice así

def crear_mat(i,j):
    mat = []
    for fila in range(i):
        mat.append([])
    for fila in range(i):
        for columna in range(j):
            mat[fila].append("")
    return mat

Matriz = crear_mat(5,5)

def agregar_matriz(matriz):
    while True:
        estructura = input("Debug option: ") #f para finish
        

        if estructura == "f":
            break
        
        fila = int(input("fila: "))
        columna = int(input("columna: "))

        if (estructura == "w" or estructura == "r" or estructura == "p" or
        estructura == "g" or estructura == "s" or estructura == "e" or estructura == ""):
            matriz[fila][columna] = estructura

        print("\nEstado actual del laberinto:")
        for fila in matriz:
            print(fila)
    return matriz

laberinto = agregar_matriz(Matriz)
"""
Debug options:

r: rock
p: poison
g: glucose
s: start
e: exit
a: alcohol
"":empty

"""


####

#algoritmo main:

#la población se guarda en puntajes-hormiga

Alelos = {"arriba":  [-1,0], 
          "abajo":  [1,0],
          "derecha": [0,1],
          "izquierda": [1,0],
          "comer arriba": "comer",
          "comer abajo": "comer",
          "comer derecha": "comer",
          "comer izquierda": "comer"}

alelos_keys = list(Alelos.keys()) #para llamar a los alelos

Puntos_general = {"e": 100,
          " " : 10,
          "a" : -20,
          "s" : 30,
          "p" : "muerte" #la mata, la elimina directamente, se cruzan las dos mejores
          #si no hay dos mejores se genera una nueva
}


def algoritmo_principal(matriz, hormiga):
    h_i_1 = crear_hormiga()
    h_i_2 = crear_hormiga()
    

#para saber numéricamente la posición de la hormiga

def encontrar_pos(matriz, elemento):

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == elemento:
                return [fila, columna] #posición del elemento en la fila, es basicamente para el inicio 
            
start = encontrar_pos(laberinto, "s")
exit = encontrar_pos(laberinto, "e")

def adn_i ():  
    return [random.choice(alelos_keys)] #retorna una lista con un alelo incial
    #básicamente, genera a la hormiga, pero no es la hormiga
    #porque esta tiene puntos y esas cosas

def crear_hormiga(): #método del objeto, pero hay que hacer el objeto a parte
    
    adn = adn_i()
    with open("puntajes-hormiga.txt", "w") as text:
        num = 0
        for line in text:
            num+=1
        text.write(f"{num+1} _ ADN:{adn} _ AZUCAR:0 _ ALCOHOL:0 _DISTANCIA:0_PUNTUACION:0")

def mutacion(adn):

    for alelo in adn:
        muta = random.randint(0,10)

        if muta == 10:
            print("La hormiga ha mutado")
            alelo = random.choice(alelos_keys)
    
    for alelo in range(adn):
        muta = random.randint(0,20)

        if muta == 20:
            print("La hormiga ha mutado")
            adn.append(random.choice(alelos_keys))
    
    return adn #retorna la lista con alguna mutación o sin ella




"""
Para uno de los parámetros del fitness, voy a utilizar la distancia del taxista:
es el valor absoluto de la suma de la diferencia de las coordenadas entre dos puntos.
En este caso, la hormiga y la salida.
Si la distancia es cero, ese es el mejor caso para este parámetro.

Otro va a ser la cantidad de puntos de azucar, entre más mejor.

Otro va a ser la cantidad de puntos de alcohol, entre menos mejor.

Y si come veneno directamente se muere XD.
"""

def comer(dirección, matriz, x, y):
    if dirección == "comer arriba":
        pass

def accion_objetos(matriz, x, y):
    if matriz[y][x] == "p":
        print("La hormiga ha ingerido veneno y ha muerto")
        #habrá un método que la mate
    
    elif matriz[y][x] == "s":
        print(f"La hormiga ha ingerido azucar, gana {Puntos_general["s"]} puntos")
###
###
##
###
###
##

    

def fitness(matriz, adn):
    global start, exit

    xi = start[0]
    yi = start[1]

    xf= exit[0]
    yf= exit[1]
    
    x_actual = xi
    y_actual = xi

    puntos_azucar = 0
    puntos_alcohol = 0

    distancia_rel = 0

    for alelo in adn:

        if ( 0 <= Alelos[alelo][0] + x_actual < len(matriz[0]) and 0 <= Alelos[alelo][1] + y_actual < len(matriz) 
            ):

            if Alelos[alelo] != "comer" and matriz[Alelos[alelo][1] + y_actual][Alelos[alelo][0] + x_actual] != "r":

           
                x_actual += Alelos[alelo][0]
                y_actual += Alelos[alelo][0] 

            if Alelos[alelo] == "comer":

                comer(alelo, matriz, x_actual, y_actual)

