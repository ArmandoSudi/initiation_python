#
# Fichier exemple pour les fonctions
#

# Ecrire une fonction basique


def func1():
    print("Je suis une fonction")


# Fonction qui prennent plusieurs arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# Fonction qui retourne une valeur


def cube(x):
    return x*x*x


# Fonction avec une valeur par défaut dans ses arguments


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result



# fonction avec un nombre variable des arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result



# Variables locales vs variables globales

def someFunction():
  #global a
  a = "deal"
  print (a)




func1()
print(func1())
print(func1)
func2(10, 20)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))
