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

Alelos = {"arriba":  [-1,0], 
          "abajo":  [1,0],
          "derecha": [0,1],
          "izquierda": [1,0],
          "comer": "comer"}
alelos_keys = list(Alelos.keys())

Puntos_general = {"e": 100,
          " " : 10,
          "a" : -20,
          "s" : 30,
          "p" : "muerte" #la mata, la elimina directamente, se cruzan las dos mejores
}


def algoritmo_principal(matriz):
    pass

#para saber numéricamente la posición de la hormiga

def encontrar_pos(matriz, elemento):

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == elemento:
                return [fila, columna] #posición del elemento en la fila, es basicamente para el inicio 
            
start = encontrar_pos(laberinto, "s")
exit = encontrar_pos(laberinto, "e")
def action(al):
    return Alelos[al]

def adn_i (): 
    return [random.choice(alelos_keys)] #retorna una lista con un alelo incial

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




"""
Para uno de los parámetros del fitness, voy a utilizar la distancia del taxista:
es el valor absoluto de la suma de la diferencia de las coordenadas entre dos puntos.
En este caso, la hormiga y la salida.
Si la distancia es cero, ese es el mejor caso para este parámetro.

Otro va a ser la cantidad de puntos de azucar, entre más mejor.

Otro va a ser la cantidad de puntos de alcohol, entre menos mejor.

Y si come veneno directamente se muere XD.
"""


print(adn_i())