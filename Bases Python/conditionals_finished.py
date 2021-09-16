#
# Fichier d'Exemple pour les structures conditionnelles
#


def main():
    x, y = 10, 100

    # flow conditionel utilisant if, elif, else
    if(x < y):
        st = "x est petit que y"
    elif (x == y):
        st = "x égale à y"
    else:
        st = "x est plus grand que y"
    print(st)

    # conditional statements te permet de  faire "a if C else b"
    st = "x est petit que y" if (x < y) else "x iest plus grand que y"
    print(st)

    #Instruction imbriquée
    age1,age2 = 10, 100
    nom, ville = "Sion", "Kinshasa"
    if (age1 > 10):
        if (nom == "Sion"):
            print("I Got IT")
        else:
            print("No Got")
    else:
        print("Out of 10")

    


if __name__ == "__main__":
    main()
