
# Un prompteur devra s’afficher “>”, et le programme devra attendre un input.
# Si l’input entré est “Bonjour”, le programme devra répondre “Bonjour à toi”.
# Si l’input entré est “Au revoir”, le programme devra quitter.


n = (input(">"))
while n != "Au revoir":
    if n == "Bonjour":
        print("Bonjour à toi")
    else:
        print(n)
    n = (input(">"))




