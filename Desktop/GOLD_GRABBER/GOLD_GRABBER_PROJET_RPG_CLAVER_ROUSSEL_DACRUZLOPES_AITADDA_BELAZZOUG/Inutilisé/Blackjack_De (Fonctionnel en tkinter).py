from tkinter import *
from random import randint

def BlackJack(Jetons):
        # La fenetre du lancement du jeu
    Windows_real_Game = Tk()
    Windows_real_Game.title("Blackjack")
    Windows_real_Game.iconbitmap('logo.ico')
    Windows_real_Game.geometry("1600x900")
    Windows_real_Game.resizable(height=False,width=False)
    Windows_real_Game.config(background='#000000')

    # Boite de rangement
    Frame_Box = Frame(Windows_real_Game)

    # Les Bouttons et l'affichage
    title_Game = Label(Windows_real_Game, text = "Le BlackJack" ,font=("Super legend boy",40), bg = 'black' , fg = 'white')
    Button_Inventory = Button(Frame_Box,text="Inventaire",font=("Super legend boy", 40),padx=150,pady=100,bg='black',fg='white')
    Button_Start = Button(Frame_Box,text= "Start",font=("Super legend boy", 60),bg='black',fg='white',padx=150,pady=75,command= lambda : Pari(Windows_real_Game,Jetons))

    # Rangement dans la fenetre
    title_Game.pack(side=TOP)
    Frame_Box.pack(expand=YES)

    # Placement dans la box
    Button_Inventory.grid(row=0,column=0)
    Button_Start.grid(row=0,column=1)

    # Affichage de la fenetre
    Windows_real_Game.mainloop()
def Pari(Window,Jetons):
    
    # la fenetre des bets
    Window.withdraw()
    Window_Bet = Toplevel(Window)
    Window_Bet.title("BlackJack")
    Window_Bet.geometry("1600x900")
    Window_Bet.resizable(height=False,width=False)
    Window_Bet.config(background='#000000')
    
    #Changer l'état du bouton
    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
          btn['state'] = NORMAL

    # les boutons et affichage
    Label(Window_Bet, text="Choisissez votre mise." , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()
    Label(Window_Bet, text=('Vous avez' ,Jetons, "jetons.") , font= ("Super legend boy" , 20)).pack()
    
    #Le résultat
    #Result = resultats()

    #La valeur de la mise avant qu'on la choisisse grâce aux boutons
    IntMise = IntVar()
    
    #Les boutons de mise
    btn_100 = Radiobutton(Window_Bet , text = 100 ,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : Game_BlackJack(Window_Bet,Jetons,100))#, action(IntMise, 100)], indicatoron=0)
    btn_100.pack(expand=YES)
    
    btn_250 = Radiobutton(Window_Bet , text = 250,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : Game_BlackJack(Window_Bet,Jetons, 250))#, action(IntMise, 250)], indicatoron=0)
    btn_250.pack(expand=YES)
    
    btn_500 = Radiobutton(Window_Bet , text = 500,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : Game_BlackJack(Window_Bet,Jetons, 500))#, action(IntMise, 500)], indicatoron=0)
    btn_500.pack(expand=YES)
    
    btn_1000 = Radiobutton(Window_Bet , text = 1000,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : Game_BlackJack(Window_Bet,Jetons, 1000))#, action(IntMise, 1000)], indicatoron=0)
    btn_1000.pack(expand=YES)
    
    btn_all = Radiobutton(Window_Bet , text = "All in",font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = Jetons, command = lambda : Game_BlackJack(Window_Bet,Jetons, Jetons))#, action(IntMise, Jetons)], indicatoron=0)
    btn_all.pack(expand=YES)

    #changer l'état des boutons
    if Jetons < 100:
        changeState(btn_1000)
        changeState(btn_500)
        changeState(btn_250)
        changeState(btn_100)

    elif Jetons < 250:
        changeState(btn_1000)
        changeState(btn_500)
        changeState(btn_250)

    elif Jetons < 500:
        changeState(btn_1000)
        changeState(btn_500)
    
    elif Jetons < 1000:
        changeState(btn_1000) 

    Window_Bet.mainloop()   

def Game_BlackJack (Window,Jetons,Mise):
    
    # la fenetre des bets
    Window.withdraw()
    Windows_Principale = Toplevel(Window)
    Windows_Principale.title("BlackJack")
    Windows_Principale.geometry("1600x900")
    Windows_Principale.resizable(height=False,width=False)
    Windows_Principale.config(background='#000000')
    
    # Stat de base
    De_Bot = randint(4,6) + randint(4,6)
    De_1_Player = randint(1,6)
    De_2_Player = randint(1,6)
    De_3_Player = randint(1,6)
    Valut_Hand_Player = [De_1_Player + De_2_Player]
    print(Valut_Hand_Player)
    
    # Le jeu
    def Game(Button,Valut_Hand_Player,De_Bot,De_3_Player,Jetons,Mise):
        Button_3De.config(state=DISABLED)
        if Button :
            Button_3De.config(state=DISABLED)
            Valut_Hand_Player[0] = Valut_Hand_Player[0] + De_3_Player
            Label_game.config(text=('Votre main a une valeur de ', Valut_Hand_Player,' points'))
        if not Button :
            if Valut_Hand_Player[0] > 12 :
                Jetons = Jetons - Mise
                Label_game.config(text="Vous avez perdu, votre main est trop grande")
            elif Valut_Hand_Player[0] < De_Bot :
                Jetons = Jetons - Mise
                Label_game.config(text=(" Vous avez perdu, la bank rafle tout : ",De_Bot))
            elif Valut_Hand_Player[0] >= De_Bot :
                Jetons = Jetons + Mise*2
                Label_game.config(text="Vous avez gagné")
            print(Jetons)

    # La boite de rangement
    Frame_Menu = Frame(Windows_Principale,bg='#000000')

    # Les boutons du jeu
    Button_3De = Button(Frame_Menu,text='Ajouter un Dé',font= ("Super legend boy" , 30),padx=30,pady=20,bg='#000000',fg='white',command= lambda : Game(True,Valut_Hand_Player,De_Bot,De_3_Player,Jetons,Mise))
    Button_verif = Button(Frame_Menu,text='Dévoiler',font= ("Super legend boy" , 30),padx=30,pady=20,bg='#000000',fg='white',command= lambda : Game(False,Valut_Hand_Player,De_Bot,De_3_Player,Jetons,Mise))
    Label_game = Label(Frame_Menu,text= (' Votre main a une valeur de ',Valut_Hand_Player,' points'),font= ("Super legend boy" , 30),padx=140,pady=20,bg='#000000',fg='white')

    # Placements
    Frame_Menu.pack(expand=YES)
    Button_3De.grid(row=0,column=0)
    Label_game.grid(row=0,column=1)
    Button_verif.grid(row=0,column=2)

    Windows_Principale.mainloop()
    

BlackJack(600)