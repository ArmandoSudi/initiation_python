#
# Fichier d'exemple pour les classes for working with classes
#

from typing import Reversible


class myClass(object):
   roues = 2
   def method1(self):
      self.roues = 4
      print("methode 1")
   
   def method2(self):
      print("methode 2")


class Velo:
   
   def __init__(self, marque, prix, poids, roues = 2):
      self.marque = marque
      self.prix = prix
      self.poids = poids
      self.roues = roues
   
   def rouler(self):
      print("Wouh, ça roule mieux avec un velo {0}".format(self.marque))

class str:
   def upper():
      print("majuscule")

class Rectangle:
   L = 0
   l = 0
   nom = ""

   "Classe Rectangle"
   def __init__(self, longeur = 0, largeur = 0):
      self.L = longeur
      self.l = largeur
      self.nom = "rectangle"
   
   def perimetre(self):
      return self.L * 2 + self.l * 2
   
   def surface(self):
      return self.L * self.L
   


class Employe:
   nom = ""
   prenom = ""
   age = ""
   salaire = ""

   def __init__(self,firstname, lastname, age, salary = 0):
      self.nom  = lastname
      self.prenom = firstname
      self.age = age
      self.salaire = salary
   




#Class avec COnstructeur


def main():
   
   unemploye = Employe("Sion", "Israel", "5000")
   deuxemploye = Employe("Alvarez", "Alj", "50", 5000)
   

   


if __name__ == "__main__":
    main()
