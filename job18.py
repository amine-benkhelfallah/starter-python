#Trier avec sort

#- Remplir une liste myList contenant tous ces paramètres.
#- Trier par ordre croissant la liste à l’aide de la fonction sort
#- Afficher la liste dans un terminal

def myFunction ( *params ):
    myList = []

    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
# La fonction Python list sort() peut être utilisée pour trier 
# une liste dans l’ordre croissant, décroissant ou défini par l’utilisateur

            myList.sort()
        else:
            print("Le programme reconnaît uniquemnt les nombres")
    
    print(myList)

myFunction(45, 568, 547, 12 , 48)

#Apres execution du programme on aura le resultat suivant: 12, 45,48, 547,568