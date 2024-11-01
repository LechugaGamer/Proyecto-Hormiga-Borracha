import random
import time
from Objeto_veneno import Veneno

Alelos = {"arriba":  [0,-1], 
          "abajo":  [0,1],
          "derecha": [1,0],
          "izquierda": [-1,0],
          "comer": "comer"}


alelos_keys = list(Alelos.keys()) #para llamar a los alelos



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

Matriz = crear_mat(3,3)

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

veneno = Veneno()

class Hormiga:
    def __init__(self, posicion, salud, alcohol_lvl, puntos, adn):

        self.posicion = posicion.copy() #debe ser una lista, aquí ponemos donde inicia
        self.salud = salud 
        self.alcohol_lvl = alcohol_lvl
        self.puntos = puntos 

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


        if (0 <= Alelos[alelo][0] + self.posicion[0] < len(laberinto[0]) and 0 <= Alelos[alelo][1] + self.posicion[1] < len(laberinto) 
                ):

            if  laberinto[Alelos[alelo][1] + self.posicion[1]][Alelos[alelo][0] + self.posicion[0]] != "r":

                
                if laberinto[self.posicion[1]][self.posicion[0]] == "p": 
                    print("La hormiga a ignorado al veneno")
                
                if laberinto[self.posicion[1]][self.posicion[0]] == "g": 
                    print("La hormiga a ignorado al azucar")

                if laberinto[self.posicion[1]][self.posicion[0]] == "a": 
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
        
        casilla = laberinto[self.posicion[1]][self.posicion[0]]

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
        casilla = laberinto[self.posicion[1]][self.posicion[0]]

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
    
Poblacion = [Hormiga(start, 100, 0, 0, adn_i_1), Hormiga(start, 100, 0, 0, adn_i_2)]

def cruce(adn1, adn2):

    print(f"Inicio de cruce: {start}")
    if not adn1 or not adn2:
        return []
    adn_hijo = []
    
    for i in range(max(len(adn1), len(adn2))):
        mutacion = random.randint(0,3)
        if mutacion == 1: #si es 1 toma el alelo de padre 1
            if i < len(adn1):
                adn_hijo.append(adn1[i])

                if random.choice([True, False]): #si es true también toma el alelo de padre 2
                    if i < len(adn2):
                        adn_hijo.append(adn2[i])

        elif mutacion==2: #si es dos toma el alelo de padre 2
            if i < len(adn2):
                adn_hijo.append(adn2[i])

                if random.choice([True, False]): #si es True también toma el alelo de padre 1
                    if i < len(adn1):
                        adn_hijo.append(adn1[i])
        
        #si es 3, nada pasa, o sea no toma ningún alelo


    
    

    print(type(adn_hijo))
    hormiga_hija = Hormiga(start, 100, 0, 0, adn_hijo)
    return hormiga_hija

def encuentre_datos(linea, etiqueta):
    
    inicio = linea.find(etiqueta)
    inicio += len(etiqueta) 

    final = linea.find("_", inicio)

    if etiqueta == "ADN:": #Esto porque ADN siempre es una lista y para efectos de este código ponerlo aparte es muy útil
        dato = linea[inicio:final].strip()  # Eliminar espacios en blanco

        if dato.startswith("[") and dato.endswith("]"): # Si el dato está en formato de lista, convertirlo en una lista
            
            dato = dato[1:-1].replace("'", "").strip()
            return [d.strip() for d in dato.split(",")]  # Devolver una lista de alelos
        else:
            return [dato]  # Retornar como lista de un solo elemento
    

    return linea[inicio:final]  #si no es ADN, retorna string, pues lo que se escribe es str            

