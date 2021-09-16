#
# Fichier d'Exemple pour les structures conditionnelles
#


def main():
    x, y = 10, 100

    # flow conditionel utilisant if, elif, else
    if (x > y):
        print("x est plus grand que y")
    elif (x == y):
        print("x es égale à y")
    else:
        print("x est plus petit que y")
    
   


   

    # conditional statements te permet de  faire "a if C else b"
    print("x est plus petit que y" if (x < y) else "x est plus grand que y")

    age1, age2 = 10, 100
    ville1, ville2 = "Paris", "Lyon"
    if (age1 > age2):
        if ville1 == "Paris":
            print("Cas 1")
        elif ville2 == "Lyon":
            print("Cas 2")
    else:
        print('Cas General')



    


if __name__ == "__main__":
    main()
