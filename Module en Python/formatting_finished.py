#
# Fichier d'exemple pour formatter l'affichage de la date et de l'heure
#

from datetime import datetime

def main():
  # Les heures et les dates peuvent être formatées à l'aide d'un ensemble de chaînes prédéfinies.
  # obtenir la date et l'heure actuelles
  now = datetime.now()
  
  #### Formattage de la Date  ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

  ## Année complète avec siècle
  print (now.strftime("L'année actuelle is: %Y"))


  ## jour abrégé, num, mois complet, année abrégée
  print (now.strftime("%a, %d %B, %y")) 
  
  ## %c - locale's date and time, %x - locale's date, %X - locale's time
  print (now.strftime("Locale date and time: %c"))
  print (now.strftime("Locale date: %x"))
  print (now.strftime("Locale time: %X"))
  
  #### Formattage Heure ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM

  ## 12-Hour:Minute:Second:AM
  print (now.strftime("Heure actuelle: %I:%M:%S %p")) 

  ## 24-Hour:Minute
  print (now.strftime("Heure Minute: %H:%M")) 


if __name__ == "__main__":
  main()
