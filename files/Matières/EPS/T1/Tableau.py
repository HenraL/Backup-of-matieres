from tkinter import*
from tkinter.filedialog import *
import datetime, os
date=datetime.datetime.now()

gender=0
time=0
markTime=0
markGap=0
markRecovery=0

Project_Gap_main=["+ de 15 secondes","15-10 secondes","<10 secondes"]
Project_Gap_main_corresponds=["0","2","4"]

Recovery_main=["Trop passive, pas de liaison directe avec l'effort consenti",
               "Récupération active immédiatement après l'effort (course lente, étirements)",
               "Toutes les dimensions de la récupération sont présentes, chronologiquement positionnées. On conjure l'effort fait et l'effort à faire."]

Recovery_main_corresponds=["0","1","2"]

Level_5_not_acquired={"mark":["0,7","1,4","2,1","2,8","3,5","4,2","4,9","5,6","6,3"],
                      "TG":["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39"],
                      "TB":["7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29"]}
Level_5_acquired={"list1":{"mark":["7","7,7","8,4","9,1","9,8","10,5"],
                           "TG":["6'26","6'20","6'13","6'07","6'01","5'55"],
                           "TB":["5'19","5'11","5'03","4'55","4'51","4'47"]}
                  ,"list2":{"mark":["11,2","11,9","12,6","13,3","14"],
                            "TG":["5'49","5'43","5'37","5'31","5,25"],
                            "TB":["4'43","4'40","4'37","4'34","4'31"]}}

mark=["0,7","1,4","2,1","2,8","3,5","4,2","4,9","5,6","6,3","7","7,7","8,4","9,1","9,8","10,5","11,2","11,9","12,6","13,3","14"]
TG=["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"]
TB=["7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]
chosen={"Last name":"","First name":"","mark":"","gender":"","gap":"","Recovery main":""}
chosen["T{}".format(chosen["gender"])]=""




#print(chosen)
#print(TB)
##print(TG)
#print(mark)
#print(Level_5_acquired)
#print(Level_5_not_acquired)
#print(Recovery_main_corresponds)
#print(Recovery_main)
#print(Project_Gap_main_corresponds)
#print(Project_Gap_main)

class root():
    # def __init__(self,gender,time,markTime,markGap,markRecovery,data,lastName,firstName):
    #     self.gender=gender
    #     self.time=time
    #     self.mT=markTime
    #     self.mG=markGap
    #     self.mR=markRecovery
    #     self.file=data
    #     self.LN=lastName
    #     self.FN=firstName
    #     self.Date="{}/{}/{}".format(date.day,date.month,date.year)
    #     self.DateFile="{} {} {}".format(date.day,date.month,date.year)
    #     self.filepath=""
    #     self.fileList=os.listdir("data")
    #     self.path="data/{}".format(self.chosenFile)
    class mainVars():
        def dumb():print("dumb")
        def __init__(self,gender,time,markTime,markGap,markRecovery,data,lastName,firstName):
            self.gender=gender
            self.time=time
            self.mT=markTime
            self.mG=markGap
            self.mR=markRecovery
            self.file=data
            self.LN=lastName
            self.FN=firstName
            self.Date="{}/{}/{}".format(date.day,date.month,date.year)
            self.DateFile="{} {} {}".format(date.day,date.month,date.year)
            self.filepath=""
            self.fileList=os.listdir("data")
            self.path="data/{}".format(self.chosenFile)
            # self.

        # def printer(self):
        #     print(self.gender)
        #     print(self.time)
        #     print(self.mT)
        #     print(self.mG)
        #     print(self.mR)
        #     print(self.file)
        #     print(self.LN)
        #     print(self.FN)
        #     print(self.Date)
        #     print(self.DateFile)
        #     print(self.filepath)
        #     print(self.fileList)
        #     print(self.path)
        #     print("Done")

    class systemDealing(mainVars):
        def pause():
            pause=input("Please press enter to continue...")
        def openFile(self):
            get.file(self)
            f=open(self.path,"r")
            data=f.read()
            f.close()
            #for i in data:
            #   if 
    class get(mainVars):
        def file(self):
            def GetChosenSheet(self):
                filepath = int(liister.get())
                self.filepath=filepath
                lister.destroy()
                return filepath
            #self.filepath = askopenfilename(title="Choisissez le tableau a ouvrir",filetypes=[('Fichiers python','.py'),('Tous les fichiers','.*')])
            lister = Tk()
            lister['bg']="White"
            lister.title("Choix Tableaux:")
            lister.geometry("250x200")
            lister.minsize(250,200)
            Frame1 = Frame(lister, borderwidth=2, relief=FLAT, bg="white")
            Frame1.pack(side=TOP, padx=10, pady=10)
            Framebot = Frame(lister, borderwidth=2, relief=FLAT)
            Framebot.pack(side=BOTTOM, padx=0, pady=0)
            colonne,ligne=0,0
            for I in range(len(self.fileList)):
                Label(Frame1, text="Index: {} Tableau: {} ".format(I+1,self.fileList[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
                if ligne==20:
                    ligne,colonne=0,colonne+1
                else:
                    ligne+=1
            bla = Label(Framebot, text="Quel Tabeau voulez-vous ouvrir:")
            bla.pack(side=LEFT)#anchor=S,
            liister=Spinbox(Framebot, from_=0, to=len(self.fileList), increment=1)
            liister.pack(side=LEFT, padx=5)#anchor=S,
            bouton=Button(Framebot, text="Ouvir", command=GetChosenSheet)
            bouton.pack(side=LEFT, padx=5)#anchor=S,
            lister.mainloop()
        def gender():
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
            fenetre.mainloop()
        def Current(self):
            self.currentd=os.getcwd()
            return self.currentd
        def Name(self):
            if os.path.exists("{}".format(self.chosenFile))==True:
                self.filenamebool=True
            else:
                self.filenamebool=False
            return self.filenamebool
            

    class windows(mainVars):
        def MarkGapTkinter(self):
            gap=Tk()
            label = Label(fenetre, text="Ecart du Projet")
            label.pack()
        def ShowResults(self):
            if self.fromfile==True:
                root.systemDealing.openFile(self)
        #mainVars.printer(self)

        def call(self):
            root.get.file(self)
gender="ee"
time="ee"
markTime="ee"
markGap="ee"
markRecovery="ee"
data="ee"
lastName="ee"
firstName="ee"
rMainVars=root.mainVars#()
Init=rMainVars.__init__(self,gender,time,markTime,markGap,markRecovery,data,lastName,firstName)
rSysDealing=root.systemDealing#()#rMainVars)
rGet=root.get#()#rMainVars)
rWin=root.windows#rMainVars)
# SELF=rMainVars.__init__(self,gender,time,markTime,markGap,markRecovery,data,lastName,firstName)
rWin.call(Init)
# root.windows.call()

fenetre = Tk()

fenetre.mainloop()
