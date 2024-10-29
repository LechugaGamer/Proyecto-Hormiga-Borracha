import algoritmo_genético

Alelos = {"arriba":  [-1,0], 
          "abajo":  [1,0],
          "derecha": [0,1],
          "izquierda": [1,0],
          "comer": "comer"}


alelos_keys = list(Alelos.keys()) #para llamar a los alelos

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
def encontrar_pos(matriz, elemento):

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == elemento:
                return [columna, fila] #posición del elemento en la fila, es basicamente para el inicio  [x,y]
            
start = encontrar_pos(laberinto, "s")
exit = encontrar_pos(laberinto, "e")

adn_i_1 = [random.choice(alelos_keys)]
adn_i_2 = [random.choice(alelos_keys)]

class Hormiga:
    def __init__(self, posicion, salud, alcohol_lvl, puntos, adn):

        self.posicion = posicion #debe ser una lista, aquí ponemos donde inicia
        self.salud = salud 
        self.alcohol_lvl = alcohol_lvl
        self.puntos = puntos 

        self.adn =  adn

    def get_info(self):

        return [self.posicion, self.salud, self.alcohol_lvl, self.puntos, self.adn]

    def mover(self, alelo):


        if ( 0 <= Alelos[alelo][0] + self.posicion[0] < len(laberinto[0]) and 0 <= Alelos[alelo][1] + self.posicion[1] < len(laberinto) 
                ):

            if  laberinto[Alelos[alelo][1] + self.posicion[1]][Alelos[alelo][0] + self.posicion[0]] != "r":

                
                if laberinto[self.posicion[1]][self.posicion[0]] == "p": 
                    print("La hormiga a ignorado al veneno")
                
                if laberinto[self.posicion[1]][self.posicion[0]] == "s": 
                    print("La hormiga a ignorado al azucar")

                if laberinto[self.posicion[1]][self.posicion[0]] == "a": 
                    print("La hormiga a ignorado al alcohol")
                #para decir que no comió y avanzó

                self.posicion[1] += Alelos[alelo][1]
                self.posicion[0] += Alelos[alelo][0] #aquí cambiamos el self para actualizar la posición de la hormiga hasta su final
    def comer(self):
        
        casilla = laberinto[self.posicion[1]][self.posicion[0]]

        if casilla == "p":
            #interactua con poison
            pass
        if casilla == "s":
            #interactua con sugar
            pass
        if casilla == "a":
            #interactua con alcohol
            pass

    def modifica_salud(self):
        casilla = laberinto[self.posicion[1]][self.posicion[0]]

        if casilla == "p":
            #poison la mata
            pass
        if casilla == "a":
            #alcohol le quita 10 puntos de salud
            pass

h1 = Hormiga(start, 100, 0, 0, adn_i_1)
h2 = Hormiga(start, 100, 0, 0, adn_i_2)

Poblacion = [h1, h2]

def main ():
    while True:
        n=0
        for hormiga in Poblacion:
            n+=1
            with open("puntajes-hormiga.txt", "w") as text:
                text.write(f"Hormiga:{n}_Salud:{hormiga.get_info()[1]}_")
