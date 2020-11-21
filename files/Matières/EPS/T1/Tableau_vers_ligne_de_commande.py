from tkinter import*
from tkinter.filedialog import *
import datetime, os
from lists import *
# print(Date)
    # print(DateFile)
    # print(fileList)
    # print(chosenFile)
    # print(path)
    # print(Recovery_main)
    # print(Recovery_main_corresponds)
    # print(Level_5_not_acquired)
    # print(Level_5_acquired)
    # print(mark)
    # print(TG)
    # print(TB)
    # print(Project_Gap_main)

# chosen={"Last name":"","First name":"","mark":"","gender":"","gap":"","Recovery main":""}

class get:
    def __init__(self): #-> None
        self.Turn=0
        self.gender=None
        self.Rmc=["---------Choisissez un élément---------","0","1","2"] #Recovery_main_corresponds
        self.PGmc=["---------Choisissez un élément---------","0","2","4"] #Project_Gap_main_corresponds
        self.TG=["---------Choisissez un élément---------","9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"]
        self.TB=["---------Choisissez un élément---------","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]
        self.actTimeTurn_results=""
        self.BigRounds=1
        self.Turns=0
        self.ShowList=""
        self.actTimeTurn_results=""
        self.chosenList=[]
        self.lists=[
            ["---------Choisissez un élément---------","0","1","2"], #recuperation
            ["---------Choisissez un élément---------","0","2","4"], #ecart projet
            ["---------Choisissez un élément---------","9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"],
            ["---------Choisissez un élément---------","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]]
        self.messages=["Tour n°1","Tour n°2","Tour n°3","Ecart Projet","Récupération"]
    def Female(self):
        self.gender="Female"
        self.processedGender="G"
    def Male(self):
        self.gender="Male"
        self.processedGender="B"
    def Gender(self):
        def getButton1():
            TT.destroy()
            get.Female(self)
        def getButton2():
            TT.destroy()
            get.Male(self)
        
        TT=Tk()
        TT['bg']="White"
        TT.title("Quel est votre sexe?")
        TT.geometry("230x100")
        TT.minsize(230,100)
        ST=Label(TT, text="Quel est votre sexe?")
        ST.pack(fill=X,pady=20)
        B1=Button(TT,text="Feminin",command=getButton1)
        B1.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        B2=Button(TT,text="Masculin",command=getButton2)
        B2.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        TT.mainloop()
    def write(self,chosen):
        chosen["T{}".format(self.processedGender)]=""
        chosen["gender"]=self.gender
    def actTimeTurn(self):
        def writeGetTurn(self,actTimeTurn_results):
            print ("self.Turns={}".format(self.Turns))
            # self.Turns+=1
            print ("self.ShowList={}".format(self.ShowList))
            self.ShowList+=1
            self.actTimeTurn_results=actTimeTurn_results
        chosenList=[]
        print("Checker (ShowList)")
        print("self.ShowList={}".format(self.ShowList))
        if self.ShowList==4:
            chosenList=self.lists[0]#self.Rmc
            print("chosenList='{}'".format(chosenList))
        elif self.ShowList==3:
            chosenList=self.lists[1]
            print("chosenList='{}'".format(chosenList))
        elif self.ShowList<3:
            if self.gender=="Female":
                chosenList=self.lists[2]#self.TG
                print("chosenList='{}'".format(chosenList))
            elif self.gender=="Male":
                chosenList=self.lists[3]#self.TB
                print("chosenList='{}'".format(chosenList))
        print("window")
        TT=Tk()
        def getTurn(*arg):
            comunalList=["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31","0","1","2","0","2","4"]
            actTimeTurn_results=variable.get()
            print("actTimeTurn_results='{}'".format(actTimeTurn_results))
            if actTimeTurn_results in comunalList:
                if actTimeTurn_results !="" and actTimeTurn_results != "---------Choisissez un élément---------":
                    writeGetTurn(self,actTimeTurn_results)
                    print("actTimeTurn_results='{}',type={}".format(actTimeTurn_results,type(actTimeTurn_results)))
                    TT.destroy()
                else:print("Merci de bien vouloir faire un choix autre que ---------Choisissez un élément---------")
            else:print("Merci de bien vouloir faire un choix")
        TT['bg']="White"
        TT.title("Temps du tour de terrain n°x du x ème 800")
        TT.geometry("424x200")
        TT.minsize(424,200)
        FrameTitle = LabelFrame(TT, text="800 n°{}".format(self.BigRounds+1), padx=20, pady=20)
        FrameTitle.pack(fill="both", expand="yes")
        FrameSubTitle = LabelFrame(FrameTitle, text="{}".format(self.messages[self.Turns-1]), padx=20, pady=20)
        FrameSubTitle.pack(fill="both", expand="yes")
        print("chosenList[0]='{}'".format(chosenList[0]))
        variable = StringVar(FrameSubTitle)
        variable.set(chosenList[0])
        opt = OptionMenu(FrameSubTitle, variable, *chosenList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")
        Quit=Button(TT, text="Confirmer", command=getTurn)
        Quit.pack()
        TT.mainloop()
    
    def appendTurns(self,chosen):
        if self.ShowList==1:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 1
            print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==2:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 2
            print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==3:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 3
            print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==4 and self.BigRounds==0:
            chosen["T{}_E{}".format(self.BigRounds+1,self.Turns-3)]=self.actTimeTurn_results #Projet
            print("chosen[\"T{}_E1\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==5 and self.BigRounds==0:
            chosen["T{}_R{}".format(self.BigRounds+1,self.Turns-4)]=self.actTimeTurn_results #Récup
            print("chosen[\"T{}_R1\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==4 and self.BigRounds==1:
            chosen["T{}_E{}".format(self.BigRounds+1,self.Turns-3)]=self.actTimeTurn_results #Projet
            print("chosen[\"T{}_E2\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==5 and self.BigRounds==1:
            chosen["T{}_R{}".format(self.BigRounds+1,self.Turns-4)]=self.actTimeTurn_results #Récup
            print("chosen[\"T{}_R2\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
    def debug(c_choice,chosen):
        for i in range(len(c_choice)):
            print("{}={}".format(c_choice[i],chosen[c_choice[i]]))

class make(get):
    def small_loop(self,chosen):
        while self.Turns <6:
            print("\n\n\nLOOP range\n\n\n")
            print("actTimeTurn")
            get.actTimeTurn(self)#,self.BigRounds+1
            print("appendTurns")
            get.appendTurns(self,chosen)#
            print("ShowList={}".format(self.ShowList))
            print("self.Turns={}".format(self.Turns))
            get.debug(c_choice,chosen)
            print("\n ShowList={} \n".format(self.ShowList))
            print("\n choicemade={} \n".format(self.choicemade))
            self.Turns+=1
    def mainLoop(self,chosen):
        self.ShowList=0
        self.BigRounds=0
        self.cont=True
        self.choicemade=True
        while self.BigRounds <2:
            print("\n\n\nLOOP Big\n\n\n")
            self.Turns=1
            make.small_loop(self,chosen)
            get.debug(c_choice,chosen)
            print("self.Turns={}".format(self.Turns))
            self.ShowList=1
            print("self.ShowList={}".format(self.ShowList))
            # self.BigRounds+=1
            self.BigRounds+=1


for i in range(2):
    for k in range(3):
        chosen["T{}_T{}".format(i+1,k+1)]=""
    if i==0:
        chosen["T{}_E1".format(i+1)]=""
        chosen["T{}_R1".format(i+1)]=""
    elif i==1:
        chosen["T{}_E2".format(i+1)]=""
        chosen["T{}_R2".format(i+1)]=""

print("\n\n\nchosen={}\n\n\n".format(chosen))
GI=get()#.__init__
get.Gender(GI)#
print("write")
get.write(GI,chosen)#
print("\n\n\nLOOP\n\n\n")
make.mainLoop(GI,chosen)
print("Créé par Henry Letellier")
get.debug(c_choice,chosen)