#
# Lire et écrire dans les fichiers
#

def main():  
  #Ouvrir un fichier pour ecriture and le créer si cela n'existe pas
  f = open("textfile.txt","w+")
  
  # Ouvrir un fichier pour ajouter du contenu à la fin
  # f = open("textfile.txt","a+")

  # Ecrire quelques lignes des données dans le fichier
  for i in range(10):
    f.write("Ligne %d\r\n" % (i+1))
  
  # Fermer le fichier à la fin des opérations
  f.close()
  
  # Ouvrir le fichier en mode lecture
  f = open("textfile.txt","r")

  #Lire dans le fichier
  if f.mode == 'r': # Test pour verifier que le fichier est bien ouvert en mode lecture
    # Utilisez la fonction read() pour lire tout le contenu du fichier
    # contents = f.read()
    # print (contents)
    
    fl = f.readlines() # readlines lit les lignes individuellement dans une liste
    for x in fl:
      print (x)
    
if __name__ == "__main__":
  main()
