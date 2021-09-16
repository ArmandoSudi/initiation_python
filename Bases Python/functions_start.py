#
# Fichier exemple pour les fonctions
#

# Ecrire une fonction basique

def fonction1():
    print("Je suis dans la fonction 1")




# Fonction qui prennent plusieurs arguments

def somme(val1, val2):
    somme = val1 + val2
    print("Somme", somme )

# Fonction qui retourne une valeur

def somme2(val1, val2):
    somme = val1 + val2
    return somme

def cube(val1):
    return val1 ** 3
    




# Fonction avec une valeur par défaut dans ses arguments
def puissance(nombre,exposant = 1, valeur = 3):
    return nombre ** exposant

    


# fonction avec un nombre variable des arguments
def somme_multiple(*args):
    somme = 0
    for x in args:
        somme = somme + x
    return somme

resultat = somme2(40,50)
resultat2 = cube(5)
resultat3 = puissance(5, 5)
print(somme_multiple(5,15,30,45,90,100))
