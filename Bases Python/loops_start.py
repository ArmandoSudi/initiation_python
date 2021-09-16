#
# Fichier d'exemple pour les boucles
#

def main():
    
  
  # Definir une boucle while
  # x = 0
  # while (x < 5):
  #   print("valeur de x", x)
  #   x = x + 1 #incrementation
    
  

  # Definir une boucle For
  # for x in range(0,8):
  #   print(x)
  
    
  # Utiliser For sur une collection
  # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  # for d in days:
  #   print(d)
  
  print("*************")
  # print (days[1])

  # for x in range(0,len(days) - 1):
  #   print(x)
  #   print(days[x])
  
  
  # Utilisation du break and continue statements

  # for x in range(0,len(days) - 1):
  #   if x > 4:
  #     break
  #   print(x)
  #   print(days[x])
    

  
  
  #Utiliser la fonction enumerate() pour retrouver l'index
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for (i, d) in enumerate(days):
    print(i, d)
  
  
if __name__ == "__main__":
  main()
