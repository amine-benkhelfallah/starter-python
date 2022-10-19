#Traitement d’un fichier 
#Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
#le nombre de mots (sans caractère spéciaux) qui s’y trouvent.

#Un RegEx,Regular Expressionou (re)  est une séquence de caractères qui forme un modèle de recherche.
# le RegEx est utilisé pour vérifier si une chaîne contient un pattern spécifié
import re
with open('data.txt', "r") as fichier:   #ou fichier = open('data.txt', "r")
    texte = fichier.read()
#[a-zA-Z]+ Renvoie une correspondance au caractère alphabétique de a-z, minuscule & majuscule
    pattern = '[a-zA-Z]+'     
#Imprimez une liste de tous les matchs (les correspondances)        
    match = re.findall(pattern,texte)
    print(len(match))

