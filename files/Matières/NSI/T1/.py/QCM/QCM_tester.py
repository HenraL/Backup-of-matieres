import os
def refreshQCMS(files):#QCMS
    global QCMS
    QCMS=os.listdir("{}".format(files))
    return QCMS
def refreshscore(files):#Scores
    global Scores
    Scores=os.listdir("{}".format(files))
    return Scores

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
Font="Times_New_Roman"
Size=8
WBG="Orange"
FBG="White"
LBG="grey"
WFG="black"
FFG="blue"
LFG="white"
F1=FLAT
F1T=GROOVE
F1b=GROOVE
F1q=FLAT
hfDE="blue"
hbDE="green"
hfEN="blue"
hbEN="green"
hfFR="blue"
hbFR="green"
hfES="blue"
hbES="green"
hfq="blue"
hbq="green"

def goodbye():
    fenetre.destroy()
    main="n"
    print("Goodbye, See you next time")
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Language:")
    aaaa.geometry("250x200")
    aaaa.minsize(250,200)
    #aaaa.iconbitmap("the icone of the software in.ico")
    aaaa.config(background="#2CDF85")
    label = Label(aaaa, text="Goodbye, see you next time. :-)", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
    label = Label(aaaa, text="You have {} point(s).".format(score), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
    label = Label(aaaa, text="You have made {} mistake(s).".format(erreur), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


def chooseQCMS(QCMS):
    def GetChosenQCM():
        global ChosenQCM
        ChosenQCM = int(QCMM.get())
        fenetre.destroy()
        return ChosenQCM
    fenetre = Tk()
    fenetre.title("Quel QCM voulez-vous exécuter?")
    Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT, bg="white")
    Frame1.pack(side=TOP, padx=10, pady=10)
    Framebot = Frame(fenetre, borderwidth=2, relief=FLAT)
    Framebot.pack(side=BOTTOM, padx=0, pady=0)
    ligne,colonne=0,0
    for I in range(len(QCMS)):
        Label(Frame1, text="Index repère: {} nom du fichier: {} ".format(I+1,QCMS[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
        if ligne==20:
            ligne,colonne=0,colonne+1
        else:ligne+=1
    bla = Label(Framebot, text="Quel Niveau voulez-vous exécuter:")
    bla.pack(side=LEFT)#anchor=S,
    QCMM=Spinbox(Framebot, from_=1, to=len(QCMS), increment=1)
    QCMM.pack(side=LEFT, padx=5)#anchor=S,
    bouton=Button(Framebot, text="Exécuter", command=GetChosenQCM)
    bouton.pack(side=LEFT, padx=5)#anchor=S,
    fenetre.mainloop()

def pllay():
    refreshQCMS("QCM")
    chooseQCMS(QCMS)
    refreshscore("files")
    for I in range(len(QCMS)):
        print("Index repère: {} nom du fichier: {}".format(I+1,QCMS[I]))
    qcmopen="QCM/{}".format(QCMS[ChosenQCM])
    f=open(qcmopen,"r")
    a=f.read()
    f.close()
    d=len(a)
    question1=0
    info2=0
    info3=0
    info4=0
    info5=0
    answer=0
    QCM=[]
    try:
        answertype,question1,info2,info3,info4,info5,answer=1,0,0,0,0,0,0
        for z in a:
            if z=="\n" and answer==1:
                question1cont,info2,info3,info4,info5,answer=0,0,0,0,0,0
                QCM.append({"question":"{}".format(question1cont),"reponse1":"{}".format(info2cont),"reponse2":"{}".format(info3cont),"reponse3":"{}".format(info4cont),"reponse4":"{}".format(info5cont),"answer":"{}".format(answercont)})
            elif z==",":continue
            else:
                if info5==1:
                    answer=1
                    answercont=z
                elif info4==1:
                    info5=1
                    info5cont=z
                elif info3==1:
                    info4=1
                    info4cont=z
                elif info2==1:
                    info3=1
                    info3cont=z
                elif question1==1:
                    info2=1
                    info2cont=z
                else:
                    question1=1
                    question1cont=z
    except:
        answertype,question1,info2,info3,info4,answer=2,0,0,0,0,0
        for z in a:
            if z=="\n" and answer==1:
                question1cont,info2,info3,info4,answer=0,0,0,0,0
                QCM.append({"question":"{}".format(question1cont),"reponse1":"{}".format(info2cont),"reponse2":"{}".format(info3cont),"reponse3":"{}".format(info4cont),"answer":"{}".format(answercont)})
            elif z==",":continue
            else:
                if info4==1:
                    answer=1
                    answercont=z
                elif info3==1:
                    info4=1
                    info4cont=z
                elif info2==1:
                    info3=1
                    info3cont=z
                elif question1==1:
                    info2=1
                    info2cont=z
                else:
                    question1=1
                    question1cont=z

    if answertype==1:
        for i in range(len(QCM)):
            3
    elif answertype==2:
        for i in range(len(QCM)):
            4
else:print("votre fichier as trop ou pas assez de mots pour fonctionner.\nLe QCM doit avoir:\n- Soit trois réponses\n- Soit quatres réponses.")
print(QCM)
def create():
    print("e")
def goodbye():
    print("e")

def CreateOrPlay():
    def Play():
        fenetre.destroy()
        pllay()
    def Create():
        fenetre.destroy()
        create()
    def Quit():
        fenetre.destroy()
        goodbye()
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


