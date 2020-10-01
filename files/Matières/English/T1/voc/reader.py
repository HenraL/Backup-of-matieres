class read:
    def scanQCMFolder():
        file=os.listdir("QCM")
        return file
    def AskQCMToPlay(QCMFolder):
        def GetChosenQCM():
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

    def read(file):
        f=open(file,"r")
        readfile=f.read()
        f.close()
        return readfile
class createQCMList:
    read.scanQCMFolder()
    read.AskQCMToPlay(file)
    #PlayQcm.scanScoreFolder()
    #PlayQcm.writeAndCreateScore(QCMFolder[ChosenQCM],0,0)
    qcmopen="QCM/{}".format(file[ChosenQCM])
    f=open(qcmopen,"r")
    FILE=f.read()
    f.close()
    QCM,d,question1,info2=[],len(FILE),0,0
    try:
        answertype,question1,info2=1,0,0
        for letters in FILE:
            if letters=="\n" and answer==1:
                question1cont,info2=0,0
                QCM.append({"date":"{}".format(question1cont),"event":"{}".format(info2cont)})
            elif letters==",":continue
            else:
                if question1==1:
                    info2,info2cont=1,letters
                else:
                    question1,question1cont=1,letters
    def processData(readfile):
        term=""
        word=""
        for i in readfile:
            if i=="\n":
                term=""
            elif i==" ":
                term+=" {}".format(word)
                word=""
            elif 

# {"date":"de 1337-1453 J.-C.","event":"la Guerre de 100 ans"},
