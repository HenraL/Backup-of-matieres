from random import*
from tkinter import*
import os, platform, datetime
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)
TIME="{}:{}:{}".format(date.hour,date.minute,date.second)
graphortypechoicemade,score,erreur,ganswer,wrung="no",0,0,0,0
# 
# -------------------------------- Variables ----------------------------------------
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
BACKGround="#2CDF85"
# ---------------------------------------------------- Defs ----------------------------------------------------
def write(content):
    f=open("QCM_global_stats_debugger.txt","a")
    f.write(content)
    f.close
def write_user_stats(content):
    f=open("see your stats.txt","a")
    f.write(content)
    f.close
def pause():pause=input("Please press enter to continue...")
def error(TypeOfMCQ):
    aaaa = Tk()
    aaaa['bg']='white'
    aaaa.title("Correct")
    aaaa.geometry("250x200")
    aaaa.minsize(250,200)
    Frame1=Frame(aaaa, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(side=TOP, expand=YES, pady=10, fill=X)
    #aaaa.iconbitmap("the icone of the software in.ico")
    aaaa.config(background="#2CDF85")
    label = Label(Frame1, text="ERROR!!", font=(Font,Size,"Bold"), bg=LBG, fg="Red")
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="This question has been skipped because it did not fit the supported options.", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" the Question must have : einther 2, 3 or 4 possible answers.", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="You have {} answer(s) in this question.".format(TypeOfMCQ), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="Close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()
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
        answer=-1
        DATES=random.randint(0,len(dates)-1)
        DATEOREVENT=random.randint(0,1)
        # 
        wrightanswer=QCM[i]["correct"]
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
def QUITend():
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
    bouton=Button(aaaa, text="Close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()

def correct(corres,wrightanswer):
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
    label = Label(Frame1, text="{}".format(corres), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text="Does correspond to ", font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    label = Label(Frame1, text=" {}".format(wrightanswer), font=(Font,Size), bg=LBG, fg=LFG)
    label.pack(side=TOP, pady=0, expand=YES,fill=X)#padx=5)
    bouton=Button(aaaa, text="Close", font=(Font,Size), bg=WBG, fg=WFG, command=aaaa.destroy ,activebackground=hbq, activeforeground=hfq)
    bouton.pack(side=BOTTOM,pady=10, expand=YES,fill=X)#padx=5)
    aaaa.mainloop()
    
def window():
    fenetre = Tk()
    fenetre['bg']='white'
    fenetre.title("Language:")
    fenetre.geometry("1000x220")
    fenetre.minsize(1000,220)
    #fenetre.iconbitmap("the icone of the software in.ico")
    fenetre.config(background=BACKGround)

    Frame1=Frame(fenetre, borderwidth=2, relief=F1, bg=FBG)
    Frame1.pack(padx=10, pady=10, fill=X, anchor=CENTER)

    Frame1Top=Frame(Frame1, borderwidth=2, relief=F1T, bg=FBG)
    Frame1Top.pack(side=TOP, padx=10, pady=10, expand=YES, fill=X)

    Frame1bot=Frame(Frame1,borderwidth=2, relief=F1b, bg=FBG)
    Frame1bot.pack(side=BOTTOM, padx=10, pady=10, expand=YES, fill=X)

    Frame1quit=Frame(Frame1,borderwidth=2, relief=F1q, bg=FBG)
    Frame1quit.pack(side=BOTTOM, padx=30, pady=10, expand=YES, fill=X)

    label = Label(Frame1, text="{}: {}".format(i,i), font=(Font,Size), bg=LBG, fg=LFG)
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

QCM=[
    {"date":"le 5 mai 1789","event":"l'Ouverture des états généraux"},
    {"date":"le 20 juin 1789","event":"le serment du jeux de paume"},
    {"date":"le 14 Juillet 1789","event":"la Prise de la bastille"},
    {"date":"le 4 août 1789","event":"Abolition des privilèges"},
    {"date":"le 26 août 1789","event":"Déclaration des droits de l'homme et du citoyen"},
    {"date":"le 2 novembre 1789 - 9 novembre 1799","event":"la Révolution française"},
    {"date":"le 21 juin 1791","event":"la Fuite du roi à Varennes"},
    {"date":"le 17 juillet 1791","event":"la fusillade du Champ-de-Mars"},
    {"date":"le 14 septembre 1791","event":"Louis XVI prête serment à la Constitution"},
    {"date":"le 10 août 1792","event":"la prise des Tuileries avec l'aide des fédérés marseillais"},
    {"date":"le 10 août 1792 (bis)","event":"la Chute de la monarchie"},
    {"date":"le 10 août 1792 (tiers)","event":"suspension de Louis XVI"},
    {"date":"le 20 septembre 1792","event":"victoire de Valmy"},
    {"date":"le 21 septembre 1792","event":"la Convention nationale abolit la royauté et fonde la Ire République au lendemain de la bataille de Valmy"},
    {"date":"le 22 septembre 1792","event":"Proclamation de la première république"},
    {"date":"le 21 janvier 1793","event":"l'Exécution de Louis XVI"},
    {"date":"le 26 juin 1794","event":"La baitaille de Fleurus"},
    {"date":"le 9 thermidor an II (29 juillet 1794)","event":"la Fin de la Terreur et chute de Robespierre"},
    {"date":"en 1795","event":"le Directoire"},
    {"date":"en 1796","event":"la campagne d'Italie"},
    {"date":"le 1er prairial an III (1795)","event":"l'Insurrection populaire réclamant le pain et le retour à la Constitution de l'an I (Insurrection violement réprimée dans le sang)"},
    {"date":"le 9 brumaire an IV (1796)","event":"le début du Directoire"},
    {"date":"le 18 et 19 brumaire an VIII (9 et 10 novembre 1799)","event":"le Coup d'état établissant le Consulat, dominé par Bonaparte"},
    {"date":"en 1815 ","event":"le Congrès de Vienne"}
    # {"date":"","event":""}
]

def TypeOfMCQ3(button1,button2,button3):
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
def TypeOfMCQ4(button1,button2,button3,button4):
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

write("\n-------------------------------- stats ----------------------------------------\nChemin d'accès:{}\nOS:{}\nDate:{}\ntime:{}\n-------------------------------- end stats ----------------------------------------\n\n-------------------------------- Game Stats ----------------------------------------\nFont:{}\nSize:{}\nWBG:{}\nFBG:{}\nLBG:{}\nWFG:{}\nFFG:{}\nLFG:{}\nF1:{}\nF1T:{}\nF1b:{}\nF1q:{}\nhfDE:{}\nhbDE:{}\nhfEN:{}\nhbEN:{}\nhfFR:{}\nhbFR:{}\nhfES:{}\nhbES:{}\nhfq:{}\nhbq:{}\nscore:{}\nerreur:{}\ndates:\n-------------------------------- End of Game Stats ----------------------------------------\n\n-------------------------------- InGameStats ----------------------------------------\n".format(os.getcwd(),platform.system(),DATE,TIME,Font,Size,WBG,FBG,LBG,WFG,FFG,LFG,F1,F1T,F1b,F1q,hfDE,hbDE,hfEN,hbEN,hfFR,hbFR,hfES,hbES,hfq,hbq,score,erreur,dates))
write_user_stats("\n-------------------------------- stats of the {} ----------------------------------------\n".format(DATE))
for i in range(len(dates)):
    TypeOfMCQ=len(date[i])
    rightanswer=QCM[i]["correct"]
    button1,button2,button3,button4=0,0,0,0
    if TypeOfMCQ==2:
        button1=randint(1,2)
        button2=randint((len(dates[i])+1),(len(dates[i])-1))
        button3=randint(len(dates[i+1],len(dates[i-1])))
        button4=randint(len(dates[i+2],len(dates[i-2])))
        while button1==button2:button2=randint(1,2)
    elif TypeOfMCQ==3:
        button1=randint((len(dates[i])+1),(len(dates[i])-1))
        button2=randint((len(dates[i])+1),(len(dates[i])-1))
        button3=randint((len(dates[i])+1),(len(dates[i])-1))
        button4=randint(len(dates[i+1],len(dates[i-1])))
        if button1==button2 or button1==button3 or button2==button3:TypeOfMCQ3(button1,button2,button3)
    elif TypeOfMCQ==4:
        button1=randint((len(dates[i])+1),(len(dates[i])-1))
        button2=randint((len(dates[i])+1),(len(dates[i])-1))
        button3=randint((len(dates[i])+1),(len(dates[i])-1))
        button4=randint((len(dates[i])+1),(len(dates[i])-1))
    else:
        error(TypeOfMCQ)
    # print("answer={}".format(ansswer))
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
        correct(dates[i][dateorevent[DATEOREVENT]],dates[i][dateorevent[DATEOREVENTT]])
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

QUITend()
print(" You have {} point(s) and have made {} mistake(s).".format(score,erreur))
print("{} Created by Henry Letellier".format(chr(169)))
