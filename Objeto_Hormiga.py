import random
from Objeto_veneno import Veneno

Alelos = {"arriba":  [0,-1], 
          "abajo":  [0,1],
          "derecha": [1,0],
          "izquierda": [-1,0],
          "comer": "comer"}


alelos_keys = list(Alelos.keys()) #para llamar a los alelos

veneno = Veneno()

class Hormiga:
    def __init__(self, posicion, salud, alcohol_lvl, puntos, adn, laberinto):

        self.posicion = posicion.copy() #debe ser una lista, aquí ponemos donde inicia
        self.salud = salud 
        self.alcohol_lvl = alcohol_lvl
        self.puntos = puntos 
        self.laberinto = laberinto

        self.adn =  adn

    def get_info(self):

        return [self.posicion, self.salud, self.alcohol_lvl, self.puntos, self.adn]
    
    def add_pts(self, puntos):

        self.puntos += puntos
    def change_adn(self, pos, valor):

        print(f"Sin cambio {self.adn}")
        self.adn[pos] = valor
        print("cambia adn")
        print(f"Sí cambió {self.adn}")


    def mover(self, alelo):


        if (0 <= Alelos[alelo][0] + self.posicion[0] < len(self.laberinto[0]) and 0 <= Alelos[alelo][1] + self.posicion[1] < len(self.laberinto) 
                ):

            if  self.laberinto[Alelos[alelo][1] + self.posicion[1]][Alelos[alelo][0] + self.posicion[0]] != "r":

                
                if self.laberinto[self.posicion[1]][self.posicion[0]] == "p": 
                    print("La hormiga a ignorado al veneno")
                
                if self.laberinto[self.posicion[1]][self.posicion[0]] == "g": 
                    print("La hormiga a ignorado al azucar")

                if self.laberinto[self.posicion[1]][self.posicion[0]] == "a": 
                    print("La hormiga a ignorado al alcohol")
                #para decir que no comió y avanzó

                self.posicion[1] = self.posicion[1] + Alelos[alelo][1]
                self.posicion[0] = self.posicion[0] + Alelos[alelo][0] #aquí cambiamos el self para actualizar la posición de la hormiga hasta su final
            else:
                print("Topó con roca (-20 pts)")
                self.puntos -= 20
                
        else:
            print("Intentó salir de la frontera (-20 pts)")
            self.puntos -= 20
            

    def comer(self):
        
        casilla = self.laberinto[self.posicion[1]][self.posicion[0]]

        if casilla == "p":

            self.salud += veneno.consumir()

        elif casilla == "s":
            #interactua con sugar
            pass
        elif casilla == "a":
            #interactua con alcohol
            pass
        else:
            print("La hormiga intentó comer donde no había comida (-30 pts)")
            self.puntos -= 30
            
        
    def modifica_salud(self):
        casilla = self.laberinto[self.posicion[1]][self.posicion[0]]

        if casilla == "p":
            #poison la mata
            pass
        if casilla == "a":
            #alcohol le quita 10 puntos de salud
            pass
    def fitness(self):
        return abs(exit[0]-self.posicion[0]) + abs(exit[1] - self.posicion[1])

    
    def muta(self): 

        for i in range(len(self.adn)):

            muta = random.randint(0,1)

            if muta == 1:
                new_adn = random.choice(alelos_keys)
                print(f"La hormiga ha mutado y cambió {self.adn[i]} por {new_adn}")
                self.adn[i] = new_adn
        
        for alelo in range(len(self.adn)):
            muta = random.randint(0,20)

            if muta == 20:
                print("La hormiga ha mutado y obtuvo un alelo")
                self.adn.append(random.choice(alelos_keys))
    
