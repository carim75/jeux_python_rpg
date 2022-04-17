from tkinter import *
from random import randint
from PIL import ImageTk, Image

def changeState(btn):
    if (btn['state'] == NORMAL):
        btn['state'] = DISABLED
    else:
        btn['state'] = NORMAL


#donner une valeur à une variable
def action(Variable, valeur):
    Variable.set(valeur) 

def puissance4(window_tp, Jetons, Inventaire, Objet):
    window_tp.withdraw()
    # creation de la 1e fenetre
    window_1 = Toplevel(window_tp)
    # configuration des parametres de la fenetre
    window_1.title("PUISSANCE 4")
    window_1.geometry("1350x680")
    window_1.minsize(480 , 360)
    window_1.config(background='black')
    # pas de possibilité de + / - la fenetre
    window_1.resizable(height=False , width= False)
    
    title = Label(window_1, text = "PUISSANCE 4 " , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    start = Button(window_1, text= "COMMENCER !", font= ("Super legend boy" , 60) , bg = 'black' , fg = 'white', command = lambda : mise(window_1,Jetons, Inventaire, Objet))
    title.pack(side=TOP)
    start.pack(expand=YES)
    objet = Label(window_1, text=("0bjet actif :", Objet) , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    objet.pack(expand=YES)
    btn_Start = Button(window_1, text="Inventaire", font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , command = lambda:  bag_p4(window_1, Jetons, Inventaire, Objet))
    btn_Start.pack(expand=YES)      

    #On regarde si l'utilisateur veut sortir
    # if Objet == "Corde de sortie":
    #     tp(window_1, Jetons)
    #     Inventaire[2] = Inventaire[2]-1                                                                         

#inventaire de la machine à sous
def bag_p4(window, Jetons, Inventaire, Objet) :
    window.withdraw()
    Window_shop = Toplevel(window)
    #taille/nom/logo
    Window_shop.title("GOLD GRABBER")
    Window_shop.geometry("800x600")
    Window_shop.resizable(height=False,width=False)
    Window_shop.iconbitmap("logo.ico")
    #fond de la fenetre menu
    Window_shop.config(background='black')
    #valeur pour le nombre d'occurence pour chaque objet
    nombre_clic_3 = IntVar(Window_shop,value = Inventaire[2])
    nombre_clic_2 = IntVar(Window_shop,value = Inventaire[1]) 
    nombre_clic_1 = IntVar(Window_shop,value = Inventaire[0])  
    
    lettre_3=str(nombre_clic_3.get())
    lettre_2=str(nombre_clic_2.get())
    lettre_1=str(nombre_clic_1.get())

    #Bouton et affichage pour l'objet 1, on lance la fonction en fonction de l'objet choisi
    Panel_item_1 = Label(Window_shop,text="Quitte ou Triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command= lambda : [puissance4(Window_shop, Jetons, Inventaire, "Quitte ou triple")])
    Button_item_1.grid(row=0,column=2,pady=5)
    if Inventaire[0]==0:
        changeState(Button_item_1)
    #Idem
    Panel_item_2 = Label(Window_shop,text="Bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:puissance4(Window_shop, Jetons, Inventaire, "Bouclier"))
    Button_item_2.grid(row=1,column=2,pady=5)
    if Inventaire[1]==0:
        changeState(Button_item_2)
    #Idem
    Panel_item_3 = Label(Window_shop,text="Corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:puissance4(Window_shop, Jetons, Inventaire, "Corde de sortie"))
    Button_item_3.grid(row=2,column=2,pady=5)
    if Inventaire[2]==0:
        changeState(Button_item_3)
    #Bouton quitter au cas où on n'a pas d'objet
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5, command= lambda : puissance4(Window_shop, Jetons, Inventaire, Objet))
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
    Window_shop.mainloop()

def mise(window,Jetons, Inventaire, Objet):
    # creation 2e fenetre -> entrer la mise
    window.withdraw()
    Fenetre2 = Toplevel(window)
    Fenetre2.title("PUISSANCE 4")
    Fenetre2.geometry("1350x680")
    Fenetre2.config(background='black')
    Fenetre2.resizable(height=False , width= False)
    
    Label(Fenetre2, text="Choisissez votre mise." , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()
    Label(Fenetre2, text=('Vous avez' ,Jetons, "jetons.") , font= ("Super legend boy" , 20)).pack()
    objet = Label(Fenetre2, text=("Objet actif :", Objet) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
    objet.pack()

    Colonne = " "

    #Les boutons de mise
    btn_100 = Radiobutton(Fenetre2 , text = 100 ,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,value = 100,command = lambda : [window_grille(Fenetre2, Jetons, 100, Inventaire, Objet, Colonne)], indicatoron=0)
    btn_100.pack(expand=YES)
    
    btn_250 = Radiobutton(Fenetre2 , text = 250,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white',value = 250, command = lambda : [window_grille(Fenetre2, Jetons, 250, Inventaire, Objet, Colonne)], indicatoron=0)
    btn_250.pack(expand=YES)
    
    btn_500 = Radiobutton(Fenetre2 , text = 500,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , value = 500,command = lambda : [window_grille(Fenetre2, Jetons, 500, Inventaire, Objet, Colonne)], indicatoron=0)
    btn_500.pack(expand=YES)
    
    btn_1000 = Radiobutton(Fenetre2 , text = 1000,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , value = 1000,command = lambda : [window_grille(Fenetre2, Jetons, 1000, Inventaire, Objet, Colonne)], indicatoron=0)
    btn_1000.pack(expand=YES)
    
    btn_all = Radiobutton(Fenetre2 , text = "All in",font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , value = Jetons, command = lambda : [window_grille(Fenetre2, Jetons, Jetons, Inventaire, Objet, Colonne)], indicatoron=0)
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
    
    Fenetre2.mainloop()

def window_grille(window, Jetons, Mise, Inventaire, Objet):
    Grille = [["_","_","_","_","_","_","_"], 
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_"]]

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
    window.withdraw()
    #creation 3e fenetre -> affichage de la machine a sous
    window_resultat = Toplevel(window)
    window_resultat.title("PUISSANCE 4")
    window_resultat.geometry("1350x680")
    window_resultat.resizable(height=False , width= False)
    window_resultat.config(background='black')
    Label(window_resultat, text = "Jouez sur une colonne",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').grid(anchor="n")
    Button_colonne = Button(window_resultat,text="o",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5, command= lambda : window_grille(window_resultat, Jetons, Inventaire, Objet))
    Button_colonne.grid(row=3,column=0,columnspan=4,pady=5) 


    window_resultat.mainloop()



Window = Tk()
Jetons = 1000
Inventaire = [1,1,1]
Objet = "Aucun"
puissance4(Window, Jetons, Inventaire, Objet)
Window.mainloop()
