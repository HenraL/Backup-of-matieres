from tkinter import *
QCMS=['e', 'z', 'f', 't', 'y', 'i','e', 'z', 'f', 't', 'y', 'i','e', 'z', 'f', 't', 'y', 'i']

Framebotbg="white"
Framebotfg="black"
playbg="white"
playfg="black"
createbg="white"
createfg="black"
fenetrebg="white"
Framebotbg="white"
Framemidbg="white"
Frame1bg="white"

def CreateOrPlay():
    def Play():
        fenetre.destroy()
        print("ze")
    def Create():
        fenetre.destroy()
        print("ez")
    def Quit():
        fenetre.destroy()
        print("quit")
    fenetre = Tk()
    fenetre.title("Créer ou Jouer ?")
    fenetre['bg']=fenetrebg
    Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT, bg=Frame1bg)
    Frame1.pack(side=TOP, padx=10, pady=10, fill=X)
    Framebot = Frame(fenetre, borderwidth=2, relief=FLAT, bg=Framemidbg)
    Framebot.pack(side=BOTTOM, padx=0, pady=0)
    Framemid = Frame(fenetre, borderwidth=2, relief=FLAT, bg=Framebotbg)
    Framemid.pack(side=BOTTOM, padx=0, pady=0)
    label=Label(Frame1, text="Voulez-vous créé ou jouer à un QCM?", bg=Framebotbg, fg=Framebotfg)
    label.pack()
    bouton=Button(Framemid, text="Créer un QCM",bg=playbg, fg=playfg, command=Play)
    bouton.pack(side=LEFT, padx=5)#anchor=S,
    bouton=Button(Framemid, text="Jouer à un QCM",bg=createbg, fg=createfg, command=Create)
    bouton.pack(side=LEFT, padx=5)#anchor=S,
    bouton=Button(Framebot, text="Quiter",bg=createbg, fg=createfg, command=Quit)
    bouton.pack(side=BOTTOM, padx=5)#anchor=S,
    fenetre.mainloop()

CreateOrPlay()
#print(ChosenQCM)
