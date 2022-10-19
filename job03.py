#Quel âge as tu?..-18:tu es mineur/ +18:tu es majeur 
age = (input("Bonjour, quel âge as tu ?"))
# pourquoi int???
age=int(age)
if(age<=18):
    print("tu es mineur")
else:
    print("tu es majeur")


