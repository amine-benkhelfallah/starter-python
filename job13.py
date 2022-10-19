#Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre entier. 
# Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
#nombre de mots de la taille renseignée qui s’y trouvent.


nombre = int(input("Entrez un nombre entier : "))  # nombre de caractère d'un mot

with open ("data.txt", 'r') as fichier:
    texte = fichier.read()
    liste = texte.split()
nbr_mots = 0
for element in liste:
    if len(element) == nombre:
        nbr_mots = nbr_mots + 1 
print(nbr_mots)