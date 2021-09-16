# 
# Fichier d'exemple pour les variables
#

# Declarer une variable et l'initialiser

#Integer
a = 3
print(a)



#Float
b = 3.7
print(b)


#String
nom = "Hermine Lilou"
print(nom)


un_string = '''
Je crois que je suis concentré!
'''
print(un_string)

autre_string = "Hermine \n, Pascaline"
print(autre_string)


# La re-declaration des variables est possible
a = "Je suis un string"
print(a)


#Obtenir le type d'une variable
type(a)
type(autre_string)

#Caster
str(3) #Transformer un nombre 3 en string "3"
int("3")
float("5.3")
bool("True")


# Erreur: Les variables des types différents ne peuvent être combinées

#print ("string type " + 123)
print ("string type " + str(123))


#Operations sur le string
texte1 = "Je suis un developpeur python"

## Concatenation
texte2 = " et j'en suis fière"
texte3 = texte1 + texte2
print("texte Concatené", texte3)

##longueur de la chaine
len(texte1)

## Split Chaine
res = texte1.split(" ")
print(res)


#Mettre texte en majuscule
texte1 = texte1.upper()
texte1.

##Mettre texte en miniscule
texte1 = texte1.lower()

##Remplacer un element dans le texte
texte1 = texte1.replace(" ", "-")



#Collections

#Déclarer une list avec la possibilité de modifier son contenu
maliste = [0, 1, 1, 2, 2, 3, 5, 8, 13]
print (maliste)

# J'accède au 7e élément de la liste (les index commencent à 0)
maliste[6]
print(maliste[6])

# Je retire le 5e élément de la liste
maliste.pop(4)
print (maliste)
# J'ajoute un élément à la fin
maliste.append(21)
print (maliste)

#Ou
maliste+=[12]

# J'extrais les éléments de la position 3 jusqu'au bout
print(maliste[2:])

# J'extrais les deux premiers éléments
print(maliste[:2])

# J'extrais les éléments de la position 4 à 6 (les index commencent à 0)
print(maliste[3:5])

# Quelle est la longueur de ma liste ?
len(maliste)

maliste[2] = 'modif'
print(maliste)
# Je modifie un élément (celui qui est en 3e position !)

#Serie de fonction
ma_liste = []
ma_liste.append(1) # ajoute un élément à la liste
print(ma_liste)
print(ma_liste[0])
ma_liste.index(1) # retourne l’index d’une valeur 
ma_liste[0] = 2 # ajoute un élément à la liste
del ma_liste[0]  # supprimer une entrée avec son index 
ma_liste.remove(1)  # supprimer une entrée avec sa valeur ( la premiere trouvée ) 
ma_liste.reverse()  # inverse la liste
ma_liste.count(1)  # compte le nombre d’occurence d’une valeur
ma_liste_imbrique = [1, [2, 3 ]] # liste imbriqué
print(type(ma_liste ))

#Copier une liste
##Copie par référence
y = [1,2,3]
x = y # Attention ici x possède la même référence que y, ils sont donc lié 
y[0] = 4
print(x)

##Copie par valeur
x = [1,2,3]
y = x[:] # copie par valeur et non pas par référence
y[0] = 9
print(x, y)

#Transformation String en liste
ma_chaine = "Nicolas:Haziza:Toulouse"
resultat = ma_chaine.split(":")
print(resultat)

#Transformation liste en string
ma_liste = ['Nicolas', 'Haziza', 'Toulouse']
resultat = ':'.join(ma_liste)
print(resultat)

#Extension de liste  
ma_liste = ['Nicolas', 'Haziza']
ma_liste2 = ['Rennes', 'Toulouse']
ma_liste.extend(ma_liste2)
print(ma_liste)



#Déclarer un tuple sans la possibilité de modifier son contenu
montuple = (0, 1, 1, 2, 2, 3, 5, 8, 13)
print(montuple)

#J'accède au 7e élément de la liste (les index commencent à 0)
montuple[6]


#On peut pas modifier un tuple
montuple.pop(4)



#SET
liste_avec_doublons = ['pascal', 'pierre', 'paul', 'pierre']
print(set(liste_avec_doublons))

#Construire un dictionnaire
dico = {}
dico['computer'] = 'ordinateur'
dico['mouse'] ='souris'
dico['keyboard'] ='clavier'
dico.update({'printer': 'canon'})
print("dico")
dico = {'computer': 'ordinateur', 'keyboard': 'clavier', 'mouse': 'souris'}


#Un autre dictionnaire
berti = {
  'nom': 'Bertignac', 
  'prenom': 'Louis', 
  'instruments': ['guitare', 'chant']
  }
print(berti)

#Accéder à la valeur rattaché à la clé Nom
print(berti['nom'])

#Accéder à la valeur rattaché à la clé Instrument
print(berti['instruments'])

#Enregistrer un nouvel ensemble clé valeur
berti['groupes'] = ['Higelin', 'Telephone', 'Bertignac et les visiteurs']
print(berti)

#Accéder à une liste dans un dictionnaire
print(berti['groupes'][1])

#Effacer une clé et la valeur qui lui est associée
del berti['instruments']
print(berti)

#Récupérer une valeur depuis sa clé
print(dico.get("computer"))
print(dico["computer"])


#Supprimer une entrée
del dico["computer"]

#Récupérer la listes des clés
print(dico.keys())

#Récupérer la listes des valeurs
print(dico.values())


#Récupérer la listes des clés/valeurs
print(dico.items())



#Copier un dictionnaire par référene
dico_ref = dico

#Copier un dictionnaire par valeur
dico_copy =  dico.copy()






# Variables locales vs variables globales

def someFunction():
  #global a
  a = "deal"
  print (a)



#Mutiples variables
a,b = 7, "Je suis là"
print("a", a)
print("b", b)