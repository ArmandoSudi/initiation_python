#pip install python
#pip install pip install openpyxl xlsxwriter xlrd
#pip install xlwt

import pandas as pd


### Ecriture dans un fichier excel

#Pour ecrire dans un fichier excel, on utilise la methode Dataframe de Panda qui prend en paramètre un dictionnaire

#Declaration d'un dictionnaire
mondico = {
    'Pays': ['France', 'Canada', 'Belgique'],
    'Capitale': ['Paris', 'Ottawa', 'Bruxelles']
}

#créer mon dataframe panda
df = pd.DataFrame(mondico)

#Ecrit puis crée dans le repetoire en cours le fichier pays.xls ayant les informations de notre dictionnaire
df.to_excel('./pays.xls', sheet_name='test pays', index = False)
print("Fichier créé avec succès")







### LECTURE


#cols = [0,1]
#mics_result = pd.read_excel('./mics.xlsx', usecols = cols)
#Affichage d'un resumé du fichier excel par Pandas


#Recuperation des [meta]données sur le fichier excel mics.xls
xl = pd.ExcelFile('./mics.xlsx')
#Affiche les noms de feuille provenant du fichier excel
print(xl.sheet_names) 
#Lecture d'un fichier mics.xlsx se trouvant sur le repertoire en cours.
df1 = pd.read_excel(io = './mics.xlsx', sheet_name=xl.sheet_names[0], header= None)
#Affiche le résumé du fichier lu
print("Affichage du rsumé")
print(df1.head)

#Opération de parcours sur l'ensemble des colonnes du fichier
print("Resultat du parcours")
for j in df1.index:
    print(df1[0][j]) #Parcours sur l'ensemble des valeurs de la colonne 0
    print(df1[1][j]) #Parcours sur l'ensemble des valeurs de la colonne 1
    print(df1[2][j]) #Parcours sur l'ensemble des valeurs de la colonne 2

    if j > 50:
        break


