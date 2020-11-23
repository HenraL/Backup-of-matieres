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
    """ Class for data gathering """
    def __init__(self,fileList): #-> None
        """ Defining the Globals """
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
        self.Date="{}/{}/{}".format(date.day,date.month,date.year)
        self.DateFile="{}_{}_{}".format(date.day,date.month,date.year)
        self.do=False
        self.c_choice=['Last name','First name','mark','gender','gap','Recovery main','T1_T1','T1_T2','T1_T3','T1_E1','T1_R1','T2_T1','T2_T2','T2_T3','T2_E2','T2_R2','TB']
        self.filelist=fileList
        # -------------------------------- Variables ----------------------------------------
        # self.Font="Algerian"
        self.Font="Times_New_Roman"
        #self.Font=""
        #self.Size=14
        #self.Size=10
        self.Size=8
        self.WBG="Orange"
        self.FBG="White"
        self.LBG="grey"
        self.WFG="black"
        self.FFG="blue"
        self.LFG="white"
        self.F1=FLAT
        self.F1T=GROOVE
        self.F1b=GROOVE
        self.F1q=FLAT
        self.hfDE="blue"
        self.hbDE="green"
        self.hfEN="blue"
        self.hbEN="green"
        self.hfFR="blue"
        self.hbFR="green"
        self.hfES="blue"
        self.hbES="green"
        self.hfq="blue"
        self.hbq="green"
        self.BACKGround="#2CDF85"
        self.background=self.BACKGround
        self.cleanBackground="White"
        # ---------------------------------------------------- Defs ----------------------------------------------------

    def Last_name(self):
        """ Getting last name """
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est votre nom de famille?")
        TT.geometry("230x100")
        TT.minsize(230,100)
        ST=Label(TT, text="Veuillez entrer votre nom de famille.")
        ST.pack(fill=X,pady=20)
        value = StringVar() 
        value.set("Nom de famille")
        entree = Entry(TT, textvariable=value, width=30)
        entree.pack()
        B2=Button(TT,text="Valider",command=getButton2)
        B2.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        TT.mainloop()
    def First_name(self):
        """ Getting first name """
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est votre prénom?")
        TT.geometry("230x100")
        TT.minsize(230,100)
        Framemain=Frame(TT, padx=20, pady=20)
        ST=Label(TT, text="Veuillez entrer votre prénom.")
        ST.pack(fill=X,pady=20)
        value = StringVar() 
        value.set("Prénom")
        entree = Entry(TT, textvariable=value, width=30)
        entree.pack()
        B2=Button(TT,text="Valider",command=getButton2)
        B2.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        TT.mainloop()
    def Female(self):
        """ Defining slot as Female """
        self.gender="Female"
        self.processedGender="G"
    def Male(self):
        """ Defining slot as Male """
        self.gender="Male"
        self.processedGender="B"
    def Gender(self):
        """ Getting the gender of the user """
        def getButton1():
            TT.destroy()
            get.Female(self)
        def getButton2():
            TT.destroy()
            get.Male(self)
        
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Quel est votre genre?")
        TT.geometry("230x100")
        TT.minsize(230,100)
        ST=Label(TT, text="Quel est votre genre?")
        ST.pack(fill=X,pady=20)
        B1=Button(TT,text="Feminin",command=getButton1)
        B1.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        B2=Button(TT,text="Masculin",command=getButton2)
        B2.pack(side=LEFT,padx=30,pady=0)#anchor=CENTER,,fill=Y
        TT.mainloop()
    def write(self,chosen):
        """ Appending the Gender of the user """
        chosen["T{}".format(self.processedGender)]=""
        chosen["gender"]=self.gender
    def actTimeTurn(self):
        """ Getting info for the different rounds, gap and projects """
        def writeGetTurn(self,actTimeTurn_results):
            # print ("self.Turns={}".format(self.Turns))
            # print ("self.ShowList={}".format(self.ShowList))
            self.ShowList+=1
            self.actTimeTurn_results=actTimeTurn_results
        chosenList=[]
        # print("Checker (ShowList)")
        # print("self.ShowList={}".format(self.ShowList))
        if self.ShowList==4:
            chosenList=self.lists[0]#self.Rmc
            # print("chosenList='{}'".format(chosenList))
        elif self.ShowList==3:
            chosenList=self.lists[1]
            # print("chosenList='{}'".format(chosenList))
        elif self.ShowList<3:
            if self.gender=="Female":
                chosenList=self.lists[2]#self.TG
                # print("chosenList='{}'".format(chosenList))
            elif self.gender=="Male":
                chosenList=self.lists[3]#self.TB
                # print("chosenList='{}'".format(chosenList))
        # print("window")
        TT=Tk()
        def getTurn(*arg):
            comunalList=["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25","7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31","0","1","2","0","2","4"]
            actTimeTurn_results=variable.get()
            # print("actTimeTurn_results='{}'".format(actTimeTurn_results))
            if actTimeTurn_results in comunalList:
                if actTimeTurn_results !="" and actTimeTurn_results != "---------Choisissez un élément---------":
                    writeGetTurn(self,actTimeTurn_results)
                    # print("actTimeTurn_results='{}',type={}".format(actTimeTurn_results,type(actTimeTurn_results)))
                    TT.destroy()
                else:print("Merci de bien vouloir faire un choix autre que ---------Choisissez un élément---------")
            else:print("Merci de bien vouloir faire un choix")
        TT['bg']=self.cleanBackground
        TT.title("Temps du tour de terrain n°x du x ème 800")
        TT.geometry("424x200")
        TT.minsize(424,200)
        FrameTitle = LabelFrame(TT, text="800 n°{}".format(self.BigRounds+1), padx=20, pady=20)
        FrameTitle.pack(fill="both", expand="yes")
        FrameSubTitle = LabelFrame(FrameTitle, text="{}".format(self.messages[self.Turns-1]), padx=20, pady=20)
        FrameSubTitle.pack(fill="both", expand="yes")
        # print("chosenList[0]='{}'".format(chosenList[0]))
        variable = StringVar(FrameSubTitle)
        variable.set(chosenList[0])
        opt = OptionMenu(FrameSubTitle, variable, *chosenList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")
        Quit=Button(TT, text="Confirmer", command=getTurn)
        Quit.pack()
        TT.mainloop()
    
    def appendTurns(self,chosen):
        """ Appending information to the list chosen """
        if self.ShowList==1:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 1
            # print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==2:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 2
            # print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==3:
            chosen["T{}_T{}".format(self.BigRounds+1,self.Turns)]=self.actTimeTurn_results #Tour piste 3
            # print("chosen[\"T{}_T{}\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.Turns-1,self.actTimeTurn_results))
        elif self.ShowList==4 and self.BigRounds==0:
            chosen["T{}_E{}".format(self.BigRounds+1,self.Turns-3)]=self.actTimeTurn_results #Projet
            # print("chosen[\"T{}_E1\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==5 and self.BigRounds==0:
            chosen["T{}_R{}".format(self.BigRounds+1,self.Turns-4)]=self.actTimeTurn_results #Récup
            # print("chosen[\"T{}_R1\"]=self.actTimeTurn_results {} #Tour piste 1".format(self.BigRounds+1,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==4 and self.BigRounds==1:
            chosen["T{}_E{}".format(self.BigRounds+1,self.Turns-2)]=self.actTimeTurn_results #Projet
            # print("chosen[\"T{}_E{}\"]=self.actTimeTurn_results {} #Tour piste 2".format(self.BigRounds+1,self.Turns-2,self.actTimeTurn_results))#,Turns+1
        elif self.ShowList==5 and self.BigRounds==1:
            chosen["T{}_R{}".format(self.BigRounds+1,self.Turns-3)]=self.actTimeTurn_results #Récup
            # print("chosen[\"T{}_R{}\"]=self.actTimeTurn_results {} #Tour piste 2".format(self.BigRounds+1,self.Turns-3,self.actTimeTurn_results))#,Turns+1
            self.do=True
        else:
            print("\n\n\n\n\nIndex not avaidable\n\n\n\n\n")
    def debug(c_choice,chosen):
        """ Show the content of the list chosen """
        for i in range(len(c_choice)):
            print("{}={}".format(c_choice[i],chosen[c_choice[i]]))
    def FileName(self):
        """ Getting the name of the file to open for process """
        def choosenFile(self,filename):
            self.filename=filename
        def chosenFile():
            filename = int(FIILE.get())
            TT.destroy()
            choosenFile(self,filename)
        TT = Tk()
        TT.title("Quel fichier désirez-vous voir?")
        Frame1 = Frame(TT, borderwidth=2, relief=FLAT, bg="white")
        Frame1.pack(side=TOP, padx=10, pady=10)
        Framebot = Frame(TT, borderwidth=2, relief=FLAT)
        Framebot.pack(side=BOTTOM, padx=0, pady=0)
        ligne,colonne=0,0
        for I in range(len(self.filelist)):
            Label(Frame1, text="Index repère: {} nom du fichier: {} ".format(I+1,self.filelist[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
            if ligne==20:
                ligne,colonne=0,colonne+1
            else:ligne+=1
        bla = Label(Framebot, text="Quel fichier voulez-vous voir:")
        bla.pack(side=LEFT)
        FIILE=Spinbox(Framebot, from_=1, to=len(self.filelist), increment=1)
        FIILE.pack(side=LEFT, padx=5)
        bouton=Button(Framebot, text="Exécuter", command=chosenFile)
        bouton.pack(side=LEFT, padx=5)
        TT.mainloop()

    def fileinfo(self):
        """ Processing Data Files For Viewing """
        f=open("data/{}".format(self.filelist[self.filename]),"r")
        d=f.read()
        f.close()
        self.ShowListBoard={}
        element1=""
        word=""
        b=0
        for i in d: 
            if i=="\n":
                element1=word
                self.ShowListBoard[self.c_choice[b]]=str(element1)
                element1=""
                word=""
                b+=1
            else:
                word+=str(i)
        print(self.ShowListBoard)
    def updatelist(self):
        """ Refreshing the file list """
        self.fileList=os.listdir("data")         

class make(get):
    """ Class for graphics and other parts of the program"""
    def main_menu(self):
        """ Main menu Window """
        def QUIT():
            """ Exit program calling """
            TT.destroy()
            make.QUITT(GI)
        def cn():
            """ Create new data file calling """
            TT.destroy()
            get.updatelist(self)
            make.create_new(GI,chosen,c_choice)
            create.file(GI,chosen,c_choice)
        def dss():
            """ Show stats of files calling """
            TT.destroy()
            make.show_stats(GI)
        TT=Tk()
        TT['bg']=self.cleanBackground
        TT.title("Menu Principal")
        TT.geometry("530x140")
        TT.minsize(530,140)
        FrameText=Frame(TT, borderwidth=1, relief=self.F1, bg=self.FBG)
        FrameText.pack(fill=X,side=TOP)
        FrameChoiceButtons=Frame(TT, borderwidth=1, relief=self.F1, bg=self.FBG)
        FrameChoiceButtons.pack(fill=X,side=TOP,pady=0.5)
        FrameQuit=Frame(TT, borderwidth=1, relief=self.F1, bg=self.FBG)
        FrameQuit.pack(fill=X, side=TOP,pady=0.5)
        SubFrameQuit=Frame(FrameQuit, borderwidth=0, relief=self.F1, bg=self.FBG)
        SubFrameQuit.pack(fill=X, side=BOTTOM, pady=0.5)
        ST=Label(FrameText, text="Menu Principal")
        ST.pack(fill=X,pady=0)
        DT=Label(FrameText, text="Que voulez-vous faire?")
        DT.pack(fill=X,pady=5)
        B1=Button(FrameChoiceButtons,text="Ajouter les temps d'un nouveau deux fois 800",command=cn)
        B1.pack(side=LEFT,padx=5,pady=0)#anchor=CENTER,,fill=Y
        B2=Button(FrameChoiceButtons,text="Voir les temps d'un deux fois 800 déjà présent",command=dss)
        B2.pack(side=LEFT,padx=5,pady=0)#anchor=CENTER,,fill=Y
        B3=Button(FrameQuit,text="Quitter",command=QUIT)
        B3.pack(anchor=CENTER, side=TOP,padx=5,pady=0)#anchor=CENTER,,fill=Y
        LC=Label(FrameQuit,text="{} Créé par Henry Letellier".format(chr(169)))
        LC.pack(side=RIGHT,pady=0)
        TT.mainloop()
    
    def create_new(self,chosen,c_choice):#,chosen,c_choice
        """ Main def for file_data collection """
        get.Gender(self)#
        print("write")
        get.write(self,chosen)#
        print("\n\n\nLOOP\n\n\n")
        make.mainLoop(self,chosen,c_choice)
        print("{} Créé par Henry Letellier".format(chr(169)))
        get.debug(c_choice,chosen)
        
    def show_stats(self):
        """ Main def for Stat viewing """
        get.FileName(self)
        get.fileinfo(self)
    def small_loop(self,chosen):
        """ Inner loop for data gathering """
        self.ShowList=0
        while self.Turns <6:
            # print("\n\n\nLOOP range\n\n\n")
            # print("\n\n\n\n\n\nShowList={}\n\n\n\n\n\n".format(self.ShowList))
            # print("actTimeTurn")
            get.actTimeTurn(self)#,self.BigRounds+1
            # print("appendTurns")
            get.appendTurns(self,chosen)#
            # print("ShowList={}".format(self.ShowList))
            # print("self.Turns={}".format(self.Turns))
            get.debug(c_choice,chosen)
            # print("\n ShowList={} \n".format(self.ShowList))
            # print("\n choicemade={} \n".format(self.choicemade))
            self.Turns+=1
    def mainLoop(self,chosen,c_choice):
        """ Outer loop for data gathering"""
        self.ShowList=0
        self.BigRounds=0
        self.cont=True
        self.choicemade=True
        while self.BigRounds <2:
            print("\n\n\nLOOP Big\n\n\n")
            self.Turns=1
            make.small_loop(self,chosen)
            # get.debug(c_choice,chosen)
            # print("self.Turns={}".format(self.Turns))
            self.ShowList=1
            # print("self.ShowList={}".format(self.ShowList))
            # self.BigRounds+=1
            self.BigRounds+=1
    
    def QUITT(self):
        """ Exit def """
        print("Au revoir et à la prochaine fois")
        aaaa = Tk()
        aaaa['bg']=self.cleanBackground
        aaaa.title("Language:")
        aaaa.geometry("250x200")
        aaaa.minsize(250,200)
        #aaaa.iconbitmap("the icone of the software in.ico")
        aaaa.config(background="#2CDF85")
        label = Label(aaaa, text="Au revoir et à la prochaine fois {}{}{}{}{}{}{}{}{}".format(chr(40),chr(9679),chr(180),chr(92),chr(95),chr(47),chr(96),chr(9679),chr(41)), font=(self.Font,self.Size), bg=self.LBG, fg=self.LFG)#🙂
        label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
        bouton=Button(aaaa, text="Fermer", font=(self.Font,self.Size), bg=self.WBG, fg=self.WFG, command=aaaa.destroy ,activebackground=self.hbq, activeforeground=self.hfq)
        bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
        aaaa.mainloop()
        sys.exit(0)

class create(get):
    """ Class for dealing with long time data storage """
    def file(self,chosen,c_choice):
        if self.do==True:
            f=open("data/2x800_du_{}.txt".format(self.DateFile),"w")
            f.write("{}".format(self.Date))#\n,end=""
            for i in range(len(self.c_choice)):
                f.write("{}\n".format(chosen[c_choice[i]]))#,end=""\n
            f.close()
    def sc(self):
        f=open("S.txt","r")
        check=f.read()
        f.close()
        self.check=[]
        element1=""
        element2=""
        word=""
        for i in check:
            if i=="\n":
                element2=word
                self.check.append({"name":"{}".format(element1),"done":"{}".format(element2)})
                element2=""
            elif i=="|":
                element1=word
                word=""
            else:
                word+=str(i)
    def update(self):
        f=open("S.txt","w")
        for i in range(len(self.check)):
            f.write("{}|{}\n".format(self.check[i]["name"],self.check[i]["done"]),end="")
        f.close()


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
GI=get(fileList)#.__init__
MaInLoOp=True
while MaInLoOp==True:
    make.main_menu(GI)
