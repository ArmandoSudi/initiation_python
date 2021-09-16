#
# Fichier d'exemple pour le timedelta Objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construire un basic timedelta et l'afficher
print (timedelta(days=365, hours=5, minutes=1))

# Afficher la date d'aujourd'hui 
now = datetime.now()
print ("today is: " + str(now))

# Ajouter un an à la date actuelle
print ("Un an à partir d'aujourd'hui sera: " + str(now + timedelta(days=365)))

# créer un timedelta qui utilise plus d'un argument
print ("Dans deux semaines et 3 jours, il sera: " + str(now + timedelta(weeks=2, days=3)))

# calcule la date d'il y a une semaine, formatée comme un String
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("Il y a une semaine, c'etait le  " + s)


#Obtenir la date d'aujourd'hui
today = date.today()

#Obtenir une date precise (Nouvel an)
nouvel_an = date(today.year, 1,1)

#Operation entre les dates
diff = today-nouvel_an

print(diff.days)
print(diff.min)
print(diff.seconds)


#Obtenir la date pour le prochain nouvel an
nouvel_an = nouvel_an.replace(year = today.year + 1)




