#
# Fichier d'exemple de travail avec le module os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Afficher le nom de l'OS
  print (os.name)
  
  # Verification de l'existence d'un element et de son tyoe
  print ("L'element existe: " + str(path.exists("textfile.txt")))
  print ("L'element est un fichier: " + str(path.isfile("textfile.txt")))
  print ("L'element est un repertoire: " + str(path.isdir("textfile.txt")))
  
  # Manipuler les informations sur le chemin du fichier avec file paths
  print ("Le chemin du fichier: " + str(path.realpath("textfile.txt")))
  print ("Le chemin du fichier et sa designation: " + str(path.split(path.realpath("textfile.txt"))))
  
  # Obtenir la date de modification du fichier
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Caclucler le temps écoulé depuis la dernière modification
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("Il s'est passé " + str(td) + " depuis la dernière modification")
  print ("Ou, " + str(td.total_seconds()) + " secondes")

if __name__ == "__main__":
  main()
