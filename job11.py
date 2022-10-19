# Traitement d'un fichier
# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le nombre de noms de domaine.
# Dans notre fichier on trouve : <column name="domain">0wnd.net</column>

with open('domains.xml', "r") as fichier:
   number  = fichier.read()
element = number.count('name="domain">')
print(element)
fichier.close() 


#Quand on execute le programme on trouve 309 noms de domaine.