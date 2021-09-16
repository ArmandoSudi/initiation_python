#
# Fichier d'exemple pour les classes for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")

    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")


#Class avec COnstructeur
class Velo:
    roues = 2

    def __init__(self, marque, prix, poids):
        self.marque = marque
        self.prix = prix
        self.poids = poids

    def rouler(self):
        print("Wouh, ça roule mieux avec un vélo {} !".format(self.marque))





def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()


if __name__ == "__main__":
    main()


#### Exercice Rectangle
'''class Rectangle(object): 
    "Classe de rectangles" 
    def __init__(self, longueur =0, largeur =0): 
        self.L = longueur 
        self.l = largeur 
        self.nom ="rectangle" 
    def perimetre(self): 
        return "({0:d} + {1:d}) * 2 = {2:d}".\ 
        format(self.L, self.l, (self.L + self.l)*2) 
    def surface(self): 
        return "{0:d} * {1:d} = {2:d}".format(self.L, self.l, self.L*self.l) 
    def mesures(self): 
        print("Un {0} de {1:d} sur {2:d}".format(self.nom, self.L, self.l)) 
        print("a une surface de {0}".format(self.surface())) 
        print("et un périmètre de {0}\n".format(self.perimetre())) 
class Carre(Rectangle): 
    "Classe de carrés" 
    def __init__(self, cote): 
        Rectangle.__init__(self, cote, cote) 
        self.nom ="carré" 

if __name__ == "__main__": 
    r1 = Rectangle(15, 30) 
    r1.mesures() 
    c1 = Carre(13) 
    c1.mesures() '''