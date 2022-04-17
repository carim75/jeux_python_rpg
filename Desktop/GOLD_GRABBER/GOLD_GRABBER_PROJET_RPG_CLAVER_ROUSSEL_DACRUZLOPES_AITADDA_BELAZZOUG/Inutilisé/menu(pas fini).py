# ce fichier à pour but de mettre en place le menu qui sera appelé dans le Fichier principale du jeu rpg

from time import sleep # Pour mettre un temps de pause dans le terminal sleep(Temps_Pause)

# Fonction Menu -> debut du jeu
def Menu():
    print ("Voici le menu :")
    print("Start")
    print("Charger")
    print("Information utile")
    print("Quitter")
    print("Veuillez entrer un menu :")
    List_Choice_Menu = ["Start","Charger","Info","Quitter"]
    Player_Choice_Menu = input()
    Result_Player_Choice = Ask_Menu_Player(Player_Choice_Menu,List_Choice_Menu)
    
    '''
    if Result_Player_Choice == "Start":
        New_game()
    
    elif Result_Player_Choice == "Charger":
        Load_Game()
    '''
    
    if Result_Player_Choice == "Info" :
        Infos()
    
    elif Result_Player_Choice == "Quitter":
        Quit()
    

'''
# Fonction qui crée une nouvelle partie
def New_Game():
    pass

# Fonction qui charge une partie
def Load_Game():
    pass
'''

# Fonction information qui appelle 3 autres fonctions 
def Infos():
    print("Vous voici dans le menu d'information du jeu.")
    print("Que rechercher vous ?")
    print("Distribution / Régle / Info")
    Info_List_Menu = ["Distribution","Régle","Info"]
    Info_Player_Choice_Menu = input()
    Info_Result_Player_Choice_Menu = Ask_Menu_Player(Info_Player_Choice_Menu,Info_List_Menu)
    
    if Info_Result_Player_Choice_Menu == "Distribution":
        Info_Distribution()
    
    elif Info_Result_Player_Choice_Menu == "Régle":
        Info_Rule_Game()
    
    elif Info_Result_Player_Choice_Menu == "Info":
        Info_Version()
    
    Menu()


# Fonction qui presente l'équipe

def Info_Distribution():
    print("Voici la distribution du Jeu.")
    print("On peut remercier")
    print("Carime pour tous son travail")
    print("Hugo pour ces mauvaise bonnes idées")
    print("Martin")
    print("Juba")
    print("Sanaa")
    sleep(5.0)


#Fonction qui montre comment jouer
def Info_Rule_Game():
    print("Voici comment jouer.")
    print("")
    sleep(5.0)

#fonction qui montre
def Info_Version():
    print("Voivi les informations du jeu.")
    print("")
    sleep(5.0)

# Fonction qui sort du jeu
def Quit():
    print("Merci d'avoir lancer le jeu.")
    sleep(2.0)
    quit

# Fonction qui recupere le choix du joueur dans le menu 
def Ask_Menu_Player(Player_Choice_Menu,List_Choice_Menu):
    while not Search_Player_Choice_Menu(Player_Choice_Menu,List_Choice_Menu):
        print("Veuillez vérifier votre choix, Vous cherhcer un menu non existant.")
        Player_Choice_Menu = input() 
    return Player_Choice_Menu

# Fonction qui cherche dans une liste un element
def Search_Player_Choice_Menu(Player_Choice,Menu_List):
  Timer = 0
  while Timer < len(Menu_List):
    if Menu_List[Timer] == Player_Choice:
      return True
    Timer = Timer + 1
  return False

Menu()