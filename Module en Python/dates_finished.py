#
# Fichier d'exemple pour travailler avec les dates
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Obtenir la date actuelle de la methode today de la classe Date
  today = date.today()
  print ("La date d'aujourd'hui est ", today)
  
  # Afficher individuellement les composants d'une date
  print ("Composant d'une date: ", today.day, today.month, today.year)
  
  # récupérer le jour de semaine d'aujourd'hui (0=lundi, 6=dimanche)
  print ("Le jour de ce semaine #: ", today.weekday())
  days = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
  print ("lequel est " + days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Obtenez la date du jour à partir de la classe datetime.
  today = datetime.now()
  print  ("La date et l'heure actuelles sont ", today)
  
  # Obtenir l'heure actuelle
  t = datetime.time(datetime.now())
  print ("Le temps actuel est ", t)
  
  
if __name__ == "__main__":
  main()
  