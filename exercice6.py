import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):
    # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
    module = math.sqrt(nombreComplexe.real**2 + nombreComplexe.imag**2)
    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)
    print("Module:" + str(round(module,3)))
    print("Angle:" + str(round(angle,3)))

    # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'

    resultat = complex(nombreComplexe * complex(math.cos(math.radians(angle_rotation)), math.sin(math.radians(angle_rotation))))

    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)
    print("Nouveau module:" + str(round(nouveauModule,3)))
    print("Nouvel angle:" + str(round(nouvelAngle,3)))
    print(resultat)

    return resultat


def dessiner(number, label): 
    ax = plt.subplot(projection='polar') 
    if number != None: 
        ax.plot([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
