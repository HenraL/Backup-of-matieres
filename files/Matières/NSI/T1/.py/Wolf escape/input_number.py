from tkinter import*
def pause():
    pause=input("Appuyez sur Entrée pour continuer")
def LEVEL():
    #Récupération de la valeur du Spinbox
    Levelchoice = int(level.get())
    fenetre.destroy()
    print(Levelchoice)
    pause()

fenetre = Tk()
Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
Frame1.pack(side=LEFT, padx=10, pady=10)

label = Label(Frame1, text="Hello World")
label.pack()
level=Spinbox(Frame1, from_=0, to=10, increment=1)
level.pack(side=LEFT, padx=5)
bouton=Button(Frame1, text="Jouer!", command=LEVEL)
bouton.pack(side=RIGHT, padx=5)
fenetre.mainloop()