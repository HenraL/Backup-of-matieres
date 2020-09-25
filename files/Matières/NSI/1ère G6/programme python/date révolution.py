import random
from time import sleep
from tkinter import*
dates=[
    {"date":"de 1337-1453 J.-C.","event":"la Guerre de 100 ans"},
    {"date":"en 1492 J.-C.","event":"la Découverte de L’Amérique"},
    {"date":"le 29 mai 1453 J.-C.","event":"l'Imprimerie en Europe"},
    {"date":"en 1682 J.-C.","event":"Louis XIV à Versailles"},
    {"date":"de 1775-1782 J.-C.","event":"la Révolution Américaine"},
    {"date":"le 2 novembre 1789 - 9 novembre 1799","event":"la Révolution française"},
    {"date":"le 14 Juillet 1789 J.-C.","event":"la Prise de la bastille"},
    {"date":"le 2 Décembre 1804 J.-C.","event":"le Sacre de Napoléon"},
    {"date":"de 1811-1820 J.-C.","event":"l'Indépendance En Amérique du Sud"},
    {"date":"en 1815 J.-C.","event":"le Congrès de Vienne"},
    {"date":"de 1861-1865 J.-C.","event":"la Guerre de Sécession"},
    {"date":"en 1989 J.-C.","event":"la Chute du mur de Berlin"},
    {"date":"en 1917 J.-C.","event":"la Révolution Russe"},
    {"date":"au Milieu XIXe J.-C.","event":"la Révolution Industrielle"},
    {"date":"le 24 octobre 1929 J.-C.","event":"le Jeudi noir"},
    {"date":"de 1941-1945 J.-C.","event":"Extermination des juifs"},
    {"date":"le 1er Octobre 1949 J.-C.","event":"La République populaire de Chine"},
    {"date":"en 1954 J.-C.","event":"Guerre d’Algérie"},
    {"date":"en 1965 J.-C.","event":"Guerre du Vietnam"},
    {"date":"le 21 juillet 1969","event":"Le premier pas sur la lune"},
    {"date":"le 9 novembre 1989","event":"Chute du mur de Berlin"},
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
    {"date":"le 9 thermidor an II","event":"la Fin de la Terruer et chute de Robespierre"},
    {"date":"le 1er prairial an III","event":"l'Insurrection populaire réclamant le pain et le retour à la Constitution de l'an I (Insurrection violement réprimée dans le sang)"},
    {"date":"le 9 brumaire an IV","event":"le début du Directoire"},
    {"date":"le 18 brumaire an VIII","event":"le Coup d'état établissant le Consulat, dominé par Bonaparte"},

]
    # {"date":"","event":""}
dateorevent=["date","event"]
# placeanswer=[i+2,i+1,i,i-1,i-2]
# def Randoms(dateorevent,dates):
#     DATES=random.randint(0,len(dates)-1)
#     DATEOREVENT=random.randint(0,1)
# # 
#     wrightanswer=dates[DATES][dateorevent[DATEOREVENT]]
#     SLeEP=random.randint(5,50)
#     return DATEOREVENT, DATES,wrightanswer,SLeEP

# Randoms(dateorevent,dates)

DATES=random.randint(0,len(dates)-1)
DATEOREVENT=random.randint(0,1)
# 
wrightanswer=dates[DATES][dateorevent[DATEOREVENT]]
SLeEP=random.randint(5,50)

def pause():
    pause=input("Please press enter to continue...")
print ("pause................................[OK]")

def SLEEP(SleEP):
    fenetre.destroy()
    sleep(SLeEP)
    # randoms(dateorevent,dates)
def RANDOMISERS(DATES, DATEOREVENT):
    BU=[]
    for b in range(4):
        z=random.randint(DATES-1,DATES+2)
        for alpha in range(len(BU)):
            if BU[alpha]==z:
                while BU[alpha]==z:
                    z=random.randint(DATES-1,DATES+2)
                    alpha=0
            else:
                BU.append(z)
            

def languageDE():
    fenetre.destroy()
    answer="1"
    return answer
def languageE():
    fenetre.destroy()
    answer="2"
    return answer
def languageF():
    fenetre.destroy()
    answer="3"
    return answer
def languageES():
    fenetre.destroy()
    answer="4"
    return answer

def languagequit():
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
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


    aaaa.mainloop()
    sys.exit(0)

def wrong(wrightanswer, answer):
    fenetre.destroy()
    print("Sorry, maby Better luck next time!")
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Wrong")
    aaaa.geometry("250x200")
    aaaa.minsize(250,200)
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
    label = Label(Frame1, text=" '{}'".format(answer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" but the correct answer was ", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="'{}'.".format(wrightanswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()

def correct(wrightanswer):
    fenetre.destroy()
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
#----------------------------- First window ---------------------------------------
main="y"
while main=="y":
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

    label = Label(Frame1, text="Quand a été:\n {}".format(wrightanswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=10, expand=YES,fill=X)#padx=5)

    DE=Button(Frame1, text="Germanddddddddddddddddddddddddddddddddddddddddddddddddddddddddd", font=(Font,Size), bg=WBG, fg=WFG, command=languageDE ,activebackground=hbDE, activeforeground=hfDE)#, value="D")
    DE.pack(side=LEFT,pady=0, expand=YES, padx=5, fill=X)#)

    EN=Button(Frame1,text="English", font=(Font,Size), bg=WBG, fg=WFG, command=languageE ,activebackground=hbEN, activeforeground=hfEN)#, value="E")
    EN.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    FR=Button(Frame1,text="French", font=(Font,Size), bg=WBG, fg=WFG, command=languageF ,activebackground=hbFR, activeforeground=hfFR)#, value="F")
    FR.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    ES=Button(Frame1,text="Spanish", font=(Font,Size), bg=WBG, fg=WFG, command=languageES ,activebackground=hbES, activeforeground=hfES)#, value="ES")
    ES.pack(side=LEFT,pady=0, expand=YES,padx=5, fill=X)#)

    bouton=Button(Frame1quit, text="Quit", font=(Font,Size), bg=WBG, fg=WFG, command=languagequit ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)


    fenetre.mainloop()

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


