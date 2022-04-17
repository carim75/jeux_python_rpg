#Identifie tous les carrés non minés sans déclancher d'explosion ,car des bombes sont dissimulées dans le champ vert
from tkinter import *
import random

gameover = False
score = 0
carre_verification = 0

def demineur():
    creer_terrainMiner(terrainMiner)
    fenetre = Tk()
    configuration_fenetre(fenetre)
    fenetre.mainloop()

terrainMiner = []
def creer_terrainMiner(terrainMiner):
    global carre_verification
    for rangée in range(0,10):
        listerangée = []
        for colonne in range (0,10):
            if random.randint(1,100) < 20:
                listerangée.append(1)
            else : 
                listerangée.append(0)
                carre_verification = carre_verification + 1
        terrainMiner.append(listerangée)
    #printTerrain(terrainMiner)

def printTerrain(terrainMine):
    for listeRangée in terrainMiner:
        print(listeRangée)

def configuration_fenetre(fenetre):
    for numeroRangée , listeRangée in enumerate(terrainMiner):
        for numeroColonne , entreeColonne in enumerate(listeRangée):
            if random.randint(1,100) < 25:
                carré = Label(fenetre,text = "    ",bg = "darkgreen")
            elif random.randint(1,100) > 75:
                carré = Label(fenetre,text="    ",bg="seagreen")
            else:
                carré = Label(fenetre,text="    ",bg="green")
            carré.grid(row = numeroRangée , column= numeroColonne)
            carré.bind("<Button-1>",quand_cliqué)


def quand_cliqué(event):
    global score
    global gameover
    global carre_verification
    carré = event.widget
    rangée = int(carré.grid_info()["row"])
    colonne = int(carré.grid_info()["column"])
    texteActu = carré.cget("text")
    if gameover == False:
        if terrainMiner[rangée][colonne] == 1:
            gameover = True
            carré.config(bg="red")
            print("Game Over ! Tu as touché une bombe 💣 !") 
            print("Score : ", score)
        elif texteActu == "    ":
            carré.config(bg="brown")
            totalbombe = 0

            if rangée < 9:
                if terrainMiner[rangée+1][colonne] == 1:
                    totalbombe = totalbombe + 1
            if rangée > 0 :
                if terrainMiner[rangée-1][colonne] == 1:
                    totalbombe = totalbombe + 1
            if colonne < 0:
                if terrainMiner[rangée][colonne+1] == 1:
                    totalbombe = totalbombe + 1
            if rangée < 9:
                if terrainMiner[rangée-1][colonne-1] == 1:
                    totalbombe = totalbombe + 1
            if rangée > 0 and colonne > 0:
                if terrainMiner[rangée-1][colonne-1] == 1:
                    totalbombe = totalbombe + 1
            if rangée < 9 and colonne > 0:
                if terrainMiner[rangée+1][colonne-1] == 1:
                    totalbombe = totalbombe + 1
            if rangée > 0 and colonne < 9:
                if terrainMiner[rangée-1][colonne+1] == 1:
                    totalbombe = totalbombe + 1
            if rangée < 9 and colonne < 9:
                if terrainMiner[rangée+1][colonne+1] == 1:
                    totalbombe = totalbombe + 1
            carré.config(text = " " +str(totalbombe) + " ")


            carre_verification = carre_verification - 1
            score = score + 1

            if carre_verification == 0:
                gameover = True
                print("Bravo, tu as trouvé tous les carrés non minés !")
                print("Score:",score)
demineur()






