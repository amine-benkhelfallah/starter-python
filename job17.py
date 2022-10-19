# Créer un programme qui devra contenir une fonction qui prend en paramètres un nombre 
# de paramètres indéfini (uniquement des nombres).
# La fonction devra :Remplir une liste myList contenant tous ces paramètres.
# Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def myFunction ( *params ):
    myList = []
    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print("le programme reconnaît uniquemnt les nombres")
    
    for element in myList:
        if element % 2 == 0:   #nombre pairs = multiples de 2 , modulo 
            print(element)

myFunction(45, 568, 547, 12 , 48)
#Exp/ sur cette liste de nombres, on a 3 multiple de 2 les 568,12 et 48  