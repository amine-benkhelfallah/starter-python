# Avec la boucle for et d’une fonction system, affichez uniquement les nombres se trouvant entre l’input 1 et l’input 2.
# Le programme doit toujours partir de l’input 1 et aller jusqu’à l’input 2

n = input('valeur 1 : ')
n=int(n)
b = input('valeur 2 : ')
b=int(b)
if (n<b):
    for i in range (n+1,b,1):
        print(i)
else:
    for i in range (n-1,b,-1):
        print(i)
if (n==b):
    print('Valeurs égales')