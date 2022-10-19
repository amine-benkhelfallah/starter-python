#Trier SANS SORT

# Créer un programme qui devra contenir une seule fonction qui
# prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :

# Remplir une liste myList contenant tous ces paramètres.
# Trier par ordre croissant la liste à l’aide de la fonction sort (Donc sans la fonction sort)
# Afficher la liste dans un terminal


from itertools import permutations


def myFunction ( *params ):
    myList = []

    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print("Le programme reconnaît uniquemnt les nombres")
    
    permutation = True
    passage =0
	
    while permutation == True:
        
        permutation = False
        passage = passage + 1
        
        for en_cours in range(0, len(myList) - passage):
            if myList[en_cours] > myList[en_cours + 1]:
                permutation = True
# on echange les deux élements
                myList[en_cours],  myList[en_cours + 1] =\
                myList[en_cours + 1],myList[en_cours]
    print (myList)
myFunction (45, 58, 62, 47, 25, 81, 13)

#Apres execution on a le resulatat suivant : 13, 25, 45, 47, 58, 62, 81
