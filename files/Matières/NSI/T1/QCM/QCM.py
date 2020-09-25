from tkinter import*
import os
BG="White"
FG="Black"
AFQ="blue"
ABQ="green"
class CreateQCM:
    # def __init__(self):
        #d
    
    def createQCMfile():
        def getFileName():
            FileName=CreateQCM.createQCMfile.e.get()
            CreateQCM.createQCMfile.fenetre.destroy()
            print(FileName)
            return FileName
        fenetre=Tk()
        fenetre['bg']="White"
        fenetre.title("Language:")
        fenetre.geometry("250x200")
        fenetre.minsize(250,200) 
        Frame1=LabelFrame(fenetre, borderwidth=2, relief=FLAT, bg=BG)
        Frame1.pack(padx=10, pady=10, fill=X, anchor=CENTER)
        value = StringVar() 
        value.set("texte par défaut")
        entree = Entry(Frame1, width=30)#, textvariable=stringVar
        entree.pack()
        BouttonValider=Button(fenetre, text="Valider", bg=BG, fg=FG, command=getFileName ,activebackground=ABQ, activeforeground=AFQ)
        BouttonValider.pack()
        fenetre.mainloop()

#CreateQCM.createQCMfile()
#print(CreateQCM.createQCMfile.getFileName)

class PlayQcm:
    def scanQCMFolder():
        global QCMFolder
        QCMFolder=os.listdir("QCM")
        return QCMFolder
    
    def AskQCMToPlay(QCMFolder):
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
        for I in range(len(QCMFolder)):
            Label(Frame1, text="Index repère: {} nom du fichier: {} ".format(I+1,QCMFolder[I]), borderwidth=1,bg="white").grid(row=ligne, column=colonne)
            if ligne==20:
                ligne,colonne=0,colonne+1
            else:ligne+=1
        bla = Label(Framebot, text="Quel Niveau voulez-vous exécuter:")
        bla.pack(side=LEFT)#anchor=S,
        QCMM=Spinbox(Framebot, from_=1, to=len(QCMFolder), increment=1)
        QCMM.pack(side=LEFT, padx=5)#anchor=S,
        bouton=Button(Framebot, text="Exécuter", command=GetChosenQCM)
        bouton.pack(side=LEFT, padx=5)#anchor=S,
        fenetre.mainloop()
    
    def scanScoreFolder():
        ScoreFolder=os.listdir("Score")
        return ScoreFolder
    
    def writeAndCreateScore(ScoreFileName,points,erreur):
        f=open("Score/{}".format(ScoreFileName),"w")
        f.write("{}\n{}".format(points,erreur))
        f.close()
class AnswerRandomiserAndChecker:
    def randomiser():
        
class AnswerQMC:
    def AnswerQMC3():
        print("e")
    def AnswerQMC4():
        print("e")

class createQCMList:
    PlayQcm.scanQCMFolder()
    PlayQcm.AskQCMToPlay(QCMFolder)
    PlayQcm.scanScoreFolder()
    PlayQcm.writeAndCreateScore(QCMFolder[ChosenQCM],0,0)
    qcmopen="QCM/{}".format(QCMFolder[ChosenQCM])
    f=open(qcmopen,"r")
    FILE=f.read()
    f.close()
    QCM,d,question1,info2,info3,info4,info5,answer=[],len(FILE),0,0,0,0,0,0
    try:
        answertype,question1,info2,info3,info4,info5,answer=1,0,0,0,0,0,0
        for letters in FILE:
            if letters=="\n" and answer==1:
                question1cont,info2,info3,info4,info5,answer=0,0,0,0,0,0
                QCM.append({"question":"{}".format(question1cont),"reponse1":"{}".format(info2cont),"reponse2":"{}".format(info3cont),"reponse3":"{}".format(info4cont),"reponse4":"{}".format(info5cont),"answer":"{}".format(answercont)})
            elif letters==",":continue
            else:
                if info5==1:answer,answercont=1,letters
                elif info4==1:info5,info5cont=1,letters
                elif info3==1:info4,info4cont=1,letters
                elif info2==1:info3,info3cont=1,letters
                elif question1==1:info2,info2cont=1,letters
                else:question1,question1cont=1,letters
    except:
        answertype,question1,info2,info3,info4,answer=2,0,0,0,0,0
        for letters in FILE:
            if letters=="\n" and answer==1:
                question1cont,info2,info3,info4,answer=0,0,0,0,0
                QCM.append({"question":"{}".format(question1cont),"reponse1":"{}".format(info2cont),"reponse2":"{}".format(info3cont),"reponse3":"{}".format(info4cont),"answer":"{}".format(answercont)})
            elif letters==",":continue
            else:
                if info4==1:answer,answercont=1,letters
                elif info3==1:info4,info4cont=1,letters
                elif info2==1:info3,info3cont=1,letters
                elif question1==1:info2,info2cont=1,letters
                else:question1,question1cont=1,letters
    if answertype==1:
        for i in range(len(QCM)):
            AnswerQMC.AnswerQMC3()
    elif answertype==2:
        for i in range(len(QCM)):
            AnswerQMC.AnswerQMC4
