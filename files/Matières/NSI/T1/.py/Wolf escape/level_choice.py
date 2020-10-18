from tkinter import *
img1=img2=img3=img4=img5=img6="img/wolf_mainmenu.png"
#def show_choose_leveltk():
    #def Levelchoice():
    #	Levelnumber = int(level.get())
    #	Cevel.destroy()
    #    print(Levelnumber)
    #    global choix
    #    choix='l{}'.format(Levelnumber)
    #    return choix
    #Cevel = Tk()
    #Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
    #Frame1.pack(side=LEFT, padx=10, pady=10)

    #label = Label(Frame1, text="Hello World")
    #label.pack()
    #level=Spinbox(Frame1, from_=1, to=10, increment=1)
    #level.pack(side=LEFT, padx=5)
    #bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    #bouton.pack(side=RIGHT, padx=5)
    #Cevel.mainloop()

fenetre = Tk()
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
for ligne in range(20):
    for colonne in range(2):
        Button(canvas, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)
canvas.pack()
fenetre.mainloop()
