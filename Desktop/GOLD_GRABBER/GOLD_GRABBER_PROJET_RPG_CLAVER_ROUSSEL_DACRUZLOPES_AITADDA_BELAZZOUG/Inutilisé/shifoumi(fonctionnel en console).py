# carime
from random import randint
nom = input("entrer votre nom : ")
print("bonjour", nom)

#je crée une fonction
def jeux():
    user_victoire = 1
    nul = 1
    pc_victoire = 1
    #tant que c'est vraix le code s'éxecute
    while True:

        choix_user = (
            input("(p)ierre, (f)euille, (c)iseaux ou entrer(q) pour quitter le jeux : "))
        # on quitte le jeux si le player entre q
        if choix_user == "q":
            break

        if choix_user != "p" and choix_user != "f" and choix_user != "c" and choix_user != "q":
            continue

        if choix_user == "p":
            print("pierre contre ...", end=" ")

        elif choix_user == "f":
            print("feuille contre ...", end=" ")

        else:
            print("ciseau contre ...", end=" ")

        choix_ordi = randint(1, 3)

        if choix_ordi == 1:
            choi_pc = "p"
            print("pierre")
        elif choix_ordi == 2:
            choi_pc = "f"
            print("feuille")
        else:
            choi_pc = "c"
            print("ciseaux")

        if choix_user == choi_pc:
            print("matche nul", nul)
            nul = nul + 1

        elif choix_user == "p" and choi_pc == "c":
            print("tu a gagner", user_victoire)
            user_victoire = user_victoire + 1

        elif choix_user == "c" and choi_pc == "f":
            print("tu a gagner", user_victoire)
            user_victoire = user_victoire + 1

        elif choix_user == "f" and choi_pc == "p":
            print("tu a gagner", user_victoire)
            user_victoire = user_victoire + 1

        elif choix_user == "p" and choi_pc == "f":
            print("defaite : ", pc_victoire)
            pc_victoire = pc_victoire + 1

        elif choix_user == "f" and choi_pc == "c":
            print("defaite : ", pc_victoire)
            pc_victoire = pc_victoire + 1

        elif choix_user == "c" and choi_pc == "p":
            print("defaite : ", pc_victoire)
            pc_victoire = pc_victoire + 1

        if user_victoire == 4:
            print("bravo vous avez gagner")
            break

        if pc_victoire == 4:
            print("vous avez perdu la partie")
            break


jeux()

game = input("voulez-vous rejouez ?")

#si le player rentre oui alors alors je rapelle la fonction pour qu'il rejoue 
if game == "oui":
    jeux()
