from tkinter import *

def bag(window) :
    window.withdraw()
    Window_shop = Toplevel(window)
    #taille/nom/logo
    Window_shop.title("GOLD GRABBER")
    Window_shop.geometry("800x600")
    Window_shop.resizable(height=False,width=False)
    Window_shop.iconbitmap("logo.ico")
    #fond de la fenetre menu
    Window_shop.config(background='black')
    #fonction revenir en arrire
    def back (window1,window2):
        window1.withdraw()
        window2.deiconify()
    nombre_clic  = IntVar(Window_shop,value= 5 ) 
    def add_passage (lettre,number_item_1):
        nombre_clic.set( nombre_clic.get() - 1 )
        lettre=str(nombre_clic.get())
        number_item_1.config(text=lettre)
    lettre=str(nombre_clic.get())
    #
    Panel_item_1 = Label(Window_shop,text="quitte ou double", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text="0", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_passage(lettre,number_item_1))
    Button_item_1.grid(row=0,column=2,pady=5)
    #
    Panel_item_2 = Label(Window_shop,text="bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text="0", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_passage(lettre,number_item_1))
    Button_item_2.grid(row=1,column=2,pady=5)
    #
    Panel_item_3 = Label(Window_shop,text="corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text="0", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_passage(lettre,number_item_1))
    Button_item_3.grid(row=2,column=2,pady=5)
    #
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5)
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
    Window_shop.mainloop()