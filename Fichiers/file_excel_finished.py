import pandas as pd

#### ECRITURE

#Maintenant, utilisons un dictionnaire pour remplir un DataFrame:
df = pd.DataFrame({'Pays':['France', 'Canada', 'Belgique'], 'Capitale':['Paris', 'Ottawa', 'Bruxelles']})

#les clés dans notre dictionnaire servira de nom de colonne. De même, le valeurs devenir les lignes contenant les informations.

#nous pouvons utiliser le to_excel() pour écrire le contenu dans un fichier
df.to_excel('./pays.xlsx')


#sheet name
df.to_excel('./pays.xlsx', sheet_name='Pays')


df.to_excel('./pays.xlsx', sheet_name='Pays', index = False)


#Écriture de plusieurs DataFrames dans un fichier Excel

# income1 = pd.DataFrame({'Noms': ['Stephen', 'Camilla', 'Tom'], 'Salaire':[100000, 70000, 60000]}) 
# income2 = pd.DataFrame({'Noms': ['Pete', 'April', 'Marty'], 'Salaire':[120000, 110000, 50000]})
# income3 = pd.DataFrame({'Noms': ['Victor', 'Victoria', 'Jennifer'], 'Salaire':[75000, 90000, 40000]})

# income_sheets = {'Groupe1': income1, 'Groupe2': income2, 'Groupe3': income3}
# writer = pd.ExcelWriter('./income.xlsx', engine='xlsxwriter')

# for sheet_name in income_sheets.keys(): 
#     income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

# writer.save()

#students_grades = pd.read_excel('./mics.xlsx')
#Previsualisation
#print(students_grades.head())


cols = [0, 1]
mics_result = pd.read_excel('./mics.xlsx', usecols=cols)
#print(mics_result.head())


# xl = pd.ExcelFile('./mics.xlsx')
# df1 = pd.read_excel(io='./mics.xlsx', sheet_name = xl.sheet_names[0], header = None, usecols=cols) #data

# for j in df1.index:
#     print(df1[1][j]) #Lecture de toute la colonne 1
#     if j > 6:
#         break
