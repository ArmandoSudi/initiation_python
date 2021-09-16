#
# Fichier d'exemple pour les boucles
#

def main():
  x = 0
  
  # Definir une boucle while
  x = 0
  while (x < 5):
     print (x)
     x = x + 1

  # Definir une boucle For
  for x in range(5,10):
    print (x)
    
  # Utiliser For sur une collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # Utilisation du break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (x)
  
  #Utiliser la fonction enumerate() pour retrouver l'index
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)
  
if __name__ == "__main__":
  main()
