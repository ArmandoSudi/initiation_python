# 
# Fichier d'exemple pour les variables
#

# Declarer une variable et l'initialiser

#Integer
# a = 3
# print(type(a))


#Float
# b = 12.5
# print(type(b))

#String
# nom = "GROHEUX "
# prenom = "David"
# parent = 'Henrique'
# famille = '''
# Formation python par la pratique
# On est tous sympa
# '''
# nom_complet = nom + prenom

# print(nom_complet)





# La re-declaration des variables est possible
# a = 15.6
# print(a)
# print(type(a))

#Obtenir le type d'une variable


#Caster
#str, int, float
# age = input("Quel est votre age ? ")
# resultat = int(age) + 10
# print("dans dix ans, vous aurez ", str(resultat))






# Erreur: Les variables des types différents ne peuvent être combinées

#print ("string type " + 123)


#Operations sur le string
#print(nom.lower())




## Concatenation

# nom_complet = nom + prenom
# print(nom_complet)

##longueur de la chaine
# print(len(nom_complet))

## Split Chaine
# texte_split = nom_complet.split(" ")
# print(texte_split)


#Mettre texte en majuscule


##Mettre texte en miniscule


##Remplacer un element dans le texte




#Collections

#Déclarer une list avec la possibilité de modifier son contenu
# ma_liste = [0, 1, 1, 2, 2, 3, 5, 8 , 13]
# print(ma_liste)
# print(type(ma_liste))

# J'accède au 7e élément de la liste (les index commencent à 0)
# print(ma_liste[6])


# Je retire le 5e élément de la liste
# ma_liste.pop(4)
# print(ma_liste)

# J'ajoute un élément à la fin
# ma_liste.append(21)
# print(ma_liste)

# J'extrais les éléments de la position 3 jusqu'au bout
# print("J'extrais les éléments de la position 3 jusqu'au bout")
# print(ma_liste[2:])
# ma_liste = ma_liste[2:]

# J'extrais les deux premiers éléments
# print("J'extrais les deux premiers éléments")
# print(ma_liste[:2])

# J'extrais les éléments de la position 4 à 6 (les index commencent à 0)
# print(ma_liste[3:5])


# Quelle est la longueur de ma liste ?
# print(len(ma_liste))


# Je modifie un élément (celui qui est en 3e position !)
# ma_liste[2] = "Modif"
# print(ma_liste)


#Déclarer un tuple sans la possibilité de modifier son contenu

mon_tuple = (0, 1, 1, 2, 2, 3, 5, 8 , 13)
print(mon_tuple)

#J'accède au 7e élément de la liste (les index commencent à 0)
print(mon_tuple[6])


#On peut pas modifier un tuple
#mon_tuple.append(4)



#SET
# liste_avec_doublon = ["pascal", "pierre", "alvarez", "pierre", "david"]
# print(liste_avec_doublon)

# liste_sans_doublon = set(liste_avec_doublon)
# print(liste_sans_doublon)


#Construire un dictionnaire
dico = {}
dico[0] = 'Ordinateur HP'
dico[1] = "Souris Compaq"
dico[2] = "Clavier PadTouch"
print(dico)

berti = { "nom": "Berti", "prenom": "Louis", "instruments": ["Guitare", "Piano"] }
print(berti)
print(berti["instruments"])
berti["groupes"] = ["Beattles", "Celine"]
print(berti)
del berti["instruments"]
print(berti)
berti["age"] = 25
print(berti)




#Un autre dictionnaire


#Accéder à la valeur rattaché à la clé Nom


#Accéder à la valeur rattaché à la clé Instrument


#Enregistrer un nouvel ensemble clé valeur

#Effacer une clé et la valeur qui lui est associée





# Variables locales vs variables globales
# a = 15
# def unefonctiontest():
#     b = 15
#     somme = a + b

# print(b)







#Mutiples variables



#Personne1 =  Nom de la personne 1

#Age1 = Age de la personne 1

#Personne2 = Nom de la personne 2

#Age2 = Age de la personne 2

#Personne1 a 25 ans, et Personne2 a 30 ans, le total donne 55 ans