from random import*
from tkinter import*
import os, platform, datetime
dateorevent=["date","event"]
qdateorevent=["Quand a été","Que s'est-il passé"]
fdateorevent=["La bonne date", "Le bon évènement"]
edateorevent=["e",""]
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)
TIME="{}:{}:{}".format(date.hour,date.minute,date.second)
score,erreur,ganswer,wrung=0,0,0,0
# 
# -------------------------------- Variables ----------------------------------------

#Font="Algerian"
Font="Times_New_Roman"
#Font=""
#Size=14
#Size=10
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
# ---------------------------------------------------- Defs ----------------------------------------------------
def write(content):
    f=open("Stats_dates_d_histoire_Graphic_py.txt","a")
    f.write(content)
    f.close
def write_user_stats(content):
    f=open("see your stats.txt","a")
    f.write(content)
    f.close
def pause():
    pause=input("Please press enter to continue...")
def RAANDOM():
    DATEOREVENT=randint(0,1)
    button1=randint(0,len(dates)-1)
    button2=randint(0,len(dates)-1)
    button3=randint(0,len(dates)-1)
    button4=randint(0,len(dates)-1)
    if DATEOREVENT==1:
        DATEOREVENTT=0
    else:
        DATEOREVENTT=1
    ansswer=randint(1,3)
    print("answer={}".format(ansswer))
    if ansswer==1:
        button1=i
        ranswer=1
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button3={}".format(button3))
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    elif ansswer==2:
        button2=i
        ranswer=2
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button1={}".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    elif ansswer==3:
        button3=i
        ranswer=3
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button1={}".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    else:
        button4=i
        ranswer=4
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button1={}".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button4 or button3==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        while redo!="no":
            print("button3={}".format(button3))
            if button3==i:
                button3=randint(0,len(dates)-1)
            elif button3==button1 or button3==button4 or button3==button2:
                button3=randint(0,len(dates)-1)
            else:
                redo="no"
                break
    return DATEOREVENT, DATEOREVENTT, button1, button2, button3, button4,ranswer
def check(answer, wrightanswer):
    LanguageChosen="n"
    while LanguageChosen!="y":
        if answer==wrightanswer:
            correct(wrightanswer)
            pause()
            LanguageChosen="y"
        else:
            wrong(wrightanswer, answer)
            pause()
            LanguageChosen="y"
        Sleep()
        answer=-1
        DATES=random.randint(0,len(dates)-1)
        DATEOREVENT=random.randint(0,1)
        # 
        wrightanswer=dates[DATES][dateorevent[DATEOREVENT]]
        SLeEP=random.randint(5,50)



def BUTTON1():
    fenetre.destroy()
    global ganswer, wrung
    ganswer=1
    print("ganswer={}".format(ganswer))
    wrung=button1
    return ganswer, wrung
    
def BUTTON2():
    fenetre.destroy()
    global ganswer, wrung
    ganswer=2
    print("ganswer={}".format(ganswer))
    wrung=button2
    return ganswer, wrung
def BUTTON3():
    fenetre.destroy()
    global ganswer, wrung
    ganswer=3
    print("ganswer={}".format(ganswer))
    wrung=button3
    return ganswer, wrung
def BUTTON4():
    fenetre.destroy()
    global ganswer, wrung
    ganswer=4
    print("ganswer={}".format(ganswer))
    wrung=button4
    return ganswer, wrung

def QUIT():
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


    aaaa.mainloop()
    sys.exit(0)
