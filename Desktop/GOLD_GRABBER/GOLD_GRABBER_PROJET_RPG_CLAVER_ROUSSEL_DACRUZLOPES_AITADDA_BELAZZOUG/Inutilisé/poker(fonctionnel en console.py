
def carte():
  from random import randint 
  Carte = randint(1,10)
  return Carte

def  tour_1():
  from random import randint
  tour = randint(1,2)
  return tour

def mise(Joueur):
  Mise = int(input("Combien voulez-vous miser ?"))
  while Mise > Joueur :
    Mise = int(input("Vous n'avez pas assez de jetons pour cette mise. Combien voulez-vous miser ?"))
  return Mise

def mise_2(Mise_Ordi, Joueur):
  Mise = mise(Joueur)
  print(Mise)
  while Mise < Mise_Ordi:
    print("La mise doit être égale ou supérieure à la mise de l'ordinateur.")
    return Mise
  return Mise

def coucher():
  Reponse = input("Voulez-vous vous coucher ? 'Oui' ou 'Non'")
  if Reponse == "Oui":
    print("Vous avez perdu.")
    return True
  else:
    return False


def main (Carte_1, Carte_2, Carte_3):
  Main = 0
  if Carte_1 == 1 :
    Carte_1 = 11

  if Carte_2 == 1:
    Carte_2 = 11

  if Carte_3 == 1:
   Carte_3 = 11

  if (Carte_2 == Carte_1+1 and Carte_3 == Carte_2+1) or (Carte_1 == Carte_2+1 and Carte_3 == Carte_1+1) or (Carte_3 == Carte_1+1 and Carte_2 == Carte_3+1) or (Carte_2 == Carte_3+1 and Carte_1 == Carte_2+1) or (Carte_3 == Carte_2+1 and Carte_1 == Carte_3+1) or (Carte_1 == Carte_3+1 and Carte_2 == Carte_1+1):
    Main = 200+Carte_1+Carte_2+Carte_3
  elif Carte_1 == Carte_2 and Carte_2 == Carte_3:
    Main = 100+Carte_1+Carte_2+Carte_3
  elif Carte_1 == Carte_2: 
    Main = 50+Carte_1+Carte_2
  elif Carte_2 == Carte_3 :
    Main = 50+Carte_2+Carte_3
  elif Carte_1 == Carte_3 :
    Main = 50+Carte_1+Carte_3
  else:
    if Carte_1 == 1 or Carte_2 == 1 or Carte_3 == 1:
      Main = 11
    elif Carte_3 > Carte_1 and Carte_3 > Carte_2:
      Main = Carte_3
    elif Carte_2 > Carte_1 and Carte_2 > Carte_3:
      Main = Carte_2
    elif Carte_1 > Carte_2 and Carte_1 > Carte_3:
      Main = Carte_1
  return Main

def poker (Jetons):
  from random import randint
  Carte_1 = carte()
  Carte_2 = carte()
  Carte_3 = carte()
  Carte_Ordi_1 = carte()
  Carte_Ordi_2 = carte()
  Carte_Ordi_3 = carte()
  Premier_tour = tour_1()

  print("Voici vos cartes :", Carte_1, Carte_2, Carte_3 )

  Joueur = Jetons
  Ordinateur = Jetons

  print("Vous avez ", Joueur, "jetons.")

  if Premier_tour == 1:
    Mise = mise(Joueur)
    print(Mise)
    Mise_Ordi =  randint(Mise, Ordinateur)
    print("L'ordinateur mise :",Mise_Ordi, "jetons.")
  else:
    Mise_Ordi =  randint(1, Ordinateur)
    print("L'ordinateur mise :",Mise_Ordi, "jetons.")
    if coucher():
      return
    Mise = mise_2(Mise_Ordi, Joueur)
    print(Mise)

  while Mise != Mise_Ordi:
    if Mise < Mise_Ordi:
      if coucher():
        return
      Mise = mise_2(Mise_Ordi, Joueur)
      print(Mise)
    elif Mise > Mise_Ordi:
      Mise_Ordi =  randint(Mise, Ordinateur)
      print("L'ordinateur mise :",Mise_Ordi, "jetons.")

  Main = main(Carte_1, Carte_2, Carte_3)
  Main_Ordi = main (Carte_Ordi_1, Carte_Ordi_2, Carte_Ordi_3)
  Mise_Totale = Mise + Mise_Ordi
  
  print("La main de l'ordinateur est",Carte_Ordi_1, Carte_Ordi_2, Carte_Ordi_3)
  print("Ta main est",Carte_1, Carte_2, Carte_3)

  if Main > Main_Ordi:
    print("Tu as gagné. Tu remportes", Mise_Totale, "jetons.")
  
  elif Main < Main_Ordi:
    print("Tu as perdu. L'ordinateur remporte", Mise_Totale, "jetons.")
  
  #while Joueur != 0 or Ordinateur =! 0:
    #poker(Joueur)

poker(500)