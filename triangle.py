
# Écrire un programme qui affiche dans le terminal un triangle avec des :
# "_"
# "\"
# "/"

hauteur = int(input("Entrez la hauteur de votre triangle: "))
if hauteur == 0:
    print("Size is null.")
    exit()

y = hauteur - 1 
z = 0
s = 1
space = " "

while s <= hauteur:
    if s == hauteur:
        print(y*space, end="")
        print("/",end="")
        print(z*"_",end="")
        print("\\")
    else:
        print(y*space, end="")
        print("/",end="")
        print(z*space,end="")
        print("\\")
    s+=1
    y-=1
    z+=2

    