size="260x200"
def wrong(ganswer, ranswer, corres):
    print("Sorry, maby Better luck next time!")
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Wrong")
    aaaa.geometry("310x250")
    aaaa.minsize(310,250)
    Frame1=Frame(aaaa, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(side=TOP, expand=YES, pady=10, fill=X)
    #aaaa.iconbitmap("the icone of the software in.ico")
    aaaa.config(background="#2CDF85")
    label = Label(Frame1, text="Wrong", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="\n Better luck next time!", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="You chose:", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" '{}'".format(ganswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" but the correct answer was ", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="'{}'.".format(ranswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" and corresponded to ", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="'{}'.".format(corres), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()

def correct(wrightanswer):
    print("Well Done, You got the wright answer.\n It was: {}".format(wrightanswer))
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Correct")
    aaaa.geometry("250x200")
    aaaa.minsize(250,200)
    Frame1=Frame(aaaa, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(side=TOP, expand=YES, pady=10, fill=X)
    #aaaa.iconbitmap("the icone of the software in.ico")
    aaaa.config(background="#2CDF85")
    label = Label(Frame1, text="Well Done, You got the wright answer.", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" It was:", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" {}".format(wrightanswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()
    
def window():
    fenetre = Tk()
    fenetre['bg']='white'
    fenetre.title("Language:")
    fenetre.geometry("1000x220")
    fenetre.minsize(1000,220)
    #fenetre.iconbitmap("the icone of the software in.ico")
    fenetre.config(background="#2CDF85")

    Frame1=Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(padx=10, pady=10, fill=X, anchor=CENTER)

    #Frame1=LabelFrame(fenetre, text="Choose You're Language:", padx=10, pady=-10, bg=FBG, fg=FFG)
    #Frame1.pack(fill="both",expand="yes")

    Frame1Top=Frame(Frame1, borderwidth=2, relief=F1T, bg=FBG)
    Frame1Top.pack(side=TOP, padx=10, pady=10, expand=YES, fill=X)

    Frame1bot=Frame(Frame1,borderwidth=2, relief=F1b, bg=FBG)
    Frame1bot.pack(side=BOTTOM, padx=10, pady=10, expand=YES, fill=X)

    Frame1quit=Frame(Frame1,borderwidth=2, relief=F1q, bg=FBG)
    Frame1quit.pack(side=BOTTOM, padx=30, pady=10, expand=YES, fill=X)

    label = Label(Frame1, text="{}:\n {}".format(qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]]), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)

    DE=Button(Frame1, text="{}".format(dates[button1][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON1(ganswer) ,activebackground=hbDE, activeforeground=hfDE)#, value="D")
    DE.pack(side=LEFT,pady=0, expand=YES, padx=5, fill=X)#)

    EN=Button(Frame1,text="{}".format(dates[button2][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON2 ,activebackground=hbEN, activeforeground=hfEN)#, value="E")
    EN.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    FR=Button(Frame1,text="{}".format(dates[button3][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON3 ,activebackground=hbFR, activeforeground=hfFR)#, value="F")
    FR.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    ES=Button(Frame1,text="{}".format(dates[button4][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON4 ,activebackground=hbES, activeforeground=hfES) #, value="ES")
    ES.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    bouton=Button(Frame1quit, text="Quit", font=(Font,Size), bg=WBG, fg=WFG, command=QUIT ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


    fenetre.mainloop()

def refreshQCMS(files):#QCMS
    global QCMS
    QCMS=os.listdir("{}".format(files))
    return QCMS

def refreshscore(files):#Scores
    global Scores
    Scores=os.listdir("{}".format(files))
    return Scores

def writeScore(scOre,files,ChosenQCM):#Scores
    SCORE=open("{}/{}".format(files,ChosenQCM),"w")
    SCORE.write(scOre)
    SCORE.close()
    

def readScore(files,ChosenQCM):#Scores
    SCORE=open("{}/{}".format(files,ChosenQCM),"r")
    scOredata=SCORE.read()
    SCORE.close()
    return scOredata

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
    refreshscore("Score",Scores[ChosenQCM])
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

dates=[
    # {"date":"de 1337-1453 J.-C.","event":"la Guerre de 100 ans"},
    # {"date":"en 1492 J.-C.","event":"la Découverte de L'Amérique"},
    # {"date":"le 29 mai 1453 J.-C.","event":"l'Imprimerie en Europe"},
    {"date":"Wisdom teeth","event":"dent de sagesse"},
    # {"date":"de 1775-1782 J.-C.","event":"la Révolution Américaine"},
    {"date":"A key question","event":"une problématique"},
    {"date":"Consumer society","event":"la société de consommation"},
    {"date":"A minstrel","event":"un ministrel"},
    {"date":"A tomboy","event":"un garçon manqué"},
    {"date":"en 1815 J.-C.","event":"le Congrès de Vienne"},
    # {"date":"de 1861-1865 J.-C.","event":"la Guerre de Sécession"},
    # {"date":"en 1989 J.-C.","event":"la Chute du mur de Berlin"},
    # {"date":"en 1917 J.-C.","event":"la Révolution Russe"},
    # {"date":"au Milieu XIXe J.-C.","event":"la Révolution Industrielle"},
    # {"date":"le 24 octobre 1929 J.-C.","event":"le Jeudi noir"},
    # {"date":"de 1941-1945 J.-C.","event":"Extermination des juifs"},
    # {"date":"le 1er Octobre 1949 J.-C.","event":"La République populaire de Chine"},
    # {"date":"en 1954 J.-C.","event":"Guerre d’Algérie"},
    # {"date":"en 1965 J.-C.","event":"Guerre du Vietnam"},
    # {"date":"le 21 juillet 1969","event":"Le premier pas sur la lune"},
    # {"date":"le 9 novembre 1989","event":"Chute du mur de Berlin"},
    {"date":"le 5 mai 1789","event":"l'Ouverture des états généraux"},
    {"date":"le 20 juin 1789","event":"le serment du jeux de paume"},
    {"date":"le 26 août 1789","event":"l'Adoption de la déclaration des droits de l'homme et du citoyen"},
    {"date":"le 21 juin 1791","event":"la Fuite de Varennes"},
    {"date":"le 17 juillet 1791","event":"la fusillade du Champ-de-Mars"},
    {"date":"le 14 septembre 1791","event":"Louis XVI prête serment à la Constitution"},
    {"date":"le 10 août 1792","event":"la prise des Tuileries avec l'aide des fédérés marseillais"},
    {"date":"le 10 août 1792 (bis)","event":"la Chute de la monarchie et suspension de Louis XVI"},
    {"date":"le 21 septembre 1792","event":"la Convention nationale abolit la royauté et fonde la Ire République au lendemain de la bataille de Valmy"},
    {"date":"le 21 janvier 1793","event":"l'Exécution de Louis XVI"},
    {"date":"le 9 thermidor an II","event":"la Fin de la Terreur et chute de Robespierre"},
    {"date":"le 1er prairial an III","event":"l'Insurrection populaire réclamant le pain et le retour à la Constitution de l'an I (Insurrection violement réprimée dans le sang)"},
    {"date":"le 9 brumaire an IV","event":"le début du Directoire"},
    {"date":"le 18 brumaire an VIII","event":"le Coup d'état établissant le Consulat, dominé par Bonaparte"},

]
write("\n-------------------------------- stats ----------------------------------------\nChemin d'accès:{}\nOS:{}\nDate:{}\ntime:{}\n-------------------------------- end stats ----------------------------------------\n\n-------------------------------- Game Stats ----------------------------------------\nFont:{}\nSize:{}\nWBG:{}\nFBG:{}\nLBG:{}\nWFG:{}\nFFG:{}\nLFG:{}\nF1:{}\nF1T:{}\nF1b:{}\nF1q:{}\nhfDE:{}\nhbDE:{}\nhfEN:{}\nhbEN:{}\nhfFR:{}\nhbFR:{}\nhfES:{}\nhbES:{}\nhfq:{}\nhbq:{}\nscore:{}\nerreur:{}\ndates:\n-------------------------------- End of Game Stats ----------------------------------------\n\n-------------------------------- InGameStats ----------------------------------------\n".format(os.getcwd(),platform.system(),DATE,TIME,Font,Size,WBG,FBG,LBG,WFG,FFG,LFG,F1,F1T,F1b,F1q,hfDE,hbDE,hfEN,hbEN,hfFR,hbFR,hfES,hbES,hfq,hbq,score,erreur,dates))
write_user_stats("\n-------------------------------- stats of the {} ----------------------------------------\n".format(DATE))
for i in range(len(dates)):
    DATEOREVENT=randint(0,1)
    button1,button2,button3,button4=0,0,0,0
    button1=randint(0,len(dates)-1)
    button2=randint(0,len(dates)-1)
    button3=randint(0,len(dates)-1)
    button4=randint(0,len(dates)-1)
    if DATEOREVENT==1:
        DATEOREVENTT=0
    else:
        DATEOREVENTT=1
    ansswer=randint(1,3)
    print("answer={}".format(ansswer))
    if ansswer==1:
        button1=i
        ranswer=1
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button2=i-1
                break
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button3={}".format(button3))
            if button3==i:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button3=i+1
                break
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
                turn+=1
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button4=i-2
                break
            else:
                redo="no"
                break
    elif ansswer==2:
        button2=i
        ranswer=2
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("button1 redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button1={} ansswer2".format(button1))
            write("button1={} ansswer2\n".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button1=i-5
                break
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button2 or button3==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button4={}".format(button4))
            if button3==i:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif button3==button1 or button3==button2 or button3==button4:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button3=i-7
                break
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
                turn+=1
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
                turn==1
            elif turn>50:
                print("turns over 50")
                button4=i-9
                break
            else:
                redo="no"
                break
    elif ansswer==3:
        button3=i
        ranswer=3
        button2=randint(0,len(dates)-1)
        if button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button2=i+10
                break
            else:
                redo="no"
                break
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button1={} ansswer3".format(button1))
            write("button1={} answer3\n".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button1=i-10
                break
            else:
                redo="no"
                break
        button4=randint(0,len(dates)-1)
        if button4==i or button4==button1 or button4==button3 or button4==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button4={}".format(button4))
            if button4==i:
                button4=randint(0,len(dates)-1)
                turn+=1
            elif button4==button1 or button4==button3 or button4==button2:
                button4=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button4=i-3
                break
            else:
                redo="no"
                break
    else:
        button4=i
        ranswer=4
        button2=randint(0,len(dates)-1)
        if button2==i or button2==button1 or button2==button3 or button2==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button2={}".format(button2))
            if button2==i:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif button2==button1 or button2==button3 or button2==button4:
                button2=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button2=i+5
                break
            else:
                redo="no"
                break
        button1=randint(0,len(dates)-1)
        if button1==i or button1==button2 or button1==button3 or button1==button4:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button1={} ansswer4".format(button1))
            write("button1={} ansswer4\n".format(button1))
            if button1==i:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif button1==button2 or button1==button3 or button1==button4:
                button1=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button1=i-6
                break
            else:
                redo="no"
                break
        button3=randint(0,len(dates)-1)
        if button3==i or button3==button1 or button3==button4 or button3==button2:
            redo="redo"
        else:
            redo="no"
        print("redo={}".format(redo))
        turn=0
        while redo!="no":
            print("button3={}".format(button3))
            if button3==i:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif button3==button1 or button3==button4 or button3==button2:
                button3=randint(0,len(dates)-1)
                turn+=1
            elif turn>50:
                print("turns over 50")
                button3=i-4
                break
            else:
                redo="no"
                break
    
    # print("{}: {} ?\n".format(qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]]))
    # answer=input("{}, {}, {} ?".format(dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]], dates[button3][dateorevent[DATEOREVENTT]]))
    fenetre = Tk()
    fenetre['bg']='white'
    fenetre.title("Language:")
    fenetre.geometry("1000x220")
    fenetre.minsize(1000,220)
    #fenetre.iconbitmap("the icone of the software in.ico")
    fenetre.config(background="#2CDF85")

    Frame1=Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(padx=10, pady=10, fill=X, anchor=CENTER)

    #Frame1=LabelFrame(fenetre, text="Choose You're Language:", padx=10, pady=-10, bg=FBG, fg=FFG)
    #Frame1.pack(fill="both",expand="yes")

    Frame1Top=Frame(Frame1, borderwidth=2, relief=F1T, bg=FBG)
    Frame1Top.pack(side=TOP, padx=10, pady=10, expand=YES, fill=X)

    Frame1bot=Frame(Frame1,borderwidth=2, relief=F1b, bg=FBG)
    Frame1bot.pack(side=BOTTOM, padx=10, pady=10, expand=YES, fill=X)

    Frame1quit=Frame(Frame1,borderwidth=2, relief=F1q, bg=FBG)
    Frame1quit.pack(side=BOTTOM, padx=30, pady=10, expand=YES, fill=X)

    label = Label(Frame1, text="{}:\n {}".format(qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]]), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)

    DE=Button(Frame1, text="{}".format(dates[button1][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON1 ,activebackground=hbDE, activeforeground=hfDE)#, value="D")
    DE.pack(side=LEFT,pady=0, expand=YES, padx=5, fill=X)#)

    EN=Button(Frame1,text="{}".format(dates[button2][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON2 ,activebackground=hbEN, activeforeground=hfEN)#, value="E")
    EN.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    FR=Button(Frame1,text="{}".format(dates[button3][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON3 ,activebackground=hbFR, activeforeground=hfFR)#, value="F")
    FR.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    ES=Button(Frame1,text="{}".format(dates[button4][dateorevent[DATEOREVENTT]]), font=(Font,Size), bg=WBG, fg=WFG, command=BUTTON4 ,activebackground=hbES, activeforeground=hfES) #, value="ES")
    ES.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    bouton=Button(Frame1quit, text="Quit", font=(Font,Size), bg=WBG, fg=WFG, command=QUIT ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


    fenetre.mainloop()
    if ganswer==ranswer:
        print("correct")
        print(ranswer)
        print("ganswer={}".format(ganswer))
        correct(dates[i][dateorevent[DATEOREVENTT]])
        # pause()
        score+=1
        erreur+=0
    else:
        print("false")
        print(ranswer)
        print("ganswer={}".format(ganswer))
        wrong(dates[wrung][dateorevent[DATEOREVENTT]],dates[i][dateorevent[DATEOREVENTT]],dates[i][dateorevent[DATEOREVENT]])
        # pause()
        score+=0
        erreur+=1
    write_user_stats("\n________________________________ Round {} Stats ________________________________________\nDATEOREVENT:{}\nbutton1:{}={}\nbutton2:{}={}\nbutton3:{}={}\nbutton4:{}={}\nDATEOREVENTT:{}\nansswer:{}\nredo:{}\n{}: {} ?\n{}, {}, {}, {} ?\nganswer:{}\n________________________________ end Round {} Stats ________________________________________".format(i+1,DATEOREVENT,button1,dates[button1][dateorevent[DATEOREVENTT]],button2,dates[button2][dateorevent[DATEOREVENTT]],button3,dates[button3][dateorevent[DATEOREVENTT]],button4,dates[button4][dateorevent[DATEOREVENTT]],DATEOREVENTT,ansswer,redo,qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]],dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]], dates[button3][dateorevent[DATEOREVENTT]],dates[button4][dateorevent[DATEOREVENTT]],ganswer,i+1))
    write("\n________________________________ Round {} Stats ________________________________________\nDATEOREVENT:{}\nbutton1:{}\nbutton2:{}\nbutton3:{}\nbutton4:{}\nAnswer with:{}\n Correct answer:{}\nQuestion: {}: {} ?\nChoices: {}, {}, {}, {}\ngiven answer:{}\n________________________________ end Round {} Stats ________________________________________".format(i+1,dateorevent[DATEOREVENT],dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]],dates[button3][dateorevent[DATEOREVENTT]],dates[button4][dateorevent[DATEOREVENTT]],dateorevent[DATEOREVENTT],dates[ranswer][dateorevent[DATEOREVENTT]],qdateorevent[DATEOREVENTT],dates[i][dateorevent[DATEOREVENT]],dates[button1][dateorevent[DATEOREVENTT]],dates[button2][dateorevent[DATEOREVENTT]],dates[button3][dateorevent[DATEOREVENTT]],dates[button4][dateorevent[DATEOREVENTT]],ganswer,i+1))

write("\n-------------------------------- end of InGameStats ----------------------------------------\n{} Created by Henry Letellier".format(chr(169)))
write_user_stats("\n-------------------------------- end of stats of the {} ----------------------------------------\n".format(DATE))

print(" You have {} point(s) and have made {} mistake(s).".format(score,erreur))
print("{} Created by Henry Letellier".format(chr(169)))

QUIT()