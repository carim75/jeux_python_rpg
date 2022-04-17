from tkinter import *

def Bet(Life_Coin):

    # Cree la fennetre
    Windows_Bet = Tk()
    Windows_Bet.title("Bet")

    # L'entrer
    Entry_Bet = Entry(Windows_Bet,width=35,borderwidth=5)
    Entry_Bet.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    Entry_Bet.insert(0, "0")

    # Liste des fonction

    def Add_Button(Number):
        Current_Entry_Bet = Entry_Bet.get()
        Entry_Bet.delete(0, END)
        Entry_Bet.insert(0, str(Current_Entry_Bet) + str(Number))       

    def Clear ():
        Entry_Bet.delete(0, END)
    
    def All_In (Life_Coin):
        Clear()
        Entry_Bet.insert(0, Life_Coin)
    
    def Validate_Bet():
        Current_Entry_Bet = int(Entry_Bet.get())
        if Current_Entry_Bet <= Life_Coin and Current_Entry_Bet > 0:
            return True
        return False

    Bet_Validate_True = Validate_Bet()
    if Bet_Validate_True :
        Bet_Current = int(Entry_Bet.get())
        return Bet_Current
        quit()


    # Je parrametre mes Bouttons, ils renvoient a la fonction Add_Buuton, j'utilise Lambda pour pourvoir mettre un paramettre à ma fonction
    Button_0 = Button(Windows_Bet,text="0",padx=39,pady=20,command=lambda :Add_Button(0))
    Button_1 = Button(Windows_Bet,text="1",padx=40,pady=20,command=lambda :Add_Button(1))
    Button_2 = Button(Windows_Bet,text="2",padx=40,pady=20,command=lambda :Add_Button(2))
    Button_3 = Button(Windows_Bet,text="3",padx=40,pady=20,command=lambda :Add_Button(3))
    Button_4 = Button(Windows_Bet,text="4",padx=40,pady=20,command=lambda :Add_Button(4))
    Button_5 = Button(Windows_Bet,text="5",padx=40,pady=20,command=lambda :Add_Button(5))
    Button_6 = Button(Windows_Bet,text="6",padx=40,pady=20,command=lambda :Add_Button(6))
    Button_7 = Button(Windows_Bet,text="7",padx=40,pady=20,command=lambda :Add_Button(7))
    Button_8 = Button(Windows_Bet,text="8",padx=40,pady=20,command=lambda :Add_Button(8))
    Button_9 = Button(Windows_Bet,text="9",padx=40,pady=20,command=lambda :Add_Button(9))  

    Button_Clear = Button(Windows_Bet,text="Clear",padx=29,pady=20,command=Clear)
    Button_All_In = Button(Windows_Bet,text="All In !",padx=29,pady=20,command=lambda : All_In(Life_Coin))
    Button_Validate = Button(Windows_Bet,text="Bet",padx=40,pady=20,command=Validate_Bet)

    # Initialise le boutton
    Button_1.grid(row=3,column=0)
    Button_2.grid(row=3,column=1)
    Button_3.grid(row=3,column=2)

    Button_4.grid(row=2,column=0)
    Button_5.grid(row=2,column=1)
    Button_6.grid(row=2,column=2)
    
    Button_7.grid(row=1,column=0)
    Button_8.grid(row=1,column=1)
    Button_9.grid(row=1,column=2)

    Button_0.grid(row=4,column=0)
    Button_Clear.grid(row=4,column=1)
    Button_All_In.grid(row=4,column=2)

    Button_Validate.grid(row=5,column=0,columnspan=3)


    Windows_Bet.mainloop()  

t = Bet(100)