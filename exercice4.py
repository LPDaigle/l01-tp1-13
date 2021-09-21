import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    #calcul de l'acceleration
    acceleration = (vitesseFinale/3.6 - vitesseInitiale/3.6)/duree
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = positionInitiale + vitesseInitiale*duree/3.6 + 0.5*acceleration*(duree**2)

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