def algoritmo_genetico(): #corre el algoritmo genetico

    global Poblacion    
        
    for hormiga in Poblacion:
        
        adn = hormiga.get_info()[4]
        

        for alelo in adn:

            
            if alelo != "comer":
                
                pre_fitness = hormiga.fitness()

                hormiga.mover(alelo) #cambia los atributos del objeto

                post_fitness = hormiga.fitness()

                if post_fitness <= pre_fitness:
                    print("La hormiga hizo un movimiento óptimo (+20 pts)")
                    hormiga.add_pts(20)
                else:
                    print("La hormiga hizo un movimiento NO óptimo (-30 pts)")
                    hormiga.add_pts(-30)
            else:

                hormiga.comer()

                salud = hormiga.get_info()[1]

                if salud <= 0:
                    print("La hormiga ha muerto :(")
                    break

       
                    
        salud = hormiga.get_info()[1] 

        if salud > 0:
            fitness = hormiga.fitness()

            

            if fitness == 0:
                hormiga.add_pts(100)
                print("la hormiga ha llegado a la meta")
                
            else:
                hormiga.add_pts(-5*fitness)
                print(f"la hormiga quedó a una distancia relativa de {fitness} ({-5*fitness}pts)")
                
            print("Hormiga resultados:", hormiga.get_info())

        else:

            Poblacion.remove(hormiga)

    if Poblacion:
        for hormiga in Poblacion: #para meterlas despues de modificarlas (evalua su puntaje)

            with open("puntajes-hormiga.txt", "r") as text:

                lines = text.readlines()
                
                if not lines: #si no hay nada
                    lines = []
                    
                        
                    lines.append(f"HORMIGA:1_SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                    
                
                elif len(lines) == 1:
                    puntos = int(encuentre_datos(lines[0], "PUNTOS:"))
                    if hormiga.get_info()[3] > puntos:
                        lines.append(f"HORMIGA:2_SALUD:{encuentre_datos(lines[0], "SALUD:")}_ALCOHOL:{encuentre_datos(lines[0], "ALCOHOL:")}_PUNTOS:{encuentre_datos(lines[0], "PUNTOS:")}_ADN:{encuentre_datos(lines[0], "ADN:")}_" + "\n")
                        lines[0] = f"HORMIGA:1_SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n"
                    else:
                        lines.append(f"HORMIGA:2_SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")

                elif len(lines) == 2:
                    puntos_hormiga = hormiga.get_info()[3]
                    puntos_linea_1 = int(encuentre_datos(lines[0], "PUNTOS:"))
                    puntos_linea_2 = int(encuentre_datos(lines[1], "PUNTOS:"))

                    if puntos_hormiga > puntos_linea_1:
                        linea1 = lines[0]
                        linea2 = lines[1]
                        
                        lines[0] = lines[0].replace(f"{linea1.split('HORMIGA:1_')[1]}", f"SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                        lines[1] = lines[1].replace(f"{linea2.split('HORMIGA:2_')[1]}", f"SALUD:{encuentre_datos(linea1, "SALUD:")}_ALCOHOL:{encuentre_datos(linea1, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea1, "PUNTOS:")}_ADN:{encuentre_datos(linea1, "ADN:")}_" + "\n")
                        lines.append(f"HORMIGA:3_SALUD:{encuentre_datos(linea2, "SALUD:")}_ALCOHOL:{encuentre_datos(linea2, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea2, "PUNTOS:")}_ADN:{encuentre_datos(linea2, "ADN:")}_" + "\n")
                    elif puntos_hormiga > puntos_linea_2:
                        linea2 = lines[1]
        
                        lines[1] = lines[1].replace(f"{linea2.split('HORMIGA:2_')[1]}", f"SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                        lines.append(f"HORMIGA:3_SALUD:{encuentre_datos(linea2, "SALUD:")}_ALCOHOL:{encuentre_datos(linea2, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea2, "PUNTOS:")}_ADN:{encuentre_datos(linea2, "ADN:")}_" + "\n")

                    else:
                        lines.append(f"HORMIGA:3_SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                else:

                    puntos_hormiga = hormiga.get_info()[3]
                    puntos_linea_1 = int(encuentre_datos(lines[0], "PUNTOS:"))
                    puntos_linea_2 = int(encuentre_datos(lines[1], "PUNTOS:"))
                    puntos_linea_3 = int(encuentre_datos(lines[2], "PUNTOS:"))

                    if puntos_hormiga > puntos_linea_1:
                        linea1 = lines[0]
                        linea2 = lines[1]
                        linea3 = lines[2]

                        lines[0] = lines[0].replace(f"{linea1.split('HORMIGA:1_')[1]}", f"SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                        lines[1] = lines[1].replace(f"{linea2.split('HORMIGA:2_')[1]}", f"SALUD:{encuentre_datos(linea1, "SALUD:")}_ALCOHOL:{encuentre_datos(linea1, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea1, "PUNTOS:")}_ADN:{encuentre_datos(linea1, "ADN:")}_" + "\n")
                        lines[2] = lines[2].replace(f"{linea3.split('HORMIGA:3_')[1]}", 
                                            f"SALUD:{encuentre_datos(linea2, "SALUD:")}_ALCOHOL:{encuentre_datos(linea2, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea2, "PUNTOS:")}_ADN:{encuentre_datos(linea2, "ADN:")}_" + "\n")
                    elif puntos_hormiga > puntos_linea_2:
                        linea2 = lines[1]
                        linea3 = lines[2]
        
                    
                        lines[1] = lines[1].replace(f"{linea2.split('HORMIGA:2_')[1]}", f"SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")
                        lines[2] = lines[2].replace(f"{linea3.split('HORMIGA:3_')[1]}", 
                                            f"SALUD:{encuentre_datos(linea2, "SALUD:")}_ALCOHOL:{encuentre_datos(linea2, "ALCOHOL:")}_PUNTOS:{encuentre_datos(linea2, "PUNTOS:")}_ADN:{encuentre_datos(linea2, "ADN:")}_" + "\n")
                    elif puntos_hormiga > puntos_linea_3:
                        linea3 = lines[2]
                        lines[2] = lines[2].replace(f"{linea3.split('HORMIGA:3_')[1]}", 
                                            f"SALUD:{hormiga.get_info()[1]}_ALCOHOL:{hormiga.get_info()[2]}_PUNTOS:{hormiga.get_info()[3]}_ADN:{hormiga.get_info()[4]}_" + "\n")     

                    else:
                        print("la hormiga no entra en el top 3")

        with open("puntajes-hormiga.txt", "w") as text: 
            text.writelines(lines)  


def se_cruzan ():

    global Poblacion

    with open("puntajes-hormiga.txt", "r") as text:
        lines = text.readlines()
        #Selección
    if not lines:
        print("no hay hormigas, vamos a meter dos más")
        Poblacion = [Hormiga(start, 100, 0, 0, [random.choice(alelos_keys)]), Hormiga(start, 100, 0, 0, [random.choice(alelos_keys)])]

    elif len(lines) == 1:
        print("solo queda una hormiga, vamos a meter una más")
        Poblacion = [Hormiga(start, 100, 0, 0, [random.choice(alelos_keys)])]
    
    else:
        
        adnh1 = encuentre_datos(lines[0], "ADN:")
        adnh2 = encuentre_datos(lines[1], "ADN:")

        #cruzamiento            
        hormiga_hija = cruce(adnh1, adnh2)

        hormiga_hija.muta()

        print("Hormiga Hija:", hormiga_hija.get_info())

        Poblacion = [hormiga_hija] #esta lista se modifica para que tenga sentido en el código, pues evalua las hormigas in Poblacion

def intento():

    global Poblacion

    with open("puntajes-hormiga.txt", "w") as text: #borra todo para comenzar
        pass

    gen = 1

    while True:


        gen+=1
        if Poblacion:

            algoritmo_genetico()
            se_cruzan()
        else:

            print("no hay hormigas, vamos a meter dos más")
            Poblacion = [Hormiga(start, 100, 0, 0, [random.choice(alelos_keys)]), Hormiga(start, 100, 0, 0, [random.choice(alelos_keys)])]


        with open("puntajes-hormiga.txt", "r") as text:
            lines = text.readlines()
            if lines:
                if int(encuentre_datos(lines[0], "PUNTOS:")) >= 180:
                    break
        #option = input("<s> para salir, <any oter key> para la siguiente simulación")
        #esto for debbug, pero ya después lo quitamos
        #if option == "s":
            #break

    print(f"Numero de generaciones: {gen}")


    

intento()
