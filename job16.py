#Fonctions et paramètres 

# Créer un programme qui devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini.
# La fonction écrira tous les paramètres dans le terminal.


def myFunction ( *params ):
    print(params)

# Exemple :  liste d'argument : "html", "CSS", "bébé", "école", "pomme"
myFunction("html", "CSS", "bébé", "école", "pomme")