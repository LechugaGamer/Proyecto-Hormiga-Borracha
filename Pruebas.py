import random

def cruce(adn1, adn2):
    if not adn1 or not adn2:
        return []
    adn_hijo = []
    
    for i in range(max(len(adn1), len(adn2))):
        
        if random.choice([True, False]): #si es True ejecuta
            if i < len(adn1):
                adn_hijo.append(adn1[i])
        else: #sino no
            if i < len(adn2):
                adn_hijo.append(adn2[i])

    return adn_hijo

# Ejemplo de uso
adn1 = ["comer", "abajo"]
adn2 = ["derecha", "comer"]

resultado = cruce(adn1, adn2)
print(resultado)

