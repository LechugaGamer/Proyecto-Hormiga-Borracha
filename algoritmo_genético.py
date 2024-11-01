import random
import time
import Objeto_Hormiga as h

Alelos = {"arriba":  [0,-1], 
          "abajo":  [0,1],
          "derecha": [1,0],
          "izquierda": [-1,0],
          "comer": "comer"}

###NO VER
###NO VER
##ES COMO UNA CLASE DE REPALDO MAL HECHO, NO VER
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


Poblacion = [h.Hormiga(start, 100, 0, 0, adn_i_1), h.Hormiga(start, 100, 0, 0, adn_i_2)]


def cruce(adn1, adn2):

    print(f"Inicio de cruce: {start}")
    if not adn1 or not adn2:
        return []
    adn_hijo = []
    
    for i in range(max(len(adn1), len(adn2))):
        
        if random.choice([True, False]): #si es True ejecuta
            if i < len(adn1):
                adn_hijo.append(adn1[i])

                if random.choice([True, False]):
                    if i < len(adn2):
                        adn_hijo.append(adn2[i])

        else: #sino no
            if i < len(adn2):
                adn_hijo.append(adn2[i])

                if random.choice([True, False]):
                    if i < len(adn1):
                        adn_hijo.append(adn1[i])


    
    

    
    hormiga_hija = h.Hormiga(start, 100, 0, 0, adn_hijo)
    return hormiga_hija
                   

def run():
    global Poblacion

    with open("puntajes-hormiga.txt", "w") as text:
        pass

    
    while True:
        
        

        for hormiga in Poblacion: #cambia los atributos del objeto
            adn = hormiga.get_info()[4]

            for alelo in adn:
                if alelo != "comer":
                    
                    hormiga.mover(alelo)
                    
                else:
                    hormiga.comer()
            
            fitness = hormiga.fitness()

            

            if fitness == 0:
                hormiga.add_pts(100)
                print("\n")
                print("la hormiga ha llegado a la meta")
                print("\n")
            
            else:
                print("\n")
                hormiga.add_pts(-5*fitness)
                print(f"la hormiga quedó a una distancia relativa de {fitness} ({-5*fitness}pts)")
                print("\n")
                
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

        #ya metidas en el txt(ya evaluadas), procedo a cruzar las mejores dos

        with open("puntajes-hormiga.txt", "r") as text:
            lines = text.readlines()

            adnh1 = encuentre_datos(lines[0], "ADN:")
            adnh2 = encuentre_datos(lines[1], "ADN:")

                    
        hormiga_hija = cruce(adnh1, adnh2)

        print(hormiga_hija.get_info())
        

        hormiga_hija.muta()


        Poblacion = [hormiga_hija] #esta lista se modifica para que tenga sentido en el código, pues evalua las hormigas in Poblacion

        option = input("<s> para salir, <any oter key> para la siguiente simulación")
        #esto for debbug, pero ya después lo quitamos
        if option == "s":
            break
        

        
                    

        
            
            
            
        
            

            


def encuentre_datos(linea, etiqueta):
    
    inicio = linea.find(etiqueta)
    inicio += len(etiqueta) 

    final = linea.find("_", inicio)

    if etiqueta == "ADN:":
        dato = linea[inicio:final].strip()  # Eliminar espacios en blanco

        # Si el dato está en formato de lista (por ejemplo, "['comer']"), convertirlo en una lista
        if dato.startswith("[") and dato.endswith("]"):
            dato = dato[1:-1].replace("'", "").strip()
            return [d.strip() for d in dato.split(",")]  # Devolver una lista de alelos
        else:
            return [dato]  # Retornar como lista de un solo elemento
    

    return linea[inicio:final]

run()