#On va créer 7 colonnes et le joueur choisira où il joue !
#le jeton joué sera placé en fonction de ce qu'il y a dans la colonne
from random import randint
Grille = [  ["_","_","_","_","_","_","_"], 
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"]]

#On définit quelle colonne on veut jouer
def colonne():
  Colonne = int(input("Entrez la colonne où vous voulez jouer. (1 à 6)"))
  while Colonne <0 or Colonne > 6 :
    print("Erreur, chiffre inexact")
    Colonne = colonne()
  return Colonne

#On détermine s'il y a un gagnant en comparant chaque possibilités  
def gagnant(Grille):

  #On regarde les lignes
  for i in range (0,6):
    for j in range(0,4):
      if Grille[i][j] == Grille[i][j+1] and Grille[i][j+1] == Grille[i][j+2] and Grille[i][j+2] == Grille[i][j+3] and Grille[i][j]!= "_":
        print("Le joueur de",Grille[i][j],"a gagné.")
        return True
  #On regarde les colonnes      
  for i in range (0,7):
    for j in range(0,3):
        if Grille[j][i] == Grille[j+1][i] and Grille[j+1][i] == Grille[j+2][i] and Grille[j+2][i] == Grille[j+3][i] and Grille[j][i]!= "_":
          print("Le joueur de",Grille[j][i],"a gagné.")
          return True
  #On regarde les diagonales
  for i in range (0,3):
    for j in range (0,4):
      if Grille[i][j] == Grille[i+1][j+1] and Grille[i+1][j+1] == Grille[i+2][j+2] and Grille[i+2][j+2] == Grille[i+3][j+3] and Grille[i][j]!= "_":
        print("Le joueur de",Grille[1][1],"a gagné.")
        return True
      elif Grille[i][-j-1] == Grille[i+1][-j-2] and Grille[i+1][-j-2] == Grille[i+2][-j-3] and Grille[i+2][-j-3] == Grille[i+3][-j-4] and Grille[i][-j-1]!= "_":
        print("Le joueur de",Grille[1][1],"a gagné.")
        

def puissance4 (Grille):
  print('\n',Grille[0],'\n',Grille[1],'\n',Grille[2],'\n',Grille[3],'\n',Grille[4],'\n',Grille[5],'\n')

  #Le jeu se déroule jusqu'à que le nombre de tour max soit atteint ou qu'un joueur soit gagnant
  for i in range(0,21):
    print("Vous jouez les Jaunes")
    print(i)

    Colonne = colonne()
    Colonne = Colonne - 1
    
    #On fait descendre la pièce le plus bas possible dans la colonne où le joueur veut jouer
    for ligne in range(0,6):
      if Grille[ligne][Colonne] == "1" or Grille[ligne][Colonne] == "0":
        Grille[ligne-1][Colonne] = "0"
        break
      elif ligne == 5:
        Grille[ligne][Colonne] = "0"

    print('\n',Grille[0],'\n',Grille[1],'\n',Grille[2],'\n',Grille[3],'\n',Grille[4],'\n',Grille[5],'\n')

    #On regarde s'il y a un gagnant
    if gagnant(Grille) == 1 :
      return
    #On répète les actions pour l'ordinateur qui joue au hasard
    Colonne = randint(0,5)

    for ligne in range(0,6):
      if Grille[ligne][Colonne] == "1" or Grille[ligne][Colonne] == "0":
        Grille[ligne-1][Colonne] = "1"
        break
      elif ligne == 5:
        Grille[ligne][Colonne] = "1"

    print('\n',Grille[0],'\n',Grille[1],'\n',Grille[2],'\n',Grille[3],'\n',Grille[4],'\n',Grille[5],'\n')
    #On regarde s'il y a un gagnant
    if gagnant(Grille) == 1 :
      return
    
    
        
    
  

puissance4(Grille)