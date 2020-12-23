from tkinter import *
import os
class root:
    def __init__(self):
        self.a=2
        self.Background_colour="white"
        self.bg="Grey"
        self.fg="White"
class get(root):
    def file_name(self):
        files=os.listdir()
        TT=Tk()
        TT.geometry("200x200")
        TT['bg']=self.Background_colour
        TT.Title("Quel fichier désirez-vous ouvrir?")
        LM=Label(TT,text="Quel fichier désirez-vous ouvrir?",bg=self.bg,fg=self.fg)
        LM.pack(side=TOP,fill=X)
        for I in range(len(files)):
            Label(Frame1, text="Index repère: {} nom du fichier: {} ".format(I,files[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
            if ligne==20:
                ligne,colonne=0,colonne+1
            else:ligne+=1

RI=root()
