# Nobmbre de colonnes
largeur = int(input("Entrez une largeur : ")) 
# Nombre de lignes
hauteur = int(input("Entrez une hateur : ")) 


trait_côté = "|"
séparateur = "-"

for i in range (hauteur):
    if i == 0 or i == hauteur -1:
        # On met les tirets selon l'input sur la (1ere ligne  i = 0) et (derniere ligne i =hateur-1)
        séparateur = "-"
    else:
        # On enleve les tirets comme ça on aura le vide à l'interieur du rectangle
        séparateur = " "  

    print(trait_côté + (séparateur*largeur) + trait_côté)
