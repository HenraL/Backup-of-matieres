from tkinter import *
string="ee"
fenetre=Tk()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()
Button(text="valider", command=fenetre.destroy()).pack()
fenetre.mainloop()

print(StrinVar())
